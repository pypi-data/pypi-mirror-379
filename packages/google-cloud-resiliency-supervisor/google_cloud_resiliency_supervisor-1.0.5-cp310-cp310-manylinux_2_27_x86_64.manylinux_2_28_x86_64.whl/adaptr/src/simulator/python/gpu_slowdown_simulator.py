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


class GPUSlowdownSimulator(base_simulator.BaseSimulator):
    """
    Simulates GPU slowdowns in a distributed training environment.

    This class simulates GPU slowdowns by imposing a power limit on individual GPUs
    based on a given Mean Time Between Failures (MTBF). It uses a Poisson distribution
    to model the slowdown probability.
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

        logging.info("Initializing GPU slowdown simulator.")
        self._rng = np.random.default_rng(seed=self.seed)
        self._logger = None
        self._slow_gpus = set()

        # Initialize Google Cloud Logging client
        if gcloud_logging_client is not None:
            self._logging_client = gcloud_logging_client
            self._logger = self._logging_client.logger("gpu-slowdown-simulator")

    def _gpu_slowdown_fn(self, local_ranks: list[int], gpu_power_limit: int = 200):
        """Slows down the GPUs on specified local ranks.

        Args:
            local_ranks (list[int]): The ranks of GPUs to be slowed.
        """

        logging.info(f"Slowing down GPUs with local ranks: {local_ranks}.")

        nsenter_prefix = "nsenter -at 1 --"
        local_ranks_str = ",".join([str(rank) for rank in local_ranks])
        slow_gpu_cmd = f"/home/kubernetes/bin/nvidia/bin/nvidia-smi -pl {gpu_power_limit} -i {local_ranks_str}"

        result = subprocess.run(
            nsenter_prefix.split() + slow_gpu_cmd.split(),
            capture_output=True,
            shell=False,
            text=True,
        )

        if result.returncode != 0:
            logging.warning(f"Command {slow_gpu_cmd} failed with {result.stdout}.")
        else:
            logging.info(f"Command {slow_gpu_cmd} succeeded.")

        for rank in local_ranks:
            self._slow_gpus.add(rank)

    def _gpu_reset_fn(self, local_ranks: list[int] | None = None):
        """Removes the slowdowns from the GPUs on specified local ranks.

        Args:
            local_ranks (list[int]): The ranks of GPUs to be slowed.
        """

        logging.info(
            f"Resetting GPU slowdowns on GPUs with local ranks: {local_ranks}."
        )

        nsenter_prefix = "nsenter -at 1 --"

        if local_ranks is not None:
            local_ranks = ",".join([str(rank) for rank in local_ranks])
            reset_gpu_cmd = (
                f"/home/kubernetes/bin/nvidia/bin/nvidia-smi -pl 700 -i {local_ranks}"
            )
        else:
            reset_gpu_cmd = "/home/kubernetes/bin/nvidia/bin/nvidia-smi -pl 700"

        result = subprocess.run(
            nsenter_prefix.split() + reset_gpu_cmd.split(),
            capture_output=True,
            shell=False,
            text=True,
        )

        if result.returncode != 0:
            logging.warning(f"Command {reset_gpu_cmd} failed with {result.stdout}.")
        else:
            logging.info(f"Command {reset_gpu_cmd} succeeded.")

        if local_ranks is not None:
            for rank in local_ranks:
                if rank in self._slow_gpus:
                    self._slow_gpus.remove(rank)
        else:
            self._slow_gpus.clear()

    @property
    def distribution(self) -> typing.Callable:
        """
        Returns the probability distribution used for sampling slowdowns.

        Returns:
            Callable: The numpy Generator Poisson distribution function.
        """
        return self._rng.poisson

    def sample(self, lambda_value: float) -> np.ndarray[bool]:
        """
        Samples for GPU slowdowns based on the Poisson distribution.

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
        intermittent: bool = False,
        gpu_power_limit: int = 200,
        run_async: bool = False,
        mutex: _thread.LockType | None = None,
    ):
        """
        Starts the slowdown simulation loop.

        This method continuously samples for slowdowns and simulates them by killing
        the corresponding processes running on the failed GPUs. It runs until a
        termination file is detected.

        Args:
            mtbf (float): The Mean Time Between Failures (MTBF) in years.
            sample_interval (int): The interval in seconds between samples.
            intermittent (bool): Allows for slow GPUs to recover if they are re-sampled. Defaults to False.
            run_async (bool): Whether to run the simulation asynchronously. Defaults to False.
            mutex (LockType): Optional mutex to synchronize multiple simulatenous simulators. Defaults to None.

        Raises:
            ValueError: If the GPU power limit is not between 100W and 700W.
        """
        mtbf_s = mtbf * 365 * 24 * 3600
        lambda_value = (1 / mtbf_s) * sample_interval
        mutex = mutex if mutex is not None else contextlib.nullcontext()

        if gpu_power_limit > 700 or gpu_power_limit < 100:
            raise ValueError("GPU power limit must be between 100W and 700W.")

        logging.info(
            f"Starting simulation loop with MTBF: {mtbf} years and sample interval: {sample_interval} seconds."
        )

        def simulate_loop():
            while not utils.check_termination_file():
                slowdown_events = self.sample(lambda_value)
                if slowdown_events.any():
                    with mutex:
                        slowdown_ranks = np.where(slowdown_events)[0].tolist()
                        global_ranks = self.local_to_global_ranks(slowdown_ranks)
                        self.induce_event(
                            global_ranks,
                            intermittent=intermittent,
                            gpu_power_limit=gpu_power_limit,
                        )
                        self.report_events(global_ranks)

                time.sleep(sample_interval)

        if run_async:
            thread = threading.Thread(target=simulate_loop, name="slowdown_simulator")
            thread.start()
        else:
            simulate_loop()

        logging.info("Terminating slowdown simulator.")
        self._gpu_reset_fn()

    def induce_event(
        self,
        global_ranks: list[int],
        intermittent: bool = False,
        gpu_power_limit: int = 200,
    ):
        """
        Simulates GPU slowdowns by killing processes running on the failed GPUs.

        Args:
            global_ranks (list[int]): A list indicating the global ranks of which GPUs have failed.
            intermittent (bool): Allows for slow GPUs to recover if they are re-sampled. Defaults to False.

        Raises:
            ValueError: If the GPU power limit is not between 100W and 700W.
        """
        if len(global_ranks) == 0:
            return

        if gpu_power_limit > 700 or gpu_power_limit < 100:
            raise ValueError("GPU power limit must be between 100W and 700W.")

        logging.info(
            f"Simulating slowdowns on GPUs: {global_ranks} with power: {gpu_power_limit}W."
        )

        # Only induce events on GPUs within the current VM
        global_ranks = self.filter_global_ranks(global_ranks)
        local_ranks = self.global_to_local_ranks(global_ranks)

        if intermittent:
            local_ranks_to_reset = [
                rank for rank in local_ranks if rank in self._slow_gpus
            ]
            if len(local_ranks_to_reset) > 0:
                self._gpu_reset_fn(local_ranks_to_reset)

        local_ranks_to_slow = [
            rank for rank in local_ranks if rank not in self._slow_gpus
        ]
        if len(local_ranks_to_slow) > 0:
            self._gpu_slowdown_fn(local_ranks_to_slow, gpu_power_limit)

        logging.info(f"Slow GPUs: {self._slow_gpus}")

    def report_events(self, global_ranks: list[int]):
        """
        Reports the slowdown event to the console and Google Cloud Logging.

        Args:
            global_ranks (list): A list indicating the global ranks of which GPUs have failed.
        """
        if len(global_ranks) == 0:
            return

        global_ranks = self.filter_global_ranks(global_ranks)
        message = f"GPU slowdown simulated on GPUs: {global_ranks}"
        logging.warning(message)

        if self._logger is not None:
            self._logger.log_struct({"message": message, "severity": "WARNING"})
