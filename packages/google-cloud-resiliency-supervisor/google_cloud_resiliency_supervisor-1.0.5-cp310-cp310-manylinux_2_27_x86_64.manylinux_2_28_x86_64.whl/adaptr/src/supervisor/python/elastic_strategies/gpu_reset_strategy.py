"""Definition of GPU Reset elastic strategy class."""

import copy
import logging

from adaptr.src.core.python.mesh import Mesh
from adaptr.src.core.python.device_info import HostInfo, DeviceState
from adaptr.src.core.python.utils import get_torch_master_address
from adaptr.src.supervisor.python.elastic_strategies.base_strategy import (
    BaseStrategy,
    ScaleDirection,
)
import adaptr_core


class GPUResetStrategy(BaseStrategy):
    """GPUResetStrategy is an elastic strategy that resets GPUs upon failure or slowdown.

    GPUResetStrategy is currently only supported on GKE.
    """

    def __init__(self, adaptr_mesh: Mesh, max_resets_per_gpu: int = 1):
        """Initializes the GPUResetStrategy instance.

        Args:
            adaptr_mesh (Mesh): Mesh object
            max_resets_per_gpu (int): Max number of resets permitted per GPU.
        """
        super().__init__(adaptr_mesh, "gpu_reset_strategy")

        self.adaptr_mesh = adaptr_mesh
        self._max_resets_per_gpu = max_resets_per_gpu
        self._initialized = False

    def deferred_init(self):
        """Initializes the counter used to keep track of recurring GPU failures."""
        if not self._initialized:
            self._worker_failures = {}
            for worker_info in self.adaptr_mesh.get_all_workers():
                self._worker_failures[worker_info.worker_id] = 0
            self._initialized = True

    def can_apply_strategy(
        self, scale_direction: ScaleDirection, target_hosts: list[HostInfo]
    ) -> bool:
        """Determines whether the strategy can be applied based on the given scale direction and target worker_infos.

        This strategy can be used to reset multiple failed GPUs simulataneously, but is only
        applicable if all of the failed GPUs have not exceeded max resets per GPU.

        Args:
            scale_direction (ScaleDirection): The direction in which the scaling is intended to happen.
            target_hosts (list[HostInfo]): List of hosts with new updates.

        Returns:
            bool: True if the strategy can be applied, False otherwise.
        """
        if scale_direction == ScaleDirection.UP:
            return False

        if len(target_hosts) == 0:
            return False

        if any([host.state == DeviceState.UNAVAILABLE for host in target_hosts]):
            return False

        worker_failure = True
        for host in target_hosts:
            for worker in host.workers.values():
                if worker.state in (DeviceState.UNAVAILABLE, DeviceState.SLOW):
                    failure_count = self._worker_failures[worker.worker_id]
                    worker_failure = failure_count < self._max_resets_per_gpu

        return worker_failure

    def generate_mesh(
        self, scale_direction: ScaleDirection, target_hosts: list[HostInfo]
    ) -> Mesh:
        """Generates a new mesh based on the given scale direction and target worker_infos.

        Args:
            scale_direction (ScaleDirection): The direction in which the mesh should be scaled.
            target_hosts (list[HostInfo]): List of hosts with new updates.

        Returns:
            Mesh: The generated mesh.

        Raises:
            ValueError: If the scale direction is UP.
            RuntimeError: If a GPU exceeds max_resets_per_gpu
        """
        if scale_direction == ScaleDirection.UP:
            raise ValueError("Scale direction must be 'DOWN' in GPU Reset.")

        logging.info(f"{self.name} generating new mesh.")

        self.deferred_init()
        generated_mesh = copy.deepcopy(self.adaptr_mesh)

        self._workers_to_reset = list()
        for host_info in target_hosts:
            for worker in host_info.workers.values():
                if (
                    worker.state == DeviceState.UNAVAILABLE
                    or worker.state == DeviceState.SLOW
                ):
                    if (
                        self._worker_failures[worker.worker_id]
                        < self._max_resets_per_gpu
                    ):
                        generated_mesh.update_virtual_worker_info(
                            worker_id=worker.worker_id, new_state=DeviceState.ACTIVE
                        )
                        self._workers_to_reset.append(worker.worker_id)
                    else:
                        raise RuntimeError(
                            f"{worker.worker_name}: too many repeated failures, cannot execute GPU reset."
                        )

                    self._worker_failures[worker.worker_id] += 1

        return generated_mesh

    def generate_commands(
        self, scale_direction: ScaleDirection, updated_mesh: Mesh
    ) -> adaptr_core.CommandSets:
        """
        Defines a set of commands based on scale direction and updated mesh to apply the strategy to the training workload.

        Args:
            scale_direction (ScaleDirection): The direction of scaling.
            updated_mesh (Mesh): The updated mesh resulting from `self.generate_mesh()`.

        Returns:
            adaptr_core.CommandSet: The commands to apply the strategy.

        Raises:
            ValueError: If the scale direction is UP.
        """
        if scale_direction == ScaleDirection.UP:
            raise ValueError("Scale direction must be 'DOWN' in GPU Reset.")

        logging.info(f"{self.name} generating commands.")

        command_sets = adaptr_core.CommandSets()
        command_sets_list = []

        # First command set pauses training
        command_set = adaptr_core.CommandSet()
        command_set_list = []
        for host_info in updated_mesh.get_all_hosts():
            command = adaptr_core.Command()

            command.host_info = host_info.export_info()
            command.callback_names = ["stop"]
            command.callback_kwargs = [""]

            command_set_list.append(command)

        command_set.set = command_set_list
        command_set.command_type = adaptr_core.CommandType.HOST
        command_sets_list.append(command_set)

        # Second command set resets GPUs
        command_set = adaptr_core.CommandSet()
        command_set_list = []

        for worker_id in self._workers_to_reset:
            worker = updated_mesh.get_worker(worker_id)
            host_info = worker.host

            command = adaptr_core.Command()
            command.host_info = host_info.export_info()
            command.callback_names = ["reset_gpu"]
            command.callback_kwargs = [
                f"host_name={host_info.host_name},gpu_local_rank={worker.local_rank}"
            ]

            command_set_list.append(command)

        command_set.set = command_set_list
        command_set.command_type = adaptr_core.CommandType.SUPERVISOR
        command_sets_list.append(command_set)

        # Last command set resumes training
        command_set = adaptr_core.CommandSet()
        command_set_list = []
        for host_info in updated_mesh.get_all_hosts():
            command = adaptr_core.Command()

            command.host_info = host_info.export_info()
            command.callback_names = ["start"]
            command.callback_kwargs = [
                f"master_addr={get_torch_master_address(updated_mesh)},new_world_size={updated_mesh.get_active_workers_count()}"
            ]

            command_set_list.append(command)

        command_set.set = command_set_list
        command_set.command_type = adaptr_core.CommandType.HOST
        command_sets_list.append(command_set)

        command_sets = adaptr_core.CommandSets()
        command_sets.sets = command_sets_list

        return command_sets
