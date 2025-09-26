import logging
import os
import pathlib
import re
import requests
import signal
import socket
import subprocess
import threading
import time
from typing import Any
from google.cloud import compute_v1
from google.api_core.exceptions import GoogleAPIError
from google.api_core.retry import Retry, if_exception_type


TERM_FILE_BASE = "/usr/share/adaptr/workload_terminated"

_default_retry_policy = Retry(
    predicate=if_exception_type(GoogleAPIError),
    initial=1.0,
    maximum=10.0,
    multiplier=1.3,
    deadline=15.0,
)


def launch_sync_proc(command: list[str]) -> str:
    """Launches a process, waits for it to finish, and returns its output.

    Args:
      command: Command to execute, split into spaceless strings

    Returns:
      The output of the subprocess, including both stderr and stdout
    """
    logging.info("Executing: %s", command)
    proc = subprocess.run(
        command,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
        text=True,
    )
    output = proc.stdout
    logging.info("Output: %s", output)
    return output


class AsyncSubprocess:
    """Manages a subprocess and output collection asynchronously."""

    def __init__(
        self,
        command: list[str],
        to_stdout: bool = True,
        log_file: pathlib.Path | None = None,
        env: dict[str, Any] | None = None,
    ):
        """Starts the subprocess and output collection thread.

        Args:
          command: The command to execute in the subprocess
          to_stdout: If true, all subprocess output will be mirrored to stdout
          log_file: If not None, all subprocess output will be mirrored to this file
          env: Dict of env vars to pass to the subprocess. If None, the subprocess
            will inherit the parent process's environment.
        """

        def _stringify_envs(envs: dict[str, Any]) -> dict[str, str]:
            out_envs = {}
            for env_name, env_value in envs.items():
                # Resolve any nested env vars (only resolves if they are set)
                env_value = os.path.expandvars(str(env_value))

                # Replace unset env vars with '', like bash would
                env_value = re.sub(
                    r"\$[A-Za-z_][A-Za-z0-9_]*", "", os.path.expandvars(env_value)
                )
                env_value = re.sub(
                    r"\${[A-Za-z_][A-Za-z0-9_]*}", "", os.path.expandvars(env_value)
                )

                out_envs[env_name] = env_value
            return out_envs

        logging.info("Executing:\n%s", command)
        self._command = command
        self._proc: subprocess.Popen[str] = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            text=True,
            env=_stringify_envs(env) if env else None,
        )
        self._thread: threading.Thread = threading.Thread(
            target=_multi_stream_proc_output, args=[self._proc, to_stdout, log_file]
        )
        self._thread.start()
        self._retcode: int | None = None

    def wait(self, timeout_sec: float | None = None) -> int:
        """Waits for the process and output collection thread to finish.

        Args:
          timeout_sec: Timeout length in seconds

        Returns:
          The return code of the completed process

        Raises:
          TimeoutError: Raised after waiting for over timeout_sec
        """
        cmd_str = " ".join(self._command)
        if timeout_sec is None:
            logging.info("Waiting for the process to complete: %s", cmd_str)
        else:
            logging.info(
                "Waiting %f seconds for the process to complete: %s",
                timeout_sec,
                cmd_str,
            )

        self._proc.poll()
        self._thread.join(timeout=timeout_sec)

        # Thread.join always returns None, so we need to check aliveness to know if
        # it timed out or not
        if self._thread.is_alive():
            raise TimeoutError(
                f"Timed out after {timeout_sec} seconds waiting for"
                f" {' '.join(self._command)}"
            )

        # Once the polling thread has exited, the process should be on its way to
        # completion. Wait a little bit to ensure that everything finishes up.
        self._proc.wait(10)
        self._retcode = self._proc.poll()
        if self._retcode is None:
            raise ValueError("Process return code is None. This should not happen.")
        return self._retcode

    def terminate(self) -> None:
        """Terminates the subprocess with a signal."""
        logging.info("Terminating the process executing:\n%s", " ".join(self._command))
        try:
            os.kill(self._proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        self.wait(timeout_sec=5)  # Wait for output to finish processing


def _multi_stream_proc_output(
    proc: subprocess.Popen[str],
    to_stdout: bool,
    log_file: pathlib.Path | None = None,
):
    """Streams output from a process to multiple places.

    Args:
      proc: Process to stream output from
      to_stdout: If true, streams subprocess output to stdout
      log_file: If not None, streams subprocess output to this file
    """
    log_fd = None
    if log_file:
        log_fd = open(log_file, "w")

    if proc.stdout is None:
        raise ValueError("Subprocess stdout is None. This should not happen.")
    for line in proc.stdout:
        if to_stdout:
            logging.info(line.strip())
        if log_fd:
            log_fd.write(line)

    logging.info("Logging thread is finishing")

    if log_fd:
        log_fd.close()


def get_cuda_visible_devices() -> list[int]:
    """Returns the devices that should be visible for this machine configuration.

    Returns:
      A list of visible CUDA device indices
    """
    return list(range(8))


def get_gpu_serial(local_rank: int) -> str:
    """Gets the serial number of the GPU for the given rank via nvidia-smi.

    Args:
      local_rank: Workload rank within the node

    Returns:
      The GPU serial number as a string
    """
    return launch_sync_proc(
        [
            "/usr/local/nvidia/bin/nvidia-smi",
            "--query-gpu",
            "serial",
            "--format",
            "csv,noheader",
            "-i",
            str(local_rank),
        ]
    ).strip()


def get_pci_bus_id(local_rank: int) -> str:
    """Gets the PCI Bus ID of the GPU for the given rank via nvidia-smi.

    Args:
      local_rank: Workload rank within the node

    Returns:
      The GPU serial number as a string
    """
    return launch_sync_proc(
        [
            "/usr/local/nvidia/bin/nvidia-smi",
            "--query-gpu",
            "pci.bus_id",
            "--format",
            "csv,noheader",
            "-i",
            str(local_rank),
        ]
    ).strip()


def get_host_physical_attributes(
    project_id: str, zone: str, host_name: str
) -> tuple[str, str, str]:
    """Gets the physical attributes of this host.

    Returns:
      Tuple containing Superblock, Subblock (Rack) and Serial Number
    """
    try:
        instance_client = compute_v1.InstancesClient()
        instance = instance_client.get(
            project=project_id,
            zone=zone,
            instance=host_name,
            retry=_default_retry_policy,
        )
        if instance and instance.resource_status.physical_host:
            superblock_id, subblock_id, host_serial_number = (
                instance.resource_status.physical_host.split("/")[1:]
            )
            return superblock_id, subblock_id, host_serial_number
        else:
            logging.info(
                "No information was available to parse. Is this machine in a compact placement group?"
            )
            return None
    except GoogleAPIError as e:
        logging.exception(f"Error getting host attributes after retries: {e}")
        raise


def get_host_zone() -> str:
    """Gets the zone of this host.

    Returns:
      String representing the zone of this host.
    """
    try:
        return requests.get(
            "http://metadata.google.internal/computeMetadata/v1/instance/zone?alt=text",
            headers={"Metadata-Flavor": "Google"},
        ).text.split("/")[-1]
    except RuntimeError as e:
        logging.exception("Zone query to Google Cloud metadata server failed.")
        raise e


def get_host_ip() -> str:
    """
    Gets the IP address of the host machine.

    Returns:
      The IP address of the host machine as a string.
    """
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to a remote host (doesn't actually need to be reachable)
        s.connect(("8.8.8.8", 80))
        # Get the local IP address assigned to the socket
        ip_address, _ = s.getsockname()
        s.close()
        return ip_address
    except Exception as e:
        logging.exception("Error getting host IP address.")
        raise e


def get_host_id() -> str:
    """Gets the ID of this VM.

    Returns:
      The VM ID of this VM
    """
    try:
        return requests.get(
            "http://metadata.google.internal/computeMetadata/v1/instance/id?alt=text",
            headers={"Metadata-Flavor": "Google"},
        ).text
    except RuntimeError as e:
        logging.exception("VM ID query to Google Cloud metadata server failed.")
        raise e


def get_host_name() -> str:
    """Gets the Name of this VM.

    Returns:
      The VM Name of this VM
    """
    try:
        full_name = requests.get(
            "http://metadata.google.internal/computeMetadata/v1/instance/hostname?alt=text",
            headers={"Metadata-Flavor": "Google"},
        ).text

        # Host name is returned in format of <VM_Name>.<Zone>.<Sub-zone>.<Project>.<Project-Tenant>
        host_name = full_name.split(".")[0]
        logging.info(f"Got host name: {host_name} from full response {full_name}")
        return host_name
    except RuntimeError as e:
        logging.exception("VM hostname query to Google Cloud metadata server failed.")
        raise e


def clean_termination_files() -> None:
    """Cleans up old termination files."""
    try:
        file = _get_term_filepath()
        if file.exists():
            os.remove(file)
            logging.info("Removed old termination file %s", file)
    except OSError:
        logging.warning("Failed to remove old termination files.")


def _get_term_filepath() -> pathlib.Path:
    """Returns the termination semaphore file path.

    Returns:
        Termination semaphore file path
    """
    return pathlib.Path(f"{TERM_FILE_BASE}")


def check_termination_file() -> bool:
    """Returns whether the termination file exists or not."""
    file = _get_term_filepath()
    return file.exists()


def create_termination_file() -> None:
    """Creates workload termination semaphores shared with other containers."""
    try:
        logging.info("Creating termination file")
        f = _get_term_filepath()
        os.makedirs(f.parent, exist_ok=True)
        f.touch()
        logging.info("Created termination file at %s", f)
    except OSError:
        logging.warning("Failed to create termination file.")


def check_and_clean_port(port, kill_delay=5):
    """
    Checks if a given port is in use. If so, attempts to identify and
    terminate the process using the port, then rechecks.

    Args:
        port: The port number (integer) to check.
        kill_delay: Time (in seconds) to wait after sending SIGTERM before
            sending SIGKILL.

    Returns:
        True if the port is now free, False if the port is still in use
        after attempting to clean it, or if an error occurred.
    """

    def is_port_in_use(port):
        """Helper function to check if a port is currently in use."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(("localhost", port)) == 0

    if not is_port_in_use(port):
        logging.info(f"Port {port} is free.")
        return True

    logging.info(f"Port {port} is in use. Attempting to clean...")

    try:
        # Use lsof to find the PID using the port.  More reliable than fuser
        # -n tcp: Only look at TCP ports.
        # -t: Output only the PID (terse mode).
        # -i: Specify the port to check
        result = subprocess.run(
            ["lsof", "-t", "-i", f"tcp:{port}"],
            capture_output=True,
            text=True,
            check=True,
        )
        pid_str = result.stdout.strip()

        if not pid_str:
            logging.info(
                f"Could not find a process using port {port} (lsof returned empty output)."
            )
            return False  # Port is *claimed* to be in use, but we couldn't find the PID

        pid = int(pid_str)
        logging.info(f"Process ID {pid} is using port {port}.")

        # Try to gracefully terminate the process (SIGTERM).
        logging.info(f"Sending SIGTERM to process {pid}...")
        os.kill(pid, signal.SIGTERM)
        time.sleep(kill_delay)  # Give the process time to exit

        if not is_port_in_use(port):
            logging.info(f"Port {port} is now free (process terminated gracefully).")
            return True

        # If still in use, forcefully terminate (SIGKILL).
        logging.info(f"Process {pid} did not terminate gracefully. Sending SIGKILL...")
        os.kill(pid, signal.SIGKILL)
        time.sleep(1)  # Short delay to allow OS to clean up

        if not is_port_in_use(port):
            logging.info(f"Port {port} is now free (process killed).")
            return True
        else:
            logging.info(
                f"Port {port} is still in use after SIGKILL.  Manual intervention may be required."
            )
            return False

    except subprocess.CalledProcessError:
        logging.exception("Error running lsof.")
        return False
    except ValueError:
        logging.exception(f"lsof returned invalid PID: {result.stdout.strip()}")
        return False
    except OSError:
        logging.exception("Error killing process.")
        return False
    except Exception:
        logging.exception("An unexpected error.")
        return False
