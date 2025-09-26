#!/usr/bin/env python3

import collections
import random
import re
import subprocess
from typing import Any

import adaptr_core
from adaptr.src.watchdogs.python import base_watchdog


class XIDWatchdog(base_watchdog.BaseWatchdog):
    """Implmentation of BaseWatchdog for Xid errors."""

    def __init__(self):
        """
        Initialize XID error Watchdog.
        """
        super().__init__(adaptr_core.EventType.XID)
        self.logger.info("Starting XID watchdog.")

    def _get_mock_errors(self) -> dict[int, list[dict[str, Any]]]:
        """Generate a random Xid error for debugging purposes."""
        device_ids = {
            0: "00000000:04:00.0",
            1: "00000000:05:00.0",
            2: "00000000:0A:00.0",
            3: "00000000:0B:00.0",
            4: "00000000:84:00.0",
            5: "00000000:85:00.0",
            6: "00000000:8A:00.0",
            7: "00000000:8B:00.0",
        }
        status = {
            "xid_code": random.randint(14, 50),
            "channel_info": None,
            "status": "error",
            "requires_notification": True,
        }
        device_id = device_ids[random.randint(0, 7)]
        return {device_id: [status]}

    def _get_errors(self) -> dict[int, list[dict[str, Any]]]:
        """
        Run journalctl to get NVRM logs for XID errors on all GPUs.

        Returns:
            Dict of GPU PCI Bus ID to error information
        """
        try:
            cmd = [
                "nsenter",
                "-at",
                "1",
                "--",
                "journalctl",
                "-k",
                "|",
                "grep",
                '"NVRM: Xid"',
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Regex for XID lines, extracting device ID, XID code, and optional channel info.
            xid_pattern = r"NVRM: Xid \((.*?)\): (\d+)(?:, (Channel [^\)]+))?"

            gpu_errors = collections.defaultdict(list)
            for line in result.stdout.strip().split("\n"):
                xid_match = re.search(xid_pattern, line)

                if xid_match:
                    pci_bus_id = xid_match.group(1).strip()
                    xid_code = xid_match.group(2).strip()
                    channel_info = xid_match.group(3)

                    if channel_info:
                        channel_info = channel_info.strip()

                    # Adding leading and trailing zeros to match nvidia-smi
                    pci_bus_id = "0000" + pci_bus_id + ".0"
                    status = {
                        "xid_code": xid_code,
                        "channel_info": channel_info,
                        "status": "error",
                        "requires_notification": True,
                    }
                    gpu_errors[pci_bus_id].append(status)

            return gpu_errors

        except subprocess.CalledProcessError as e:
            if e.returncode == 1:
                self.logger.debug("journalctl found no Xid errors.")
                return {}
            else:
                self.logger.exception(
                    f"journalctl failed with non-zero return code {e.returncode}."
                )
                raise
        except Exception:
            self.logger.exception("Error running journalctl.")
            raise

    def _format_error_message(self, device_id: str, error_data: dict[str, Any]) -> str:
        """Format the error message for logging and reporting.

        Args:
            device_id: String representation of GPU PCI Bus ID.
            error_data: Dictionary containing error information.

        Returns:
            Formatted error message.
        """
        return f"GPU {device_id}: Detected Xid error: {error_data['xid_code']} with channel info: {error_data['channel_info']}"
