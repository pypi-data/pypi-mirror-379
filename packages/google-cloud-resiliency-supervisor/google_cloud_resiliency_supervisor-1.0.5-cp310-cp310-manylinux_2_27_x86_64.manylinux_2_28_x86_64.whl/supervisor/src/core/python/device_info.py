"""Python classes to define Host and Worker Info objects."""

import enum
import supervisor_core


@enum.unique
class DeviceState(enum.Enum):
  """The state of a physical device.

  Worker and Host objects can have six possible
  states. RUNNING denotes that the device is healthy and
  participating in training. SPARE denotes that the worker is healthy
  but not currently participating in training. FAILED
  denotes that the worker is currently unreachable. COMPLETE denotes that the
  worker has completed its training workload.
  """

  RUNNING = 0
  SPARE = 1
  FAILED = 2
  COMPLETE = 3


class HostInfo:
  """Representation of physical and virtual identifiers for a host machine."""

  def __init__(
      self,
      host_address: str,
      host_id: str,
      host_serial_number: str,
      subblock_id: str,
      superblock_id: str,
      zone: str,
      host_name: str,
      state: DeviceState = DeviceState.SPARE,
  ):
    """HostInfo constructor.

    Args:
        host_address (str): The network address of the host.
        host_id (str): The serial number of the host machine.
        host_serial_number (str): The host's serial number.
        subblock_id (str): The host's supblock. Defaults to None.
        superblock_id (str): The host's superblock. Defaults to None.
        zone (str): The host's zone. Defaults to None.
        host_name (str): Name of host's corresponding python process.
        state (DeviceState, optional): The state of the host. Defaults to
          DeviceState.SPARE.
    """
    # Physical Identifiers
    self._host_address = host_address
    self._host_id = host_id
    self._host_serial_number = host_serial_number
    self._subblock_id = subblock_id
    self._superblock_id = superblock_id
    self._zone = zone
    self._state = state

    # Virtual Identifiers
    self._host_name = host_name

    self._workers = []

  def __repr__(self):
    return f"{self._host_id}"

  @property
  def host_address(self) -> str:
    return self._host_address

  @property
  def host_id(self) -> str:
    return self._host_id

  @property
  def host_serial_number(self) -> str:
    return self._host_serial_number

  @property
  def subblock_id(self) -> str:
    return self._subblock_id

  @property
  def superblock_id(self) -> str:
    return self._superblock_id

  @property
  def zone(self) -> str:
    return self._zone

  @property
  def state(self) -> DeviceState:
    return self._state

  @state.setter
  def state(self, state: DeviceState):
    self._state = state

  @property
  def workers(self) -> list["WorkerInfo"]:
    return self._workers

  @workers.setter
  def workers(self, workers: list["WorkerInfo"]):
    self._workers = workers

  @property
  def host_name(self) -> str:
    return self._host_name

  def export_info(self) -> supervisor_core.HostInfo:
    h_info = supervisor_core.HostInfo()
    h_info.host_address = self.host_address
    h_info.host_id = self.host_id
    h_info.host_name = self.host_name
    h_info.subblock_id = self.subblock_id
    h_info.superblock_id = self.superblock_id
    h_info.host_serial_number = self.host_serial_number
    h_info.zone = self.zone
    h_info.state = supervisor_core.DeviceState(self.state.value)
    h_info.workers = [worker.export_info() for worker in self.workers]
    return h_info

  def update_info(self, host_info_proto: supervisor_core.HostInfo):
    self.state = DeviceState(host_info_proto.state.value)
    self.workers.clear()
    for worker_info_proto in host_info_proto.workers:
      self.workers.append(worker_info_from_proto(worker_info_proto))

  def get_num_workers(self) -> int:
    return len([
        worker
        for worker in self._workers
        if worker.state == DeviceState.RUNNING
    ])


class WorkerInfo:
  """Representation of physical and virtual identifiers for a GPU Worker."""

  def __init__(
      self,
      worker_address: str,
      worker_id: str,
      local_rank: int | None = None,
      global_rank: int | None = None,
      worker_name: str | None = None,
      state: DeviceState = DeviceState.RUNNING,
  ):
    """WorkerInfo constructor.

    Args:
        worker_id (str): The serial number of the GPU associated with the
          worker.
        local_rank (int | None, optional): The worker's rank respective to the
          host.
        global_rank (int | None, optional): The worker's rank respective to the
          entire workload.
        worker_name (str | None, optional): Name of worker's corresponding
          python process. Defaults to None.
        normalized_perf (int, optional): The worker's relative performance as a
          percentage in [0, 100]. Defaults to 100.
        state (DeviceState, optional): The state of the worker. Defaults to
          DeviceState.AVAILABLE.
    """
    # Physical Identifiers
    self._worker_address = worker_address
    self._host = None
    self._worker_id = worker_id
    self._state = state

    # Virtual Identifiers
    self._local_rank = local_rank
    self._global_rank = global_rank
    self._coords = None
    self._worker_name = worker_name

  def __repr__(self):
    return f"{self._worker_id}"

  @property
  def host(self) -> HostInfo:
    return self._host

  @host.setter
  def host(self, host: HostInfo):
    self._host = host

  @property
  def worker_address(self) -> str:
    return self._worker_address

  @worker_address.setter
  def worker_address(self, address: str):
    self._worker_address = address

  @property
  def worker_id(self) -> str:
    return self._worker_id

  @property
  def state(self) -> DeviceState:
    return self._state

  @state.setter
  def state(self, state: DeviceState):
    self._state = state

  @property
  def local_rank(self) -> int:
    return self._local_rank

  @local_rank.setter
  def local_rank(self, rank: int):
    self._local_rank = rank

  @property
  def global_rank(self) -> int:
    return self._global_rank

  @global_rank.setter
  def global_rank(self, rank: int):
    self._global_rank = rank

  @property
  def coords(self) -> tuple[int, ...]:
    return self._coords

  @coords.setter
  def coords(self, coords: tuple[int, ...]):
    self._coords = coords

  @property
  def worker_name(self) -> str:
    if self._worker_name is None:
      self._worker_name = f"worker_{self.worker_id}"
    return self._worker_name

  def export_info(self) -> supervisor_core.WorkerInfo:
    w_info = supervisor_core.WorkerInfo()
    w_info.worker_address = self.worker_address
    w_info.worker_id = self.worker_id
    w_info.worker_name = self.worker_name
    w_info.local_rank = -1 if self.local_rank is None else self.local_rank
    w_info.global_rank = -1 if self.global_rank is None else self.global_rank
    w_info.state = supervisor_core.DeviceState(self.state.value)
    return w_info

  def update_info(self, worker_info_proto: supervisor_core.WorkerInfo):
    self.local_rank = worker_info_proto.local_rank
    self.global_rank = worker_info_proto.global_rank
    self.state = DeviceState(worker_info_proto.state.value)


def host_info_from_proto(host_info_proto: supervisor_core.HostInfo) -> HostInfo:
  """Converts an instance of supervisor_core.HostInfo into a device_info.HostInfo instance."""
  host_info = HostInfo(
      host_address=host_info_proto.host_address,
      host_id=host_info_proto.host_id,
      host_serial_number=host_info_proto.host_serial_number,
      host_name=host_info_proto.host_name,
      subblock_id=host_info_proto.subblock_id,
      superblock_id=host_info_proto.superblock_id,
      zone=host_info_proto.zone,
      state=DeviceState(host_info_proto.state),
  )
  workers = [
      worker_info_from_proto(worker_info_proto)
      for worker_info_proto in host_info_proto.workers
  ]
  for worker in workers:
    worker.host = host_info
  host_info.workers = workers
  return host_info


def worker_info_from_proto(
    worker_info_proto: supervisor_core.WorkerInfo,
) -> WorkerInfo:
  """Converts an instance of supervisor_core.WorkerInfo into a device_info.WorkerInfo instance."""
  worker_info = WorkerInfo(
      worker_address=worker_info_proto.worker_address,
      worker_id=worker_info_proto.worker_id,
      local_rank=worker_info_proto.local_rank,
      global_rank=worker_info_proto.global_rank,
      worker_name=worker_info_proto.worker_name,
      state=DeviceState(worker_info_proto.state),
  )
  return worker_info
