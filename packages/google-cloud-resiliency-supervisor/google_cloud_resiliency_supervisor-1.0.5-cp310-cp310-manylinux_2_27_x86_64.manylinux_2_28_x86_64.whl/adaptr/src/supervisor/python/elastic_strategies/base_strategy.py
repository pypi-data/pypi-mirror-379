"""Abstract definition of elastic strategy class."""

import abc
import enum
from adaptr.src.core.python.mesh import Mesh
from adaptr.src.core.python.device_info import HostInfo
import adaptr_core
import copy
import logging


class ScaleDirection(enum.Enum):
    DOWN = enum.auto()
    UP = enum.auto()


class BaseStrategy(abc.ABC):
    """Elastic Strategy base class. All elastic strategies must inherit from this class."""

    def __init__(self, adaptr_mesh: Mesh, name: str):
        self.adaptr_mesh = adaptr_mesh
        self.name = name
        logging.info(f"Initializing strategy {self.name}.")

    def deferred_init(self) -> None:
        """Initialization that does not happen immediately.
        Some strategies may need this, for examples those that need a complete mesh to be initialized first.
        """
        pass

    def update_mesh(self, new_adaptr_mesh) -> None:
        """Updates the stored mesh with a new mesh.
        This is applicable when another elastic strategy is applied,
        where this strategy still needs to keep its mesh up-to-date.

        Args:
            new_adaptr_mesh: The new adaptr mesh to update with.
        """
        self.adaptr_mesh = copy.deepcopy(new_adaptr_mesh)

    @abc.abstractmethod
    def can_apply_strategy(
        self, scale_direction: ScaleDirection, target_hosts: list[HostInfo]
    ) -> bool:
        """Determines whether the strategy can be applied based on the given scale direction and target hosts.

        Args:
            scale_direction (ScaleDirection): The direction in which the scaling is intended to happen.
            target_hosts (list[HostInfo]): List of hosts with new updates.

        Returns:
            bool: True if the strategy can be applied, False otherwise.
        """
        pass

    @abc.abstractmethod
    def generate_mesh(
        self, scale_direction: ScaleDirection, target_hosts: list[HostInfo]
    ) -> Mesh:
        """Generates a new mesh based on the given scale direction and target hosts.

        Args:
            scale_direction (ScaleDirection): The direction in which the mesh should be scaled.
            target_hosts (list[HostInfo]): List of hosts with new updates.

        Returns:
            Mesh: The generated mesh.
        """
        pass

    @abc.abstractmethod
    def generate_commands(
        self, scale_direction: ScaleDirection, updated_mesh: Mesh
    ) -> adaptr_core.CommandSets:
        """
        Defines a set of commands based on scale direction and updated mesh to apply the strategy to the training workload.

         Args:
             scale_direction (ScaleDirection): The direction of scaling.
             updated_mesh (Mesh): The updated mesh resulting from `self.generate_mesh()`.

         Returns:
             adaptr_core.CommandSets: The CommandSets required to apply the strategy.
        """
        pass
