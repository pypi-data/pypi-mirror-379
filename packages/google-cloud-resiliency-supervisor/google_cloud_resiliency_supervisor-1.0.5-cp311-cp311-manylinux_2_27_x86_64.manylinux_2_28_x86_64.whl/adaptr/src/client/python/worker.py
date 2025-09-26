import logging
import torch.multiprocessing as mp
import socket
import time
import threading
from typing import Any, Callable, Mapping, Sequence

import adaptr_core
from adaptr.src.core.python import device_info
from adaptr.src.client.python import utils, workload


WORKER_HEARTBEAT_INTERVAL_S = 1


class Worker:
    """Abstraction of Worker processes including communication thread with Host.

    Stores all metadata related to a worker process, including physical worker attributes
    and worker rank. Additionally, this abstraction houses the communication infrastructure
    between the worker and the Host process.
    """

    def __init__(
        self,
        port: int,
        host_port: str,
        local_rank: int,
        global_rank: int,
        hang_timeout: int = 60,
    ):
        """Constructs a Worker object.

        Args:
            port: The port on which to run workload communication.
            host_port: The port running the host process.
            local_rank: The local rank of the worker processes.
            global_rank: The global rank of the worker processes.
            hang_timeout: The time elasped (seconds) between heartbeats before declaring a hang.
        """
        host_address = "localhost:" + str(host_port)
        pci_bus_id = utils.get_pci_bus_id(local_rank)

        # Collect metadata related to worker
        self._worker_info = device_info.WorkerInfo(
            worker_address="localhost:" + str(port),
            worker_name=f"{socket.gethostname()}-{pci_bus_id}",
            worker_id=pci_bus_id,
            local_rank=local_rank,
            global_rank=global_rank,
        )

        self.workload_port = port
        self._workload_proc = None
        self._workload_func = None

        # Set multiprocessing start method before creating any multiprocessing objects
        start_method = mp.get_start_method(allow_none=True)
        if start_method is None:
            logging.info("Setting start method to `spawn`.")
            mp.set_start_method("spawn")
        elif start_method != "spawn":
            logging.warning(
                f"Spawn method was set to {start_method} elsewhere. Resetting to spawn."
            )
            mp.set_start_method("spawn", force=True)
        else:
            logging.warning("Spawn method already set")

        self._workload_intercepts = workload._WorkloadSignals(hang_timeout)
        self._worker = adaptr_core.Worker(
            worker_info=self.export_info(),
            host_address=host_address,
        )
        self._worker.start()

        # If the worker stops heartbeating, the host will determine it has failed.
        # The purpose of the worker heartbeat is to check whether the worker is healthy.
        # Here are the possible scenarios where worker is healthy:
        # 1) Workload is running
        # 2) Workload is not running since host is applying an elastic strategy
        # 3) Workload is not running since worker is not actively training
        # Any other scenario would be considered as unhealthy, such that the heartbeating should stop.

        # self._heartbeat_during_pause is used to determine whether the worker should heartbeat during a pause.
        # self._heartbeat_during_pause is True when the pause is expected,
        #   aka training will resume shortly or can resume in the future
        # self._heartbeat_during_pause is False when the pause is unexpected,
        #   aka training will not resume or cannot resume in the future due to some failure
        self._heartbeat_during_pause = True

        self._heartbeat_thread = threading.Thread(
            target=self._workload_heartbeat_loop, name="hearbeat_thread", daemon=True
        )
        self._heartbeat_thread.start()

    def __repr__(self):
        return self.worker_name

    @property
    def worker_info(self) -> device_info.WorkerInfo:
        """The information of the worker process."""
        return self._worker_info

    @property
    def worker_name(self) -> int:
        """The name of the worker process."""
        return self.worker_info.worker_name

    @property
    def local_rank(self) -> int:
        """The local rank of the worker process."""
        return self.worker_info.local_rank

    @property
    def global_rank(self) -> int:
        """The global rank of the worker process."""
        return self.worker_info.global_rank

    @property
    def worker_id(self) -> str:
        """The serial number of the GPU associated with the worker."""
        return self.worker_info.worker_id

    @property
    def state(self) -> device_info.DeviceState:
        """The current state of the worker."""
        return self.worker_info.state

    @property
    def workload_proc(self) -> mp.Process | None:
        """Returns the process running the worker's training code."""
        return self._workload_proc

    @property
    def is_complete(self) -> bool:
        """Returns whther or not the workload has completed."""
        return self._workload_intercepts.is_complete()

    def await_completion(self):
        """Waits for worker to finish its workload."""
        while not self.is_complete:
            time.sleep(10)

    def start_workload(
        self,
        func: Callable | None = None,
        *args: Sequence[Any],
        **kwargs: Mapping[str, Any],
    ):
        """Run a workload process within the worker. The workload function only needs to be specified once.

        Args:
            func: The callable workload function.
            args: The sequence of arguments to the workload funciton.
            kwargs: The mapping of key word arguments to the workload function.
        """
        self.worker_info.state = device_info.DeviceState.RUNNING

        if not self._workload_func:
            decorated_func = workload.WorkloadWrapper(func, self._workload_intercepts)
            self._workload_func = decorated_func

        self._workload_proc = mp.Process(
            target=self._workload_func,
            args=args,
            kwargs=kwargs,
            name=self.worker_id,
            daemon=False,
        )
        logging.info(f"Started workload process for {self.worker_name}")
        self.workload_proc.start()

        # Since the worker is running, no longer need _heartbeat_during_pause enabled
        self._heartbeat_during_pause = False

    def stop_workload(self):
        """Stop a workload process within the worker."""
        # This function is only called on healthy workers, thus they should heartbeat during a pause.
        # An unhealthy worker should abruptly abort its workload, and the host will determine it has failed.
        self._heartbeat_during_pause = True

        self.worker_info.state = device_info.DeviceState.SPARE

        if self.workload_proc is not None:
            try:
                logging.info(f"Terminating workload process for {self.worker_name}.")
                self.workload_proc.terminate()
                self.workload_proc.join()
                logging.info(f"Workload process for {self.worker_name} terminated.")
            except Exception:
                logging.warning(
                    f"Warning: error with terminating workload process for {self.worker_name}. This can be expected since the workload process is forcefully terminated."
                )
            if self.workload_proc.is_alive():
                logging.error(
                    f"Failed to terminate workload process for {self.worker_name}."
                )
        else:
            logging.info("No workload process to terminate.")

        if not self._heartbeat_during_pause:
            self._heartbeat_thread.join()

    def workload_is_alive(self) -> bool:
        """Check if a worker's target function is still running.

        Returns:
            True if the workload is still alive.
        """
        return self.workload_proc is not None and self.workload_proc.is_alive()

    def export_info(self) -> adaptr_core.WorkerInfo:
        """Export Worker object into adaptr_core WorkerInfo object."""
        return self.worker_info.export_info()

    def update_info(self, worker_info: adaptr_core.WorkerInfo):
        """Update the metadata associated with the worker."""
        self.worker_info.update_info(worker_info)

    def _workload_heartbeat_loop(self):
        """Periodically check the workload for liveliness."""
        logging.info(f"{self.worker_name} heartbeat thread started.")

        # Stop heartbeating if workload is not active and worker should not heartbeat during a pause.
        while self.workload_is_alive() or self._heartbeat_during_pause:
            time.sleep(WORKER_HEARTBEAT_INTERVAL_S)
            # Check if workload is hanging
            if self._workload_intercepts.check_heartbeat():
                self._worker.send_heartbeat(self.export_info())
            else:
                step = self._workload_intercepts.get_current_training_step()
                logging.warning(
                    f"{self.worker_name} workload process hang detected in training step {step}."
                )

        if self._workload_intercepts.is_complete():
            logging.info(f"{self.worker_name} workload successfully completed.")
            self.worker_info.state = device_info.DeviceState.COMPLETE
            self._worker.send_heartbeat(self.export_info())

        logging.info(f"{self.worker_name} heartbeat thread terminated.")
