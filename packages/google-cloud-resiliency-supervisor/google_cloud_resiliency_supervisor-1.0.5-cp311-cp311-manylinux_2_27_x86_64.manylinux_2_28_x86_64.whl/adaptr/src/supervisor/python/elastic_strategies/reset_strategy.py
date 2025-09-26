"""Definition of reset elastic strategy class."""

import copy
from adaptr.src.core.python.mesh import Mesh
from adaptr.src.core.python.device_info import HostInfo, DeviceState
from adaptr.src.core.python.utils import get_torch_master_address
from adaptr.src.supervisor.python.elastic_strategies.base_strategy import (
    BaseStrategy,
    ScaleDirection,
)
import adaptr_core


class ResetStrategy(BaseStrategy):
    """Elastic Strategy for Reset.

    This strategy resets the training subprocess without changing the training scale.
    ResetStrategy is intended to use as a first line of defense for software issues.
    """

    def __init__(self, mesh: Mesh, max_resets: int = 3):
        """Initializes the ResetStrategy instance.

        Args:
            mesh (Mesh): Mesh object
        """
        super().__init__(mesh, "reset_strategy")
        self.mesh = mesh
        self.max_resets = max_resets
        self.reset_count = 0

    def reset_counter(self) -> None:
        """Resets internal reset counter."""
        self.reset_count = 0

    def update_mesh(self, new_adaptr_mesh) -> None:
        """Updates the stored mesh with a new mesh.
        This is applicable when another elastic strategy is applied,
        where this strategy still needs to keep its mesh up-to-date.

        Args:
            new_adaptr_mesh: The new adaptr mesh to update with.
        """
        self.adaptr_mesh = new_adaptr_mesh

    def can_apply_strategy(
        self, scale_direction: ScaleDirection, target_hosts: list[HostInfo]
    ) -> bool:
        """Determines whether the strategy can be applied based on the given scale direction and target worker_infos.

        Args:
            scale_direction (ScaleDirection): The direction in which the scaling is intended to happen.
            target_hosts (list[HostInfo]): List of hosts with new updates.

        Returns:
            bool: True if the strategy can be applied, False otherwise.
        """
        if scale_direction == ScaleDirection.UP:
            return False

        if self.reset_count >= self.max_resets:
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
        """

        if scale_direction == ScaleDirection.UP:
            raise ValueError("Scale direction must be 'DOWN' in Reset.")

        generated_mesh = copy.deepcopy(self.mesh)

        for host_info in target_hosts:
            generated_mesh.update_virtual_host_info(
                host_id=host_info.host_id, new_state=DeviceState.RUNNING
            )
            for worker in host_info.workers:
                generated_mesh.update_virtual_worker_info(
                    worker_id=worker.worker_id, new_state=DeviceState.RUNNING
                )

        self.reset_count += 1

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
        """
        if scale_direction == ScaleDirection.UP:
            raise ValueError("Scale direction must be 'DOWN' in Reset.")

        # Define host commands
        command_set = adaptr_core.CommandSet()
        command_set_list = []
        for host_info in updated_mesh.get_all_hosts():
            # Define host command
            command = adaptr_core.Command()

            # Add host info to host command
            command.host_info = host_info.export_info()

            if host_info.state == DeviceState.RUNNING:
                command.callback_names = ["stop", "start"]
                command.callback_kwargs = [
                    "",
                    f"master_addr={get_torch_master_address(updated_mesh)},new_world_size={updated_mesh.get_running_workers_count()}",
                ]
            else:
                command.callback_names = ["stop"]
                command.callback_kwargs = [""]

            # Add host command to host commands list
            command_set_list.append(command)

        # Add host commands to host commands object
        command_set.set = command_set_list
        command_set.command_type = adaptr_core.CommandType.HOST

        command_sets = adaptr_core.CommandSets()
        command_sets.sets = [command_set]

        return command_sets
