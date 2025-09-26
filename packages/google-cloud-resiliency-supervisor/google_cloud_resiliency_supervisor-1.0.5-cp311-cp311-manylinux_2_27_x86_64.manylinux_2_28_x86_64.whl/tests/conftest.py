import os
import pytest
import socket

import adaptr_core
from adaptr.src.client.python import host
from adaptr.src.core.python import mesh, device_info
from tests.constants import ACTUATOR_PORT, CONTROLLER_PORT, SENSOR_PORT
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
    os.environ["HEARTBEAT_SIGNAL_PERIOD_S"] = "3"
    os.environ["HEARTBEAT_TIMEOUT_PERIOD_S"] = "5"

    config = adaptr_core.SupervisorConfig.from_environment()

    yield config

    for var_name in [
        "SENSOR_ADDRESS",
        "ACTUATOR_ADDRESS",
        "CONTROLLER_ADDRESS",
        "HEARTBEAT_POLLING_PERIOD_S",
        "HEARTBEAT_SIGNAL_PERIOD_S",
        "HEARTBEAT_TIMEOUT_PERIOD_S",
    ]:
        del os.environ[var_name]


@pytest.fixture(scope="module")
def actuator(config):
    actuator_instance = adaptr_core.Actuator(
        port=CONFTEST_ACTUATOR_PORT, num_grpc_threads=4, config=config
    )
    actuator_instance.start()
    while not actuator_instance.is_ready():
        continue
    yield actuator_instance
    actuator_instance.shutdown()


@pytest.fixture(scope="module")
def sensor(config):
    sensor_instance = adaptr_core.Sensor(
        port=CONFTEST_SENSOR_PORT,
        num_grpc_threads=4,
        config=config,
    )
    sensor_instance.start()
    while not sensor_instance.is_ready():
        continue
    yield sensor_instance
    sensor_instance.shutdown()


@pytest.fixture
def host_instance(actuator, sensor, config):
    host_instance = host.Host(
        project_id="test_project",
        port=find_available_port(),
        redis_port=find_available_port(),
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


@pytest.fixture()
def mesh_init(create_host_info, create_worker_info):
    def _mesh_init(dimensions: dict, virtual_mapping: bool = True):
        """Initializes a mesh."""
        tp_size = dimensions.get("tp", 1)
        pp_size = dimensions.get("pp", 1)
        dp_size = dimensions.get("dp", 1)

        world_size = dp_size * tp_size * pp_size
        adaptr_mesh = mesh.Mesh(dimensions)

        assert adaptr_mesh.get_num_dimensions() == len(dimensions)

        assert world_size % 8 == 0

        # This mimics HostInfo and WorkerInfo creation
        # that occurs on each host and is sent to the Supervisor.
        all_hosts = {}
        all_workers = {}

        # Iterate over each "host"
        for host_rank in range(world_size // 8):
            host_id = f"host_id_{host_rank}"

            # generate new host with populated workers
            host = create_host_info(host_rank=host_rank)

            for worker_rank in range(8):
                worker = create_worker_info(global_rank=worker_rank + (host_rank * 8))
                host.workers.append(worker)
                worker.host = host
                # add worker to mesh
                all_workers[worker.worker_id] = worker
            all_hosts[host_id] = host

            # add host to mesh
            adaptr_mesh.add_physical_host_info(host)

            # Check that all hosts and workers were added
            assert adaptr_mesh.get_host(host_id) == host
            for worker in host.workers:
                assert adaptr_mesh.get_worker(worker.worker_id) == worker

        # Check correctness of physical mapping
        assert adaptr_mesh.physical_worker_map == all_workers
        assert adaptr_mesh.physical_host_map == all_hosts

        # Check that mesh is not ready to use since virtual map is yet to be defined
        assert not adaptr_mesh.ready_to_use()

        # Add virtual mapping if enabled
        if virtual_mapping:
            num_tp_groups = world_size // tp_size
            num_pp_groups = world_size // pp_size

            all_parallel_groups = {}
            for key in dimensions.keys():
                all_parallel_groups[key] = []

            # Define data parallel groups
            if "dp" in dimensions:
                for i in range(pp_size):
                    start_rank = i * num_pp_groups
                    end_rank = (i + 1) * num_pp_groups
                    for j in range(tp_size):
                        group = list(range(start_rank + j, end_rank, tp_size))
                        all_parallel_groups["dp"].append(group)

            # Define tensor parallel groups
            if "tp" in dimensions:
                for i in range(num_tp_groups):
                    group = list(range(i * tp_size, (i + 1) * tp_size))
                    all_parallel_groups["tp"].append(group)

            # Check that mesh is not ready to use since not all parallel groups are ingested
            assert not adaptr_mesh.ready_to_use()

            # Define pipeline model parallel groups
            if "pp" in dimensions:
                for i in range(num_pp_groups):
                    group = list(range(i, world_size, num_pp_groups))
                    all_parallel_groups["pp"].append(group)

            # Add parallel groups to mesh
            for key in dimensions.keys():
                adaptr_mesh.ingest_all_groups_in_dim(key, all_parallel_groups[key])

            for worker in adaptr_mesh.get_all_workers():
                # Check correctness of rank to worker mapping
                assert adaptr_mesh.get_worker_from_rank(worker.global_rank) == worker
                # Check correctness of coords to worker mapping
                assert adaptr_mesh.get_worker_from_coords(worker.coords) == worker

            adaptr_mesh.set_all_parallel_groups(all_parallel_groups)

            # Check that mesh is ready to use
            assert adaptr_mesh.ready_to_use()

        return adaptr_mesh

    return _mesh_init
