from typing import Any
from torch.distributed.checkpoint.stateful import Stateful
import torch.nn as nn
import torch.optim as optim


class TrainingState(Stateful):
  """This class defines an object compatible with PyTorch checkpointing APIs that stores the relevant state of the training workload.

  Since this object is compliant with the Stateful protocol, DCP will
  automatically call state_dict/load_stat_dict as needed in the
  dcp.save/load APIs. We take advantage of this wrapper to hande calling
  distributed state dict methods on the model
  and optimizer.

  Checkpoints should have the general format:
  {
      "model": model.state_dict(),
      "optim": optimizer.state_dict(),
      "metadata": {
          "epoch": epoch,
          "step": step,
          "world_size": world_size,
          "global_rank": global_rank,
          "micro_batch_size": micro_batch_size,
          "global_batch_size": global_batch_size,
  }
  """

  def __init__(
      self,
      model: nn.Module,
      optimizer: optim.Optimizer,
      epoch: int = 0,
      step: int = 0,
      world_size: int = None,
      global_rank: int = None,
      micro_batch_size: int = None,
      global_batch_size: int = None,
  ):
    """Initializes the TrainingState object.

    Args:
        model (nn.Module): The model used for training.
        optimizer (optim.Optimizer): The optimizer used for training.
        epoch (int, optional): The epoch. Defaults to 0.
        step (int, optional): The training step. Defaults to 0.
        world_size (int, optional): The pytorch world size . Defaults to None.
        global_rank (int, optional): The global rank of the pytorch process.
          Defaults to None.
        micro_batch_size (int, optional): The micro batch size. Defaults to
          None.
        global_batch_size (int, optional): The global batch size. Defaults to
          None.
    """

    self.model = model
    self.optimizer = optimizer
    self.epoch = epoch
    self.step = step
    self.world_size = world_size
    self.global_rank = global_rank
    self.micro_batch_size = micro_batch_size
    self.global_batch_size = global_batch_size

  def state_dict(self):
    """Gathers model state, optimizer state, and metadata into a dictionary.

    Returns:
        dict: The state dictionary.
    """
    return {
        "model": self.model.state_dict(),
        "optim": self.optimizer.state_dict(),
        "metadata": self.get_metadata(),
    }

  def load_state_dict(self, state_dict: dict[str, Any]):
    """Loads model and optimizer state from the given state dictionary.

    Also loads metadata.

    Args:
        state_dict (dict[str, Any]): The state dictionary to load from.
    """
    self.model.load_state_dict(state_dict["model"])
    self.optimizer.load_state_dict(state_dict["optim"])
    self.load_metadata(state_dict["metadata"])

  def get_metadata(self):
    """Gathers metadata into a dictionary.

    Returns:
        dict: The metadata dictionary.
    """
    return {
        "epoch": self.epoch,
        "step": self.step,
        "world_size": self.world_size,
        "global_rank": self.global_rank,
        "micro_batch_size": self.micro_batch_size,
        "global_batch_size": self.global_batch_size,
    }

  def load_metadata(self, metadata: dict[str, Any]):
    """Loads metadata from the given dictionary

    Args:
        metadata (dict[str, Any]): The metadata dictionary to load from.
    """
    self.epoch = metadata["epoch"]
    self.step = metadata["step"]
    self.world_size = metadata["world_size"]
    self.global_rank = metadata["global_rank"]
    self.micro_batch_size = metadata["micro_batch_size"]
    self.global_batch_size = metadata["global_batch_size"]
