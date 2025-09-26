from google.cloud import logging as gcloud_logging

import contextlib
import logging
import numpy as np
import subprocess
import time
import threading
import _thread
import typing

from adaptr.src.client.python import utils
from adaptr.src.simulator.python import base_simulator


class GPUFailureSimulator(base_simulator.BaseSimulator):
    """
    Simulates GPU failures in a distributed training environment.

    This class simulates GPU failures by randomly killing processes running on GPUs
    based on a given Mean Time Between Failures (MTBF). It uses a Poisson distribution
    to model the failure probability.
    """

    def __init__(
        self,
        rank: int,
        gpu_world_size: int,
        gpus_per_node: int = 8,
        seed: int = 42,
        gcloud_logging_client: gcloud_logging.Client | None = None,
    ):
        """Initializes instance of FailureSimulator.

        Args:
            rank (int): The rank of the VM running the simulator.
            gpu_world_size (int): The total number of GPUs in the distributed environment.
            gpus_per_node (int, optional): The number of GPUs per node. Defaults to 8.
        """
        super().__init__(rank, gpu_world_size, gpus_per_node, seed)

        logging.info("Initializing GPU failure simulator.")
        self._rng = np.random.default_rng(seed=self.seed)
        self._logger = None

        # Initialize Google Cloud Logging client
        if gcloud_logging_client is not None:
            self._logging_client = gcloud_logging_client
            self._logger = self._logging_client.logger("gpu-failure-simulator")

    def _gpu_kill_fn(self, local_ranks: list[int]):
        """Kills the processes running on GPUs on specified local ranks.

        Args:
            local_ranks (list[int]): The ranks of GPUs to be killed.
        """
        nsenter_prefix = "nsenter -at 1 --"
        local_ranks_str = ",".join([str(rank) for rank in local_ranks])
        get_pids_cmd = f"/home/kubernetes/bin/nvidia/bin/nvidia-smi --query-compute-apps pid,name --format=csv,noheader -i {local_ranks_str}"
        result = subprocess.run(
            nsenter_prefix.split() + get_pids_cmd.split(),
            capture_output=True,
            shell=False,
            text=True,
        )

        if result.returncode != 0:
            logging.warning(f"Command {get_pids_cmd} failed with {result.stdout}.")
        else:
            processes = result.stdout.splitlines()
            pids = [
                process.split(", ")[0]
                for process in processes
                if "python" in process.split(", ")[1]
            ]
            pkill_cmd = f"sudo kill -9 {' '.join(pids)}"
            logging.info(f"Killing processes: {pkill_cmd}")

            subprocess.run(
                nsenter_prefix.split() + pkill_cmd.split(),
                capture_output=True,
                shell=False,
                text=True,
            )

    @property
    def distribution(self) -> typing.Callable:
        """
        Returns the probability distribution used for sampling failures.

        Returns:
            Callable: The numpy Generator Poisson distribution function.
        """
        return self._rng.poisson

    def sample(self, lambda_value: float) -> np.ndarray[bool]:
        """
        Samples for GPU failures based on the Poisson distribution.

        Returns:
            np.ndarray[bool]: A boolean array indicating which GPUs have failed.
        """
        random_numbers = np.random.rand(self.gpus_per_node)
        probabilities = self.distribution(lambda_value, self.gpus_per_node)
        return random_numbers < probabilities

    def simulate(
        self,
        mtbf: float,
        sample_interval: int,
        run_async: bool = False,
        mutex: _thread.LockType | None = None,
    ):
        """
        Starts the failure simulation loop.

        This method continuously samples for failures and simulates them by killing
        the corresponding processes running on the failed GPUs. It runs until a
        termination file is detected.

        Args:
            mtbf (float): The Mean Time Between Failures (MTBF) in years.
            sample_interval (int): The interval in seconds between samples.
            intermittent (bool): Allows for slow GPUs to recover if they are re-sampled. Defaults to False.
            run_async (bool): Whether to run the simulation asynchronously. Defaults to False.
            mutex (LockType): Optional mutex to synchronize multiple simulatenous simulators. Defaults to None.
        """
        mtbf_s = mtbf * 365 * 24 * 3600
        lambda_value = (1 / mtbf_s) * sample_interval
        mutex = mutex if mutex is not None else contextlib.nullcontext()

        logging.info(
            f"Starting simulation loop with MTBF: {mtbf} years and sample interval: {sample_interval} seconds."
        )

        def simulate_loop():
            while not utils.check_termination_file():
                failure_events = self.sample(lambda_value)
                if failure_events.any():
                    with mutex:
                        failure_ranks = np.where(failure_events)[0].tolist()
                        global_ranks = self.local_to_global_ranks(failure_ranks)
                        self.induce_event(global_ranks)
                        self.report_events(global_ranks)

                time.sleep(sample_interval)

        if run_async:
            thread = threading.Thread(target=simulate_loop, name="failure_simulator")
            thread.start()
        else:
            simulate_loop()

        logging.info("Terminating failure simulator.")

    def induce_event(self, global_ranks: list[int]):
        """
        Simulates GPU failures by killing processes running on the failed GPUs.

        Args:
            global_ranks (list[int]): A list indicating the global ranks of which GPUs have failed.
        """
        if len(global_ranks) == 0:
            return

        # Only induce events on GPUs within the current VM
        global_ranks = self.filter_global_ranks(global_ranks)
        local_ranks = self.global_to_local_ranks(global_ranks)

        logging.info(f"Simulating failure on GPUs: {global_ranks}")
        self._gpu_kill_fn(local_ranks)

    def report_events(self, global_ranks: list[int]):
        """
        Reports the failure event to the console and Google Cloud Logging.

        Args:
            global_ranks (list): A list indicating the global ranks of which GPUs have failed.
        """
        if len(global_ranks) == 0:
            return

        global_ranks = self.filter_global_ranks(global_ranks)
        message = f"GPU failure simulated on GPUs: {global_ranks}"
        logging.warning(message)

        if self._logger is not None:
            self._logger.log_struct({"message": message, "severity": "WARNING"})
