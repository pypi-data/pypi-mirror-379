"""Python interface for the Controller Process of the Supervisor."""

import collections
import time

from supervisor.src.client.python.orchestrators import gke_callbacks
from supervisor.src.core.python import utils
import supervisor_core


class BaseController:
  """Base Abstraction of controller processes of the Supervisor.

  Subclasses can implement the event_policy method to handle events
  reported by the Controller process in a custom way.

  Controller provides a series of primitive to trigger different types of
  orchestrator level commands. These include:
  - trigger_nvrx_reset: Triggers a reset for all hosts currently tracked by the
  controller.
  - trigger_job_reset: Triggers a job reset for the specified host.
  - trigger_hot_swap: Triggers a hot-swap for the specified host.
  - trigger_jobset_reset: Triggers a jobset reset for the specified host.
  - trigger_jobset_scale_down: Triggers a data parallel scale down for the
  jobset running on the specified host.
  - trigger_jobset_scale_up: Triggers a data parallel scale up for the jobset
  running on the specified host.

  Stores all metadata related to the Controller process and provides an
  interface to
  interact with the Controller process. The Controller process is responsible
  for
  computing new cluster states given events reported by the Controller.
  """

  def __init__(
      self,
      port: int,
      num_grpc_threads: int,
      supervisor_config: supervisor_core.SupervisorConfig | None = None,
      orchestrator: str = "GKE",
  ):
    """Constructs the Controller object.

    Args:
        port: The port on which to run the controller communication.
        num_grpc_threads: The number of gRPC threads to initialize for
          communication.
        supervisor_config: The config object for Supervisor components.
        event_handler: The policy to handle detected events.
        orchestrator: The orchestrator to use for the controller.
    """
    if not supervisor_config:
      supervisor_config = supervisor_core.SupervisorClient(
          supervisor_core.SupervisorConfig.from_environment()
      )

    self._controller = supervisor_core.Controller(
        port=port,
        num_grpc_threads=num_grpc_threads,
        config=supervisor_config,
        command_handle_fn=self._command_handler,
        update_handle_fn=self._update_handler,
        event_handle_fn=self._event_handler,
    )

    self._controller.start()
    while not self._controller.is_ready():
      continue

    self._controller_address = supervisor_config.controller_address
    self.logger = utils.setup_logger()
    self.logger.info(
        f"Successfully started controller process at address: {self.address}"
    )

    if orchestrator == "GKE":
      self._orchestrator = gke_callbacks.KubernetesCallbacks(supervisor_config)
      self._orchestrator_callbacks = {
          "get_workload_info": self._orchestrator.get_workload_info,
          "uncordon_host": self._orchestrator.uncordon_host,
          "delete_pod": self._orchestrator.delete_pod,
          "restart_jobset": self._orchestrator.restart_jobset,
          "reset_gpu": self._orchestrator.reset_gpu,
          "poll_jobset_status": self._orchestrator.poll_jobset_status,
          "drain_host": self._orchestrator.drain_host,
      }
    else:
      raise ValueError(f"Unsupported orchestrator type: {orchestrator}")

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

  def trigger_nvrx_reset(self):
    """Triggers a reset for all hosts currently tracked by the controller."""
    self._controller.trigger_nvrx_reset()

  def trigger_job_reset(self, host_info: supervisor_core.HostInfo):
    """Triggers a job reset for the specified host."""
    self._controller.trigger_job_reset(host_info)

  def trigger_hot_swap(self, host_info: supervisor_core.HostInfo):
    """Triggers a hot-swap for the specified host."""
    self._controller.trigger_hot_swap(host_info)

  def trigger_jobset_reset(self, host_info: supervisor_core.HostInfo):
    """Triggers a jobset reset for the specified host."""
    self._controller.trigger_jobset_reset(host_info)

  def trigger_jobset_scale_down(self, host_info: supervisor_core.HostInfo):
    """Triggers a jobset scale down for the specified host."""
    self._controller.trigger_jobset_scale_down(host_info)

  def trigger_jobset_scale_up(self, host_info: supervisor_core.HostInfo):
    """Triggers a jobset scale up for the specified host."""
    self._controller.trigger_jobset_scale_up(host_info)

  def shutdown(self):
    """Shuts down the controller process and child threads."""
    self._controller.shutdown()

  def wait_for_completion(self):
    """Waits for all hosts registered to controller to finish their workloads."""
    while not self._controller.is_complete():
      time.sleep(10)

  def event_policy(self, event_reports: supervisor_core.EventReports):
    """Default event policy for the Controller process."""
    event_report = event_reports.event_reports[0]
    event_type = event_report.event_type
    host_info = event_report.host_info

    self.logger.info(f"Received event report: {event_report.message}")

    if event_type == supervisor_core.EventType.WORKER_HB:
      # Only Reset Hosts in preparation for framework-level reset
      self.trigger_nvrx_reset()

    elif (
        event_type == supervisor_core.EventType.HOST_HB
        or event_type == supervisor_core.EventType.XID
        or event_type == supervisor_core.EventType.ECC
    ):

      self.failure_counter[host_info.host_name] += 1

      if self.num_spare_hosts > 0:
        # Attempt pod-level reset first, escalate to hot-swap if unsuccessful
        if self.failure_counter[host_info.host_name] <= 1:
          self.trigger_job_reset(host_info)
        else:
          self.trigger_hot_swap(host_info)
          self.failure_counter[host_info.host_name] = 0
      else:
        # Scale down the jobset if there are no spare hosts available
        self.trigger_jobset_scale_down(host_info)

    elif event_type == supervisor_core.EventType.SCALE_UP:
      self.trigger_jobset_scale_up(host_info)

  def _update_handler(self, state: supervisor_core.SupervisorState):
    """Handle update requests to synchronize C++ and Python Supervisor state.

    Args:
        state: The current supervisor state coming from the C++ controller.
    """
    if not isinstance(state, supervisor_core.SupervisorState):
      raise ValueError((
          f"Invalid callback argument type: {type(state)}. "
          "The callback argument must be of type SupervisorState."
      ))

  def _event_handler(self, event_reports: supervisor_core.EventReports):
    """Handle event reports from the C++ controller.

    Args:
        event_reports: The event reports recieved from the C++ controller.
    """
    if not isinstance(event_reports, supervisor_core.EventReports):
      raise ValueError((
          f"Invalid callback argument type: {type(event_reports)}. "
          "The callback argument must be of type EventReports."
      ))
    self.event_policy(event_reports)

  def _command_handler(self, command: supervisor_core.Command):
    """Handle orchestrator level command issued by C++ controller.

    Args:
        command: The command recieved from the C++ controller.
    """
    if not isinstance(command, supervisor_core.Command):
      raise ValueError((
          f"Invalid callback argument type: {type(command)}. "
          "The callback argument must be of type Command."
      ))
    for callback, kwargs in zip(
        command.callback_names, command.callback_kwargs
    ):
      kwargs = utils.destringify_kwargs(kwargs)
      if callback not in self._orchestrator_callbacks:
        raise ValueError(f"Unexpected callback {callback} recieved.")

      self._orchestrator_callbacks[callback](**kwargs)
