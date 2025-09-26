"""Watchdog for monitoring Xid errors from the host."""

import collections
import datetime
import random
import re
import subprocess
from typing import Any

from supervisor.src.client.python import utils
from supervisor.src.watchdogs.python import base_watchdog
import supervisor_core


class XIDWatchdog(base_watchdog.BaseWatchdog):
  """Implmentation of BaseWatchdog for Xid errors."""

  def __init__(self, sample_interval: int = 30, error_threshold: int = 1):
    """Initialize XID error Watchdog.

    Args:
        sample_interval: Time in seconds between error samples.
        error_threshold: Number of Xid errors to trigger alert.
    """
    super().__init__(
        supervisor_core.EventType.XID, error_threshold, sample_interval
    )
    self.logger.info("Starting XID watchdog.")
    self.last_poll_time = datetime.datetime.now(tz=datetime.timezone.utc)

  def _get_mock_errors(self) -> dict[int, list[dict[str, Any]]]:
    """Generate a random Xid error for debugging purposes."""
    self.logger.info("Generating mock XID error.")

    device_index = random.randint(0, 7)
    device_id = utils.get_pci_bus_id(device_index, use_nsenter=True)

    status = {
        "xid_code": random.randint(14, 50),
        "channel_info": None,
        "status": "error",
        "requires_notification": True,
    }
    return {device_id: [status]}

  def _get_errors(self) -> dict[int, list[dict[str, Any]]]:
    """Run journalctl to get NVRM logs for XID errors on all GPUs.

    Returns:
        Dict of GPU PCI Bus ID to error information
    """

    # Get kernel logs via nsenter
    journalctl_cmd = [
        "nsenter",
        "-at",
        "1",
        "--",
        "journalctl",
        "-k",
        "--since",
        format(self.last_poll_time, "%Y-%m-%d %H:%M:%S UTC"),
    ]

    try:
      p1 = subprocess.run(
          journalctl_cmd, capture_output=True, text=True, check=True
      )
      journalctl_out = p1.stdout
      self.last_poll_time = datetime.datetime.now(tz=datetime.timezone.utc)

    except subprocess.CalledProcessError as e:
      self.logger.exception(
          f"Failed to run nsenter or journalctl with error: {e.returncode}"
      )
      raise

    # Regex for XID lines, extracting device ID, XID code, and optional channel info.
    xid_pattern = r"NVRM: Xid \((.*?)\): (\d+)(?:, (Channel [^\)]+))?"

    gpu_errors = collections.defaultdict(list)
    for line in journalctl_out.strip().splitlines():
      xid_match = re.search(xid_pattern, line)

      if xid_match:
        pci_bus_id = xid_match.group(1).strip()
        xid_code = xid_match.group(2).strip()
        channel_info = xid_match.group(3)

        if channel_info:
          channel_info = channel_info.strip()

        if "PCI:" in pci_bus_id:
          pci_bus_id = pci_bus_id.replace("PCI:", "")

        if "00000000" not in pci_bus_id:
          pci_bus_id = "0000" + pci_bus_id

        if ".0" not in pci_bus_id:
          pci_bus_id = pci_bus_id + ".0"

        pci_bus_id = pci_bus_id.upper()

        # Adding leading and trailing zeros to match nvidia-smi
        status = {
            "xid_code": int(xid_code),
            "channel_info": channel_info,
            "status": "error",
            "requires_notification": True,
        }
        gpu_errors[pci_bus_id].append(status)

    return gpu_errors

  def _format_error_message(
      self, device_id: str, error_data: dict[str, Any]
  ) -> str:
    """Format the error message for logging and reporting.

    Args:
        device_id: String representation of GPU PCI Bus ID.
        error_data: Dictionary containing error information.

    Returns:
        Formatted error message.
    """
    return (
        f"GPU {device_id}: Detected Xid error: {error_data['xid_code']} with"
        f" channel info: {error_data['channel_info']}"
    )
