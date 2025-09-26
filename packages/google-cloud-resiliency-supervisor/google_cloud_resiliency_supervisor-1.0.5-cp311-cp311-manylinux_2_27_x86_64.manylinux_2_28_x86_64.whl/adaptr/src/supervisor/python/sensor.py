"""Python interface for the Sensor Process of the Supervisor."""

import logging
import time

import adaptr_core


class Sensor:
    """Abstraction of sensor processes of the Supervisor.

    Stores all metadata related to the Sensor process and provides an interface to
    interact with the Sensor process. The Sensor process is responsible for
    polling Hosts for cluster liveliness.
    """

    def __init__(
        self,
        port: int,
        num_grpc_threads: int,
        supervisor_config: adaptr_core.SupervisorConfig | None = None,
    ):
        """Constructs the Sensor object.

        Args:
            port: The port on which to run the sensor communication.
            num_grpc_threads: The number of gRPC threads to initialize for communication.
            supervisor_config: The config object for Supervisor components.
        """
        if not supervisor_config:
            supervisor_config = adaptr_core.SupervisorClient(
                adaptr_core.SupervisorConfig.from_environment()
            )

        self._sensor = adaptr_core.Sensor(
            port=port,
            num_grpc_threads=num_grpc_threads,
            config=supervisor_config,
        )

        self._sensor.start()
        while not self._sensor.is_ready():
            continue

        self._sensor_address = supervisor_config.sensor_address
        logging.info(f"Successfully started sensor process at address: {self.address}")

    def __repr__(self) -> str:
        return f"{self.name}@{self.address}"

    @property
    def name(self) -> str:
        """Returns the name of the Sensor process."""
        return "sensor"

    @property
    def address(self) -> str:
        """Returns the address of the Sensor process."""
        return self._sensor_address

    @property
    def num_registered_hosts(self) -> str:
        """Returns the total number of hosts currently tracked by the sensor."""
        return self._sensor.num_registered_hosts()

    @property
    def num_active_workers(self) -> str:
        """Returns the number of workers participating in training currently tracked by the sensor."""
        return self._sensor.num_active_workers()

    @property
    def num_active_hosts(self) -> str:
        """Returns the number of hosts participating in training currently tracked by the sensor."""
        return self._sensor.num_active_hosts()

    @property
    def num_available_workers(self) -> str:
        """Returns the number of idle workers currently tracked by the sensor."""
        return self._sensor.num_available_workers()

    @property
    def num_available_hosts(self) -> str:
        """Returns the number of idle hosts currently tracked by the sensor."""
        return self._sensor.num_available_hosts()

    def shutdown(self):
        """Shuts doen the sensor process and child threads."""
        self._sensor.shutdown()

    def wait_for_completion(self):
        """Waits for all hosts registered to sensor to finish their workloads."""
        while not self._sensor.is_complete():
            time.sleep(10)
