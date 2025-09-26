"""Python interface for the Controller Process of the Supervisor."""

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
        orchestrator: str = "GKE",
    ):
        """Constructs the Controller object.

        Args:
            port: The port on which to run the controller communication.
            num_grpc_threads: The number of gRPC threads to initialize for communication.
            supervisor_config: The config object for Supervisor components.
        """
        if not supervisor_config:
            supervisor_config = adaptr_core.SupervisorClient(
                adaptr_core.SupervisorConfig.from_environment()
            )

        self._controller = adaptr_core.Controller(
            port=port,
            num_grpc_threads=num_grpc_threads,
            config=supervisor_config,
            command_handle_fn=self.command_handler,
            update_handle_fn=self.update_handler,
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

        self._is_initialized = False

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
    def callbacks(self) -> dict:
        """Returns the callbacks used by the controller."""
        return self._callbacks

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

    def shutdown(self):
        """Shuts down the controller process and child threads."""
        self._controller.shutdown()

    def wait_for_completion(self):
        """Waits for all hosts registered to controller to finish their workloads."""
        while not self._controller.is_complete():
            time.sleep(10)

    def update_handler(self, state: adaptr_core.SupervisorState):
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

    def command_handler(self, command: adaptr_core.Command):
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
