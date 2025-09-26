"""Definition of GPU Reset elastic strategy class."""

import copy
import logging

from adaptr.src.core.python.mesh import Mesh
from adaptr.src.core.python.device_info import HostInfo
from adaptr.src.core.python.utils import get_torch_master_address
from adaptr.src.supervisor.python.elastic_strategies.base_strategy import (
    BaseStrategy,
    ScaleDirection,
)
import adaptr_core


class HotSwapStrategy(BaseStrategy):
    """HotSwapStrategy is an elastic strategy that removes a node upon failure or slowdown.

    HotSwapStrategy is currently only supported on GKE and requires spare capacity to exist
    either in the form of unused nodes in the cluster or nodes running lower priority workloads.
    """

    def __init__(self, mesh: Mesh):
        """Initializes the HotSwapStrategy instance.

        Args:
            mesh (Mesh): Mesh object
        """
        super().__init__(mesh, "hot_swap_strategy")

        self.mesh = mesh
        self.preempted_nodes = []

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

        if self.mesh.get_num_physical_hosts() <= self.mesh.running_host_count:
            return False

        return True

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
            ValueError: If the incorrect scale direction is provided.
        """

        generated_mesh = copy.deepcopy(self.adaptr_mesh)

        if scale_direction == ScaleDirection.DOWN:
            if self.preempted:
                raise ValueError(
                    "Scale direction must be 'DOWN' in the first call of generate_mesh."
                )

            logging.info(f"{self.name} generating temporary mesh.")
            self.preempted = True
            self.preempted_nodes = target_hosts

            for host_info in target_hosts:
                generated_mesh.update_virtual_host_info(
                    host_id=host_info.host_id, new_state=host_info.state
                )

                for worker in host_info.workers:
                    generated_mesh.update_virtual_worker_info(
                        worker_id=worker.worker_id, new_state=worker.state
                    )

        if scale_direction == ScaleDirection.UP:
            if not self.preempted:
                raise ValueError(
                    "Scale direction must be 'UP' in the second call of generate_mesh."
                )

            logging.info(f"{self.name} generating final mesh.")
            self.preempted = False

            for old_host_info, new_host_info in zip(target_hosts, self.preempted_nodes):
                generated_mesh.replace_physical_host_info(old_host_info, new_host_info)

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
        if scale_direction == ScaleDirection.DOWN:
            if self.preempted:
                raise ValueError(
                    "Scale direction must be 'DOWN' in the first call of generate_mesh."
                )

            logging.info(f"{self.name} generating first command set.")

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

            # Second command set taints bad node
            command_set = adaptr_core.CommandSet()
            command_set_list = []

            for host_info in self.preempted_nodes:
                command = adaptr_core.Command()
                command.host_info = host_info.export_info()
                command.callback_names = ["quarantine_host"]
                command.callback_kwargs = [f"host_name={host_info.host_name}"]

                command_set_list.append(command)

            command_set.set = command_set_list
            command_set.command_type = adaptr_core.CommandType.SUPERVISOR
            command_sets_list.append(command_set)

            self.preempted = False
            self.preempted_nodes = []

        if scale_direction == ScaleDirection.UP:
            command_sets = adaptr_core.CommandSets()
            command_sets_list = []

            # Command set resumes training
            command_set = adaptr_core.CommandSet()
            command_set_list = []
            for host_info in updated_mesh.get_all_hosts():
                command = adaptr_core.Command()

                command.host_info = host_info.export_info()
                command.callback_names = ["start"]
                command.callback_kwargs = [
                    f"master_addr={get_torch_master_address(updated_mesh)},new_world_size={updated_mesh.get_running_workers_count()}"
                ]

                command_set_list.append(command)

            command_set.set = command_set_list
            command_set.command_type = adaptr_core.CommandType.HOST
            command_sets_list.append(command_set)

            command_sets = adaptr_core.CommandSets()
            command_sets.sets = command_sets_list

        return command_sets
