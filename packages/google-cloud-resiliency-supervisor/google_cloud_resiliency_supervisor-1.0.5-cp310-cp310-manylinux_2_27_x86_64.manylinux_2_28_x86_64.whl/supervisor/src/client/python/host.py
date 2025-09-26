"""Abstraction of host processes including communication thread with Supervisor."""

import time

from supervisor.src.client.python import utils
from supervisor.src.client.python import worker
from supervisor.src.core.python import device_info
from supervisor.src.core.python import utils as core_utils
from supervisor.src.watchdogs.python import base_watchdog
from supervisor.src.watchdogs.python import ecc_watchdog
from supervisor.src.watchdogs.python import xid_watchdog
import supervisor_core


class Host:
  """Abstraction of host processes including communication thread with Supervisor.

  Stores all metadata related to a host process, including physical host
  attributes and host rank. Additionally, this abstraction houses the
  communication infrastructure between the host and the Supervisor process, as
  well as between the host and its Worker processes.
  """

  def __init__(
      self,
      project_id: str,
      port: int,
      workers_per_host: int = 8,
      worker_timeout_s: int = 60,
      address: str | None = None,
      supervisor_config: supervisor_core.SupervisorConfig | None = None,
      enable_topology_aware_scheduling: bool = False,
      watchdogs: list[str] | None = None,
      watchdog_check_interval_s: int = 30,
  ):
    """Constructs a Host object.

    Args:
        project_id: The name of the GCP project.
        port: The port on which to run the host communication with supervisor.
        workers_per_host: The maximum number of workers per host. Default is 8.
        worker_timeout_s: The time before registering a host as spare capacity.
        address: The address for other processes to communicate with this host.
          In Kubernetes environments this refers to the FQDN.
        supervisor_config: The config object to set up communication with the
          supervisor. If not provided, will be loaded from
          SupervisorConfig.from_environment().
        enable_topology_aware_scheduling: Whether to enable topology aware
          scheduling. Requires compact placement policy to be set in the
          cluster.
        watchdogs: The list of watchdogs to enable in the host. Valid values are
          'ECC' and 'XID'.
        watchdog_check_interval_s: The time interval in seconds between watchdog
          checks.
    """
    if workers_per_host < 1:
      raise ValueError("workers_per_host must be a positive integer.")

    self._host_project_id = project_id
    host_name = utils.get_host_name()

    if enable_topology_aware_scheduling:
      superblock_id, subblock_id, host_serial_number = (
          utils.get_host_physical_attributes(
              project_id=project_id,
              zone=utils.get_host_zone(),
              host_name=host_name,
          )
      )
    else:
      superblock_id = ""
      subblock_id = ""
      host_serial_number = ""

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
      supervisor_config = supervisor_core.SupervisorConfig.from_environment()

    self._host = supervisor_core.Host(
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

    # Setup logging
    self.logger = core_utils.setup_logger()

    # Clean termination files
    utils.clean_termination_files()

    self._watchdogs: dict[str, base_watchdog.BaseWatchdog] = {}
    self._watchdog_check_interval = watchdog_check_interval_s

    if watchdogs is not None:
      for watchdog in watchdogs:
        if watchdog == "ecc":
          self._watchdogs["ecc"] = ecc_watchdog.ECCWatchdog(
              sample_interval=watchdog_check_interval_s
          )
        elif watchdog == "xid":
          self._watchdogs["xid"] = xid_watchdog.XIDWatchdog(
              sample_interval=watchdog_check_interval_s
          )
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
  def num_workers(self) -> int:
    """The number of workers currently assigned to the host."""
    return self._host.num_workers()

  def report_event(self, event_reports: list[supervisor_core.EventReport]):
    """Report watchdog detected errors to the Supervisor."""
    event_reports_proto = supervisor_core.EventReports()
    event_reports_proto.event_reports = event_reports
    self._host.report_event(event_reports_proto)

  def shutdown(self):
    """Shuts down host."""
    self.logger.info(f"{self.host_name}: Shutting down Host.")
    self._host.shutdown()
    utils.create_termination_file()

  def await_completion(self):
    """Waits for all workers registered to host to finish their workloads."""

    self.logger.info(f"{self.host_name}: awaiting completion...")
    while not self._host.is_complete():
      # Update host information in Python
      self.update_info(self._pull_info_from_cc())

      if self.host_info.state != device_info.DeviceState.RUNNING:
        self.logger.info(
            f"{self.host_name}: Host is not running, skipping watchdog"
            " checks..."
        )

      elif self._watchdogs:
        self.logger.info(
            f"{self.host_name}: Checking for watchdogs for detected errors..."
        )
        error_reports = []
        for watchdog in self._watchdogs.values():
          error_reports.extend(watchdog.poll())

        if error_reports:
          self.report_event(error_reports)

      else:
        self.logger.info(f"{self.host_name}: No watchdogs enabled...")

      time.sleep(self._watchdog_check_interval)

  def export_info(self) -> supervisor_core.HostInfo:
    """Exports Host object into supervisor_core HostInfo object."""
    return self.host_info.export_info()

  def update_info(self, host_info: supervisor_core.HostInfo):
    """Update the metadata associated with the worker."""
    self.host_info.update_info(host_info)

  def start_heartbeat(self):
    """Initializes heartbeating after all expected workers are online."""
    self._host.start_heartbeat()

  def _pull_info_from_cc(self) -> supervisor_core.HostInfo:
    """Pull the latest host information from C++ process."""
    return self._host.export_info()
