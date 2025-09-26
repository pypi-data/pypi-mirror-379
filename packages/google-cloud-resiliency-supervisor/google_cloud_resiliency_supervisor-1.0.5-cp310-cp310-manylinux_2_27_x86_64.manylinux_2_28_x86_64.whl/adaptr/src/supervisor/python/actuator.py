"""Python interface for the Actuator Process of the Supervisor."""

import logging
import time

import adaptr_core


class Actuator:
    """Abstraction of actuator processes of the Supervisor.

    Stores all metadata related to the Actuator process and provides an interface to
    interact with the Actuator process. The Actuator process is responsible for
    communicating Optimizer commands to Hosts in the cluster.
    """

    def __init__(
        self,
        port: int,
        num_grpc_threads: int,
        supervisor_config: adaptr_core.SupervisorConfig | None = None,
    ):
        """Constructs the Actuator object.

        Args:
            port: The port on which to run the actuator communication.
            num_grpc_threads: The number of gRPC threads to initialize for communication.
            supervisor_config: The config object for Supervisor components.
        """
        if not supervisor_config:
            supervisor_config = adaptr_core.SupervisorClient(
                adaptr_core.SupervisorConfig.from_environment()
            )

        self._actuator = adaptr_core.Actuator(
            port=port, num_grpc_threads=num_grpc_threads, config=supervisor_config
        )

        self._actuator.start()
        while not self._actuator.is_ready():
            continue

        self._actuator_address = supervisor_config.actuator_address
        logging.info(
            f"Successfully started actuator process at address: {self.address}"
        )

    def __repr__(self) -> str:
        return f"{self.name}@{self.address}"

    @property
    def name(self) -> str:
        """Returns the name of the Actuator process."""
        return "actuator"

    @property
    def address(self) -> str:
        """Returns the address of the Actuator process."""
        return self._actuator_address

    @property
    def num_registered_hosts(self) -> str:
        """Returns the total number of hosts currently tracked by the actuator."""
        return self._actuator.num_registered_hosts()

    @property
    def num_active_workers(self) -> str:
        """Returns the number of workers participating in training currently tracked by the actuator."""
        return self._actuator.num_active_workers()

    @property
    def num_active_hosts(self) -> str:
        """Returns the number of hosts participating in training currently tracked by the actuator."""
        return self._actuator.num_active_hosts()

    @property
    def num_available_workers(self) -> str:
        """Returns the number of idle workers currently tracked by the actuator."""
        return self._actuator.num_available_workers()

    @property
    def num_available_hosts(self) -> str:
        """Returns the number of idle hosts currently tracked by the actuator."""
        return self._actuator.num_available_hosts()

    def shutdown(self):
        """Shuts doen the actuator process and child threads."""
        self._actuator.shutdown()

    def wait_for_completion(self):
        """Waits for all hosts registered to actuator to finish their workloads."""
        while not self._actuator.is_complete():
            time.sleep(10)
