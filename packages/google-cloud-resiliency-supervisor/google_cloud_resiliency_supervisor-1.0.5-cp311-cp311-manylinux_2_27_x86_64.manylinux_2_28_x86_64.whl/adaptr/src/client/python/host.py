import logging
import redis
import time

import adaptr_core
from adaptr.src.core.python import device_info
from adaptr.src.client.python import utils
from adaptr.src.client.python import worker
from adaptr.src.watchdogs.python import base_watchdog, ecc_watchdog, xid_watchdog


class Host:
    """Abstraction of host processes including communication thread with Supervisor.

    Stores all metadata related to a host process, including physical host attributes
    and host rank. Additionally, this abstraction houses the communication infrastructure
    between the host and the Supervisor process, as well as between the host and its
    Worker processes.
    """

    def __init__(
        self,
        project_id: str,
        port: int,
        redis_port: int,
        workers_per_host: int = 8,
        worker_timeout_s: int = 60,
        address: str | None = None,
        supervisor_config: adaptr_core.SupervisorConfig | None = None,
        watchdogs: list[str] | None = None,
        watchdog_check_interval_s: int = 30,
    ):
        """Constructs a Host object.

        Args:
            project_id: The name of the GCP project.
            port: The port on which to run the host communication with supervisor.
            redis_port: The port on which to run redis.
            workers_per_host: The maximum number of workers per host. Default is 8.
            worker_timeout_s: The time before registering a host as spare capacity.
            address: The address for other processes to communicate with this host. In Kubernetes environments this refers to the FQDN.
            supervisor_config: The config object to set up communication with the supervisor. If not provided, will be loaded from SupervisorConfig.from_environment().
            watchdogs: The list of watchdogs to enable in the host. Valid values are 'ECC' and 'XID'.
            watchdog_check_interval_s: The time interval in seconds between watchdog checks.
        """
        if workers_per_host < 1:
            raise ValueError("workers_per_host must be a positive integer.")

        self._host_project_id = project_id
        host_name = utils.get_host_name()

        superblock_id, subblock_id, host_serial_number = (
            utils.get_host_physical_attributes(
                project_id=project_id,
                zone=utils.get_host_zone(),
                host_name=host_name,
            )
        )

        if address:
            host_address = address
        else:
            host_address = utils.get_host_ip()

        utils.check_and_clean_port(port)

        self._host_info = device_info.HostInfo(
            host_address=host_address + ":" + str(port),
            host_id=utils.get_host_id(),
            host_serial_number=host_serial_number,
            subblock_id=subblock_id,
            superblock_id=superblock_id,
            zone=utils.get_host_zone(),
            host_name=host_name,
        )
        self._workers_per_host = workers_per_host

        if not supervisor_config:
            supervisor_config = adaptr_core.SupervisorConfig.from_environment()

        self._host = adaptr_core.Host(
            port=port,
            num_grpc_threads=workers_per_host,
            num_workers_per_host=workers_per_host,
            worker_timeout_s=worker_timeout_s,
            host_info=self.export_info(),
            config=supervisor_config,
        )
        self._host.start_server()
        while not self._host.is_ready():
            continue

        self._workers = {}
        self._worker_training_states = {}

        # Assign redis port and client
        self._redis_port = redis_port
        self._redis_client = redis.Redis(host="localhost", port=redis_port, db=0)

        # Clean termination files
        utils.clean_termination_files()

        self._watchdogs: dict[str, base_watchdog.BaseWatchdog] = {}
        self._watchdog_check_interval = watchdog_check_interval_s

        if watchdogs is not None:
            for watchdog in watchdogs:
                if watchdog == "ecc":
                    self._watchdogs["ecc"] = ecc_watchdog.ECCWatchdog()
                elif watchdog == "xid":
                    self._watchdogs["xid"] = xid_watchdog.XIDWatchdog()
                else:
                    raise ValueError(f"Invalid watchdog: {watchdog}")

    def __repr__(self):
        return self.host_name

    @property
    def host_info(self) -> device_info.HostInfo:
        """The host information."""
        return self._host_info

    @property
    def max_workers_per_host(self) -> int:
        """The number max number of workers per host."""
        return self._workers_per_host

    @property
    def host_name(self) -> str:
        """The unique host name."""
        return self.host_info.host_name

    @property
    def host_address(self) -> str:
        """The address to communicate with the host."""
        return self.host_info.host_address

    @property
    def port(self) -> int:
        """The port to communicate with the host."""
        return int(self.host_address.split(":")[-1])

    @property
    def state(self) -> int:
        """The state of the host."""
        return self.host_info.state

    @property
    def project(self) -> str:
        """The project ID associated with the host."""
        return self._host_project_id

    @property
    def zone(self) -> str:
        """The zone where the host is located."""
        return self.host_info.zone

    @property
    def host_id(self) -> str:
        """The unique host ID."""
        return self.host_info.host_id

    @property
    def host_serial_number(self) -> str:
        """The unique host serial number."""
        return self.host_info.host_serial_number

    @property
    def workers(self) -> dict[str, worker.Worker]:
        """The list of workers registered to this host."""
        return self._workers

    @property
    def redis_port(self):
        """The port on which to run redis."""
        return self._redis_port

    @property
    def redis_client(self):
        """The redis client."""
        return self._redis_client

    @property
    def num_workers(self) -> int:
        """The number of workers currently assigned to the host."""
        return self._host.num_workers()

    def report_event(self, event_reports: list[adaptr_core.EventReport]):
        """Report watchdog detected errors to the Supervisor."""
        event_reports_proto = adaptr_core.EventReports()
        event_reports_proto.event_reports = event_reports
        self._host.report_event(event_reports_proto)

    def shutdown(self):
        """Shuts down host."""
        logging.info(f"Shutting down Host {self.host_name}")
        self._host.shutdown()
        utils.create_termination_file()

    def await_completion(self):
        """Waits for all workers registered to host to finish their workloads."""

        logging.info(f"{self.host_name}: awaiting completion...")
        while not self._host.is_complete():
            # Update host information in Python
            self.update_info(self._pull_info_from_cc())

            if (
                self._watchdogs
                and self.host_info.state == device_info.DeviceState.RUNNING
            ):
                logging.info(
                    f"{self.host_name}: Checking for watchdogs for detected errors..."
                )

                error_reports = []
                for watchdog in self._watchdogs.values():
                    error_reports.extend(watchdog.poll())

                if error_reports:
                    for error_report in error_reports:
                        device_id = error_report.device_id
                        for worker in self.host_info.workers:
                            if worker.worker_id == device_id:
                                worker.state = device_info.DeviceState.FAILED

                        error_report.host_info = self.export_info()

                    # Update host information in C++ and report events
                    self._push_info_to_cc(self.export_info())
                    self.report_event(error_reports)
            else:
                logging.info(f"{self.host_name}: No watchdogs enabled...")

            time.sleep(self._watchdog_check_interval)

    def export_info(self) -> adaptr_core.HostInfo:
        """Exports Host object into adaptr_core HostInfo object."""
        return self.host_info.export_info()

    def update_info(self, host_info: adaptr_core.HostInfo):
        """Update the metadata associated with the worker."""
        self.host_info.update_info(host_info)

    def start_heartbeat(self):
        """Initializes heartbeating after all expected workers are online."""
        self._host.start_heartbeat()

    def _pull_info_from_cc(self) -> adaptr_core.HostInfo:
        """Pull the latest host information from C++ process."""
        return self._host.export_info()

    def _push_info_to_cc(self, host_info: adaptr_core.HostInfo):
        """Push the latest host information to C++ process."""
        self._host.update_info(host_info)
