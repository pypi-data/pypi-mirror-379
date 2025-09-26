"""Intercepts for user workload code including google resiliency client."""

import functools
import socket
import time
from typing import Any, Callable, Mapping, Sequence

from supervisor.src.client.python import utils
from supervisor.src.core.python import device_info
from supervisor.src.core.python import utils as core_utils
import supervisor_core
import torch.multiprocessing as mp


class _WorkloadSignals:
  """Wrapper class for workload level intercepts for elastic training."""

  def __init__(self, timeout: int = 300):
    """Intialize the WorkloadIntercepts object.

    Args:
        timeout: the time elapsed between heartbeats before declaring a hang.
    """
    self._completion_event = mp.Event()
    self._heartbeat_counter = mp.Value("i", 0)
    self._timeout = timeout
    self._heartbeat_timestamp = mp.Value("f", 0.0)

    self.logger = core_utils.setup_logger()

  def heartbeat(self):
    """Registers new heartbeat from the user workload.

    Used to determine whether the user code is making progress, or
    if it is hanging.
    """
    self.logger.info(
        f"Registering heartbeat for step {self._heartbeat_counter.value}."
    )
    with self._heartbeat_counter.get_lock():
      self._heartbeat_counter.value += 1

    with self._heartbeat_timestamp.get_lock():
      self._heartbeat_timestamp.value = time.monotonic()

  def check_heartbeat(self) -> bool:
    """Checks whether the last registed hang is within the timeout period."""
    if self._heartbeat_counter.value == 0:
      self.logger.info("Initial heartbeat not yet registered.")
      return True

    return (time.monotonic() - self._heartbeat_timestamp.value) < self._timeout

  def get_current_training_step(self) -> int:
    """Returns the last training step for which a heartbeat was registered."""
    return self._heartbeat_counter.value

  def set_complete(self):
    """Signals that the workload has completed execution."""
    self.logger.info("Registering completion signal.")
    self._completion_event.set()

  def is_complete(self) -> bool:
    """Checks whether the completion signal has been registered."""
    return self._completion_event.is_set()


class WorkloadWrapper:
  """Callable class to wrap the workload function for elastic training."""

  def __init__(self, workload: Callable, signals: _WorkloadSignals):
    """Initialize the WorkloadWrapper.

    Args:
        workload: The workload function to wrap.
        intercepts: The WorkloadIntercepts object housing user workload
          intercepts.
    """
    self._workload = workload
    self._signals = signals
    functools.update_wrapper(self, workload)

    self.logger = core_utils.setup_logger()

  def __call__(self, *args: Sequence[Any], **kwargs: Mapping[str, Any]):
    """Call the wrapped workload function."""
    self.logger.info("Wrapping workload with elastic workload decorator.")
    try:
      self.logger.info("Starting elastic workload.")
      self._workload(self._signals, *args, **kwargs)
      self._signals.set_complete()
    except Exception as e:
      self.logger.error(f"Error during workload execution: {e}")
    finally:
      return


class GoogleResiliencyClient:
  """Abstraction of Worker processes including communication thread with Host.

  Stores all metadata related to a worker process, including physical worker
  attributes and worker rank. Additionally, this abstraction houses the
  communication infrastructure between the worker and the Host process.
  """

  def __init__(
      self,
      port: int,
      host_port: str,
      local_rank: int,
      global_rank: int,
  ):
    """Constructs a GoogleResiliencyClient object.

    Args:
        port: The port on which to run workload communication.
        host_port: The port running the host process.
        local_rank: The local rank of the worker processes.
        global_rank: The global rank of the worker processes.
    """
    host_address = "localhost:" + str(host_port)
    pci_bus_id = utils.get_pci_bus_id(local_rank)

    # Collect metadata related to worker
    self._worker_info = device_info.WorkerInfo(
        worker_address="localhost:" + str(port),
        worker_name=f"{socket.gethostname()}-{pci_bus_id}",
        worker_id=pci_bus_id,
        local_rank=local_rank,
        global_rank=global_rank,
    )

    # Initialize Worker gRPC server
    self._worker = supervisor_core.Worker(
        worker_info=self.export_info(),
        host_address=host_address,
    )

    self.logger = core_utils.setup_logger()
    self.logger.info(
        f"Initializing GoogleResiliencyClient for worker {self.worker_name}"
    )

  @property
  def worker_info(self) -> device_info.WorkerInfo:
    """The information of the worker process."""
    return self._worker_info

  @property
  def worker_name(self) -> int:
    """The name of the worker process."""
    return self.worker_info.worker_name

  @property
  def worker_id(self) -> str:
    """The PCI Bus ID of the GPU associated with the worker."""
    return self.worker_info.worker_id

  @property
  def local_rank(self) -> int:
    """The local rank of the worker process."""
    return self.worker_info.local_rank

  @local_rank.setter
  def local_rank(self, value: int):
    """Set the local rank of the worker process.

    Args:
        value: The new local rank of the worker.
    """
    self.worker_info.local_rank = value

  @property
  def global_rank(self) -> int:
    """The global rank of the worker process."""
    return self.worker_info.global_rank

  @global_rank.setter
  def global_rank(self, value: int):
    """Set the global rank of the worker process.

    Args:
        value: The new global rank of the worker.
    """
    self.worker_info.global_rank = value

  @property
  def state(self) -> device_info.DeviceState:
    """The current state of the worker."""
    return self.worker_info.state

  @state.setter
  def state(self, value: device_info.DeviceState):
    """Set the current state of the worker.

    Args:
        value: The new state of the worker.

    Raises:
        ValueError: If the value is not a valid state.
    """

    if value not in (
        device_info.DeviceState.RUNNING,
        device_info.DeviceState.FAILED,
        device_info.DeviceState.COMPLETE,
    ):
      raise ValueError(f"Invalid state: {value}")

    self.worker_info.state = value

  def export_info(self) -> supervisor_core.WorkerInfo:
    """Export Worker object into supervisor_core WorkerInfo object."""
    return self.worker_info.export_info()

  def update_info(self, worker_info: supervisor_core.WorkerInfo):
    """Update the metadata associated with the worker."""
    self.worker_info.update_info(worker_info)

  def send_heartbeat(self):
    """Communicate Worker state to the Host."""
    self._worker.send_heartbeat(self.export_info())
