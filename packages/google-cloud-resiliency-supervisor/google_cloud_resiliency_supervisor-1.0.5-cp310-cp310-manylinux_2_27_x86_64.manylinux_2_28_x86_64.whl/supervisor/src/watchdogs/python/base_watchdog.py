"""Base class for watchdogs monitoring GPU health from the host."""

import abc
import os
import time
from typing import Any

import numpy as np
from supervisor.src.core.python import utils
import supervisor_core


class BaseWatchdog(abc.ABC):
  """Abstract base class for watchdogs monitoring GPU health.

  This class provides a common interface for different watchdog implementations,
  handling tasks like error collection, reporting, and the main polling method.
  Subclasses should implement the `_get_errors` method to retrieve GPU error
  data and `_format_error_message` to format the error message for logging and
  reporting.
  """

  def __init__(
      self,
      event_type: supervisor_core.EventType,
      error_threshold: int = 1,
      sample_interval: int = 30,
      notification_cooldown: int = 300,
      seed: int | None = None,
  ):
    """Initialize Base Watchdog.

    Args:
        event_type: The type of error the watchdog is expecting.
        error_threshold: The number of errors to observe prior to reporting.
        sample_interval: The time in seconds between error samples.
        notification_cooldown: The time in seconds between notifications.
        seed: The random seed for the watchdog. Used for fault injection.
    """
    self.seed = seed
    self.event_type = event_type
    self.error_threshold = error_threshold
    self.sample_interval = sample_interval
    self.notification_cooldown = notification_cooldown

    # Setup logging
    self.logger = utils.setup_logger()

    # Initialize state
    self.error_buffer = []
    self.last_notification_time = None

    # Enable fault injection
    self.enable_fault_injection = os.getenv("ENABLE_FAULT_INJECTION", "false")
    self.enable_fault_injection = self.enable_fault_injection.lower() == "true"
    self.fault_injection_frequency = int(
        os.getenv("FAULT_INJECTION_PERIOD_S", 0)
    )

    # Initialize failure distriution
    self._rng = np.random.default_rng(seed=self.seed)
    self._lambda = (1 / self.fault_injection_frequency) * self.sample_interval

    if self.enable_fault_injection and self.fault_injection_frequency > 0:
      self._last_injection_time = time.time()
      self.logger.info(
          "Fault injection enabled with period"
          f" {self.fault_injection_frequency}s."
      )

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
  ) -> supervisor_core.EventReport:
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
        and current_time - self.last_notification_time
        < self.notification_cooldown
    ):
      return None

    self.last_notification_time = current_time

    event_report = supervisor_core.EventReport()
    event_report.event_type = self.event_type
    event_report.device_id = device_id
    event_report.xid_code = error_data["xid_code"]
    event_report.message = self._format_error_message(device_id, error_data)
    return event_report

  @abc.abstractmethod
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
    pass

  def poll(self) -> list[supervisor_core.EventReport]:
    """Poll for errors and generate reports.

    Returns:
        List of EventReports for detected errors.
    """
    self.error_buffer.clear()
    try:
      if self.enable_fault_injection and self._rng.poisson(self._lambda) > 0:
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
