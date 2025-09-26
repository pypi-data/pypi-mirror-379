"""Utility functions for tests."""

import logging
import socket


def find_available_port():
  """Find an available port."""
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(("", 0))
  port = sock.getsockname()[1]
  sock.close()
  return port


def setup_logging():
  logging.basicConfig(
      filename="test_log.log",
      level=logging.DEBUG,
      format="%(asctime)s %(levelname)s:%(message)s",
  )
