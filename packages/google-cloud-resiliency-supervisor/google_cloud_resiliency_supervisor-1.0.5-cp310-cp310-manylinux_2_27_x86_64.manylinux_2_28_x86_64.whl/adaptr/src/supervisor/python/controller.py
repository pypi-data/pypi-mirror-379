"""Python interface for the Controller Process of the Supervisor."""

import collections
from collections.abc import Callable
import logging
import time

import adaptr_core
from adaptr.src.core.python import utils
from adaptr.src.supervisor.python import orchestrators


class Controller:
    """Abstraction of controller processes of the Supervisor.

    Stores all metadata related to the Controller process and provides an interface to
    interact with the Controller process. The Controller process is responsible for
    computing new cluster states given events reported by the Controller.
    """

    def __init__(
        self,
        port: int,
        num_grpc_threads: int,
        supervisor_config: adaptr_core.SupervisorConfig | None = None,
        event_handler: Callable[[adaptr_core.EventReports], None] | None = None,
        orchestrator: str = "GKE",
    ):
        """Constructs the Controller object.

        Args:
            port: The port on which to run the controller communication.
            num_grpc_threads: The number of gRPC threads to initialize for communication.
            supervisor_config: The config object for Supervisor components.
            event_handler: The policy to handle detected events.
            orchestrator: The orchestrator to use for the controller.
        """
        if not supervisor_config:
            supervisor_config = adaptr_core.SupervisorClient(
                adaptr_core.SupervisorConfig.from_environment()
            )

        self._controller = adaptr_core.Controller(
            port=port,
            num_grpc_threads=num_grpc_threads,
            config=supervisor_config,
            command_handle_fn=self._command_handler,
            update_handle_fn=self._update_handler,
            event_handle_fn=event_handler if event_handler else self._event_handler,
        )

        self._controller.start()
        while not self._controller.is_ready():
            continue

        self._controller_address = supervisor_config.controller_address
        logging.info(
            f"Successfully started controller process at address: {self.address}"
        )

        self._orchestrator_callbacks = orchestrators.get_orchestrator_callbacks(
            orchestrator
        )

        self._failure_counter = collections.defaultdict(int)

    def __repr__(self) -> str:
        return f"{self.name}@{self.address}"

    @property
    def name(self) -> str:
        """Returns the name of the Controller process."""
        return "controller"

    @property
    def address(self) -> str:
        """Returns the address of the Controller process."""
        return self._controller_address

    @property
    def num_registered_hosts(self) -> str:
        """Returns the total number of hosts currently tracked by the controller."""
        return self._controller.num_hosts()

    @property
    def num_workers(self) -> str:
        """Returns the number of workers participating in training currently tracked by the controller."""
        return self._controller.num_workers()

    @property
    def num_running_hosts(self) -> str:
        """Returns the number of hosts participating in training currently tracked by the controller."""
        return self._controller.num_running_hosts()

    @property
    def num_spare_hosts(self) -> str:
        """Returns the number of idle hosts currently tracked by the controller."""
        return self._controller.num_spare_hosts()

    @property
    def failure_counter(self) -> dict[str, int]:
        """Returns the failure counter for each host currently tracked by the controller."""
        return self._failure_counter

    def shutdown(self):
        """Shuts down the controller process and child threads."""
        self._controller.shutdown()

    def wait_for_completion(self):
        """Waits for all hosts registered to controller to finish their workloads."""
        while not self._controller.is_complete():
            time.sleep(10)

    def _update_handler(self, state: adaptr_core.SupervisorState):
        """Handle update requests to synchronize C++ and Python Supervisor state.

        Args:
            state: The current supervisor state coming from the C++ controller.
        """
        if not isinstance(state, adaptr_core.SupervisorState):
            raise ValueError(
                (
                    f"Invalid callback argument type: {type(state)}. "
                    "The callback argument must be of type SupervisorState."
                )
            )

    def _event_handler(self, event_reports: adaptr_core.EventReports):
        """Handle event reports from the C++ controller.

        Args:
            event_reports: The event reports recieved from the C++ controller.
        """
        if not isinstance(event_reports, adaptr_core.EventReports):
            raise ValueError(
                (
                    f"Invalid callback argument type: {type(event_reports)}. "
                    "The callback argument must be of type EventReports."
                )
            )
        event_report = event_reports.event_reports[0]
        event_type = event_report.event_type
        host_info = event_report.host_info

        logging.info(f"Received event report: {event_report.message}")

        if event_type == adaptr_core.EventType.WORKER_HB:
            # Only Reset Hosts in preparation for framework-level reset
            self._controller.trigger_nvrx_reset()

        elif (event_type == adaptr_core.EventType.HOST_HB or
            event_type == adaptr_core.EventType.XID or
            event_type == adaptr_core.EventType.ECC):

            self.failure_counter[host_info.host_name] += 1

            # Attempt pod-level reset first, escalate to hot-swap if unsuccessful
            if self.failure_counter[host_info.host_name] <= 1:
                self._controller.trigger_job_reset(host_info)
            else:
                self._controller.trigger_hot_swap(host_info)
                self.failure_counter[host_info.host_name] = 0

    def _command_handler(self, command: adaptr_core.Command):
        """Handle orchestrator level command issued by C++ controller.

        Args:
            command: The command recieved from the C++ controller.
        """
        if not isinstance(command, adaptr_core.Command):
            raise ValueError(
                (
                    f"Invalid callback argument type: {type(command)}. "
                    "The callback argument must be of type Command."
                )
            )
        for callback, kwargs in zip(command.callback_names, command.callback_kwargs):
            kwargs = utils.destringify_kwargs(kwargs)
            if callback not in self._orchestrator_callbacks:
                raise ValueError(f"Unexpected callback {callback} recieved.")

            self._orchestrator_callbacks[callback](**kwargs)
