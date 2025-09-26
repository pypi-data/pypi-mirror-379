import os
import socket

import pytest
from supervisor.src.client.python import actuator as actuator_module
from supervisor.src.client.python import controller as controller_module
from supervisor.src.client.python import host
from supervisor.src.client.python import sensor as sensor_module
from supervisor.src.core.python import device_info
import supervisor_core
from tests.constants import ACTUATOR_PORT
from tests.constants import CONTROLLER_PORT
from tests.constants import SENSOR_PORT
from tests.utils import find_available_port


CONFTEST_ACTUATOR_PORT = ACTUATOR_PORT
CONFTEST_SENSOR_PORT = SENSOR_PORT
CONFTEST_CONTROLLER_PORT = CONTROLLER_PORT


@pytest.fixture(scope="module")
def config():
  os.environ["SENSOR_ADDRESS"] = (
      f"{socket.gethostbyname(socket.gethostname())}:{CONFTEST_SENSOR_PORT}"
  )
  os.environ["ACTUATOR_ADDRESS"] = (
      f"{socket.gethostbyname(socket.gethostname())}:{CONFTEST_ACTUATOR_PORT}"
  )
  os.environ["CONTROLLER_ADDRESS"] = (
      f"{socket.gethostbyname(socket.gethostname())}:{CONFTEST_CONTROLLER_PORT}"
  )
  os.environ["HEARTBEAT_POLLING_PERIOD_S"] = "2"
  os.environ["HEARTBEAT_TIMEOUT_S"] = "5"
  os.environ["JOB_NAMESPACE"] = "default"
  os.environ["REPLICATED_JOB_NAME"] = "test_job"
  os.environ["WORKLOAD_CONTAINER_NAME"] = "test_container"
  os.environ["NUM_DP_REPLICAS"] = "1"
  os.environ["NUM_NODES_PER_DP"] = "1"
  os.environ["POD_TERMINATION_THRESHOLD_S"] = "5"
  os.environ["JOBSET_DOWNTIME_THRESHOLD_S"] = "10"

  config = supervisor_core.SupervisorConfig.from_environment()  # pylint: disable=redefined-outer-name

  yield config

  for var_name in [
      "SENSOR_ADDRESS",
      "ACTUATOR_ADDRESS",
      "CONTROLLER_ADDRESS",
      "HEARTBEAT_POLLING_PERIOD_S",
      "HEARTBEAT_TIMEOUT_S",
      "JOB_NAMESPACE",
      "REPLICATED_JOB_NAME",
      "WORKLOAD_CONTAINER_NAME",
      "NUM_DP_REPLICAS",
      "NUM_NODES_PER_DP",
      "POD_TERMINATION_THRESHOLD_S",
      "JOBSET_DOWNTIME_THRESHOLD_S",
  ]:
    del os.environ[var_name]


@pytest.fixture(scope="module")
def actuator(config):  # pylint: disable=redefined-outer-name
  actuator_instance = actuator_module.Actuator(
      port=CONFTEST_ACTUATOR_PORT, num_grpc_threads=4, supervisor_config=config
  )

  yield actuator_instance

  actuator_instance.shutdown()


@pytest.fixture(scope="module")
def controller(config):  # pylint: disable=redefined-outer-name
  controller_instance = controller_module.BaseController(
      port=CONFTEST_CONTROLLER_PORT,
      num_grpc_threads=4,
      supervisor_config=config,
  )

  yield controller_instance

  controller_instance.shutdown()


@pytest.fixture(scope="module")
def sensor(config):  # pylint: disable=redefined-outer-name
  sensor_instance = sensor_module.Sensor(
      port=CONFTEST_SENSOR_PORT,
      num_grpc_threads=4,
      supervisor_config=config,
  )

  yield sensor_instance

  sensor_instance.shutdown()


@pytest.fixture
def host_instance(actuator, sensor, config):  # pylint: disable=redefined-outer-name, unused-argument
  # pylint: disable=redefined-outer-name
  host_instance = host.Host(
      project_id="test_project",
      port=find_available_port(),
      supervisor_config=config,
  )
  yield host_instance
  host_instance.shutdown()


@pytest.fixture()
def create_worker_info():
  def _create_worker_info(
      global_rank: int = 0,
  ):
    """Function for creating a WorkerInfo object."""
    return device_info.WorkerInfo(
        worker_address=f"localhost:{find_available_port()}",
        worker_id=f"worker_id_{global_rank}",
        local_rank=global_rank,
        global_rank=global_rank,
    )

  return _create_worker_info


@pytest.fixture()
def create_host_info():
  def _create_host_info(
      host_rank: int = 0,
  ):
    """Function for creating a HostInfo object."""
    # pylint: disable=redefined-outer-name
    host = device_info.HostInfo(
        host_name=f"host_{host_rank}",
        host_address=f"localhost:{54321+host_rank}",
        host_id=f"host_id_{host_rank}",
        host_serial_number=f"host_serial_number_{host_rank}",
        subblock_id=f"subblock_id_{host_rank}",
        superblock_id=f"superblock_id_{host_rank}",
        zone=f"zone_{host_rank}",
    )
    return host

  return _create_host_info
