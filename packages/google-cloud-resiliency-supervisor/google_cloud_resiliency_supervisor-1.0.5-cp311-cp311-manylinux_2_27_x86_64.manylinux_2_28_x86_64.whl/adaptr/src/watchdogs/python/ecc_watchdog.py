#!/usr/bin/env python3

import collections
import random
import subprocess
from typing import Any

import adaptr_core
from adaptr.src.watchdogs.python import base_watchdog


class ECCWatchdog(base_watchdog.BaseWatchdog):
    """Implmentation of BaseWatchdog for ECC errors."""

    def __init__(self, error_threshold: int = 1):
        """
        Initialize ECC error Watchdog.

        Args:
            error_threshold: Number of volatile double-bit errors to trigger alert
        """
        super().__init__(adaptr_core.EventType.ECC, error_threshold)
        self.last_error_count = 0
        self.logger.info("Starting ECC watchdog.")

    def _get_mock_errors(self) -> dict[int, list[dict[str, Any]]]:
        """Generate an ECC error for debugging purposes."""
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
            "xid_code": 48,
            "error_count": 1,
            "status": "error",
            "requires_notification": True,
        }
        device_id = device_ids[random.randint(0, 7)]
        return {device_id: [status]}

    def _get_errors(self) -> dict[str, list[dict[str, Any]]]:
        """
        Run nvidia-smi to get volatile double-bit ECC errors for all GPUs

        Returns:
            Dict of PCI Bus ID to error data dictionary.
        """
        try:
            cmd = [
                "nsenter",
                "-at",
                "1",
                "--",
                "/home/kubernetes/bin/nvidia/bin/nvidia-smi",
                "--query-gpu=pci.bus_id,ecc.errors.uncorrected.volatile.total",
                "--format=csv,noheader",
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            gpu_errors = collections.defaultdict(list)
            for line in result.stdout.strip().split("\n"):
                if line:
                    pci_bus_id, errors = line.split(",")
                    error_count = int(errors) if errors.strip().isdigit() else 0

                    status = {
                        "xid_code": 48,
                        "status": "healthy",
                        "requires_notification": False,
                    }

                    if error_count > self.error_threshold:
                        status["error_count"] = error_count
                        status["status"] = "error"
                        status["requires_notification"] = True

                    gpu_errors[pci_bus_id].append(status)

            if not gpu_errors:
                self.logger.debug("nvidia-smi found no ECC errors.")

            return gpu_errors

        except subprocess.CalledProcessError:
            self.logger.exception("nvidia-smi command failed.")
            raise
        except Exception:
            self.logger.exception("Error running nvidia-smi.")
            raise

    def _format_error_message(self, device_id: str, error_data: dict[str, Any]) -> str:
        """Format the error message for logging and reporting.

        Args:
            device_id: String representation of GPU PCI Bus ID.
            error_data: Dictionary containing error information.

        Returns:
            Formatted error message.
        """
        return f"GPU {device_id}: Detected {error_data['error_count']} volatile double-bit ECC errors"
