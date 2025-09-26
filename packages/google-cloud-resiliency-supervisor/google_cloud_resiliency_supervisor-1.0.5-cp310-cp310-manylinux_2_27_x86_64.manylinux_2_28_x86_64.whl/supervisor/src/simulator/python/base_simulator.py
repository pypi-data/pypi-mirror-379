import abc
import typing
import numpy as np


class BaseSimulator(abc.ABC):
  """An abstract base class for defining failure simulators used for goodput studies.

  This class provides a common interface for different types of failure
  simulators. Concrete simulators should inherit from this class and implement
  the abstract methods.
  """

  def __init__(
      self,
      rank: int,
      gpu_world_size: int,
      gpus_per_node: int = 8,
      seed: int = 42,
  ):
    """Initializes the BaseSimulator with common parameters.

    Args:
        rank (int): The rank of the VM running the simulator.
        gpu_world_size (int): The total number of GPUs in the distributed
          environment.
        gpus_per_node (int, optional): The number of GPUs per node. Defaults to
          8.
    """
    self.rank = rank
    self.gpu_world_size = gpu_world_size
    self.gpus_per_node = gpus_per_node
    self.seed = seed

  def local_to_global_ranks(self, local_ranks: list[int]) -> list[int]:
    """Converts local ranks to global ranks.

    Returns:
        list[int]: A list of global ranks corresponding to the input local
        ranks.
    """
    global_ranks = [
        rank + (self.rank * self.gpus_per_node) for rank in local_ranks
    ]
    return global_ranks

  def global_to_local_ranks(self, global_ranks: list[int]) -> list[int]:
    """Converts local ranks to global ranks.

    Returns:
        list[int]: A list of global ranks corresponding to the input local
        ranks.
    """
    local_ranks = [rank % self.gpus_per_node for rank in global_ranks]
    return local_ranks

  def filter_global_ranks(self, global_ranks: list[int]) -> list[int]:
    """Filters out GPUs with global rank outside of the current VM's range.

    Returns:
        list[int]: A list of global ranks corresponding to the current VM.
    """
    filtered_global_ranks = [
        rank
        for rank in global_ranks
        if rank >= (self.rank * self.gpus_per_node)
        and rank < ((self.rank + 1) * self.gpus_per_node)
    ]
    return filtered_global_ranks

  @property
  @abc.abstractmethod
  def distribution(self) -> typing.Callable:
    """Returns the probability distribution used for sampling failures.

    Returns:
        Callable: The numpy Generator distribution used for sampling failures.
    """
    pass

  @abc.abstractmethod
  def sample(self, *args, **kwargs) -> np.ndarray[bool]:
    """Samples for a failure event accross all GPUs.

    Returns:
        np.ndarray[bool]: A boolean array indicating which GPUs have failed.
    """
    pass

  @abc.abstractmethod
  def simulate(
      self,
      *args,
      **kwargs,
  ):
    """Starts the failure simulation.

    This method defines the main loop for the simulation and should be
    implemented by concrete simulators to define the specific failure simulation
    logic.
    """
    pass

  @abc.abstractmethod
  def induce_event(self, *args, **kwargs):
    """Induces failure event determinisitcally.

    This method defines a mechanism to manually induce a failure event and
    should be implemented by concrete simulators to define the specific failure
    event logic.
    """
    pass

  @abc.abstractmethod
  def report_events(self, *args, **kwargs):
    """Reports the failure events observed.

    This method should be implemented by concrete simulators to define how
    failure events are logged (e.g., to the console, to a file, or to a
    cloud logging service).
    """
    pass
