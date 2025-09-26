#!/usr/bin/env python3

import abc
import time
import logging
from typing import Any

import adaptr_core


class BaseWatchdog(abc.ABC):
    """
    Abstract base class for watchdogs monitoring GPU health.

    This class provides a common interface for different watchdog implementations,
    handling tasks like error collection, reporting, and the main polling method.
    Subclasses should implement the `_get_errors` method to retrieve GPU error data
    and `_format_error_message` to format the error message for logging and reporting.
    """

    def __init__(
        self,
        event_type: adaptr_core.EventType,
        error_threshold: int = 1,
        notification_cooldown: int = 300,
    ):
        """
        Initialize Base Watchdog.

        Args:
            event_type: The type of error the watchdog is expecting.
            error_threshold: The number of errors to observe prior to reporting.
            notification_cooldown: The time in seconds between notifications.
        """
        self.event_type = event_type
        self.error_threshold = error_threshold
        self.notification_cooldown = notification_cooldown

        # Setup logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Initialize state
        self.error_buffer = []
        self.last_notification_time = None

    @abc.abstractmethod
    def _get_errors(self) -> dict[str, list[dict[str, Any]]]:
        """Abstract method to retrieve errors.

        Should return a dictionary where keys are device identifiers (PCI bus ID)
        and values are lists of error dictionaries. Each error dictionary should
        contain at least 'xid_code' and optionally other relevant info.

        Returns:
            Dictionary containing GPU errors.
        """
        pass

    @abc.abstractmethod
    def _get_mock_errors(self) -> dict[str, list[dict[str, Any]]]:
        """Abstract method to generate mock errors for debug purposes.

        Should return a dictionary where keys are device identifiers (PCI bus ID)
        and values are lists of error dictionaries. Each error dictionary should
        contain at least 'xid_code' and optionally other relevant info.

        Returns:
            Dictionary containing GPU errors.
        """
        pass

    def _generate_error_report(
        self, device_id: str, error_data: dict[str, Any]
    ) -> adaptr_core.EventReport:
        """Generate an Event Report for a single error.

        Args:
            device_id: String representation of GPU PCI Bus ID.
            error_data: Dictionary containing error information.

        Returns:
            EventReport for the detected error.
        """
        # TODO: Make notification cooldown XID code aware
        current_time = time.time()
        if (
            self.last_notification_time
            and current_time - self.last_notification_time < self.notification_cooldown
        ):
            return None

        self.last_notification_time = current_time

        event_report = adaptr_core.EventReport()
        event_report.event_type = self.event_type
        event_report.device_id = device_id
        event_report.xid_code = error_data["xid_code"]
        event_report.message = self._format_error_message(device_id, error_data)
        return event_report

    @abc.abstractmethod
    def _format_error_message(self, device_id: str, error_data: dict[str, Any]) -> str:
        """Format the error message for logging and reporting.

        Args:
            device_id: String representation of GPU PCI Bus ID.
            error_data: Dictionary containing error information.

        Returns:
            Formatted error message.
        """
        pass

    def poll(self, debug_mode: bool = False) -> list[adaptr_core.EventReport]:
        """Poll for errors and generate reports.

        Returns:
            List of EventReports for detected errors.
        """
        self.error_buffer.clear()
        try:
            if debug_mode:
                gpu_errors = self._get_mock_errors()
            else:
                gpu_errors = self._get_errors()

            for device_id, error_list in gpu_errors.items():
                for error_data in error_list:
                    if error_data["requires_notification"]:
                        self.logger.warning(
                            self._format_error_message(device_id, error_data)
                        )
                        report = self._generate_error_report(device_id, error_data)
                        if report is not None:
                            self.error_buffer.append(report)

            return self.error_buffer

        except RuntimeError:
            self.logger.exception("Error in error polling.")
            return []
