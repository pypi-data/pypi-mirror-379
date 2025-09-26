import logging
import os

import adaptr_core
from adaptr.src.client.python import worker


def stop(
    worker: worker.Worker,
    host_info: adaptr_core.HostInfo,
):
    """Callback definition for GPU training stop.

    Args:
        host (host.Host): Reference to the host.
        host_info (adaptr_core.HostInfo): New host information for the host.
        peer_host_info (adaptr_core.WorkerInfo): New host information on a peer. This argument is not used for this callback.
    """
    logging.info(f"{worker.worker_name}: Executing stop callback")

    # Exit training loop
    logging.info(f"{worker.worker_name}: Stopping training")
    worker.stop_workload()


def start(
    worker: worker.Worker,
    host_info: adaptr_core.HostInfo,
    master_addr: str,
    new_world_size: int,
):
    """Callback definition for GPU training start.

    Args:
        host (host.Host): Reference to the host.
        host_info (adaptr_core.HostInfo): New host information for the host.
        peer_host_info (adaptr_core.WorkerInfo): New host information on a peer. This argument is not used for this callback.
        master_addr (str): Master address for PyTorch.
        new_world_size (int): New world size for PyTorch.
    """
    logging.info(f"{worker.worker_name}: Executing start callback")

    worker_info = [
        w for w in host_info.workers if w.worker_name == worker.worker_name
    ].pop()

    # Update environment variables
    os.environ["MASTER_ADDR"] = master_addr
    os.environ["WORLD_SIZE"] = str(new_world_size)

    # Update worker attributes
    worker.update_info(worker_info=worker_info)

    # start training loop
    logging.info(f"{worker.worker_name}: Starting training")
    worker.start_workload(func=worker.workload_func)
