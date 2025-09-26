import os
import time
import torch
import logging
import concurrent

from adaptr.src.client.python.host import Host
import adaptr_core


def send_ckpt(
    host: Host,
    host_info: adaptr_core.HostInfo,
    peer_host_info: adaptr_core.HostInfo,
    new_num_hosts: int,
    master_addr: str,
    **kwargs,
) -> None:
    """Callback to send checkpoint to peer

    Args:
        host (Host): Host object.
        host_info (adaptr_core.HostInfo): Host information.
        peer_host_info (adaptr_core.HostInfo): Peer host information.
        new_num_hosts (int): Updated number of hosts participating in training.
        master_addr (str): Updated torch master address.
    """
    logging.info(f"{host.host_name}: Executing send_ckpt callback")

    # Set MASTER_ADDR environment variable
    os.environ["MASTER_ADDR"] = master_addr

    # Initialize distributed process group
    torch.distributed.init_process_group(
        backend="gloo",
        rank=host_info.host_rank,
        world_size=new_num_hosts,
    )
    num_workers = torch.cuda.device_count()
    ckpt_keys = [
        f"ckpt_host_{host.host_name}_localrank_{i}" for i in range(num_workers)
    ]

    # Gather checkpoint objects
    start = time.time()
    ckpts = []
    use_backup = [None] * num_workers
    for i, ckpt_key in enumerate(ckpt_keys):
        if host.redis_client.exists(ckpt_key + "_backup"):
            use_backup[i] = True
        elif host.redis_client.exists(ckpt_key):
            use_backup[i] = False
        else:
            raise RuntimeError("Checkpoint not found in Redis")
    logging.info(f"Took {(time.time() - start):.2f} seconds to check for checkpoints")
    # We cannot load a mixture of backup and non-backup checkpoints
    if not all(use_backup) and any(use_backup):
        raise RuntimeError("Inconsistent checkpoint state")

    def get_ckpt():
        """Helper function to get checkpoint from Redis"""
        if use_backup[0]:
            return host.redis_client.get(ckpt_key + "_backup")
        else:
            return host.redis_client.get(ckpt_key)

    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        # Submit each Redis `get` operation to the executor
        for i, ckpt_key in enumerate(ckpt_keys):
            futures.append(executor.submit(get_ckpt))

        # Collect the results
        ckpts = [future.result() for future in concurrent.futures.as_completed(futures)]
    if len(ckpts) != num_workers:
        raise RuntimeError("Invalid number of checkpoint objects")
    logging.info(f"Took {(time.time() - start):.2f} seconds to load all checkpoints")
    start = time.time()
    # Add metadata to checkpoint objects on whether to use backups
    ckpts.insert(0, use_backup[0])

    # Send checkpoint objects
    logging.info("Sending checkpoint to peer")
    torch.distributed.send_object_list(ckpts, peer_host_info.host_rank)
    logging.info(f"Took {(time.time() - start):.2f} seconds to send checkpoints")
    start = time.time()

    torch.distributed.barrier()
    logging.info(f"Took {(time.time() - start):.2f} seconds to pass barrier")
    torch.distributed.destroy_process_group()
    logging.info(f"{host.host_name}: Send checkpoint callback completed")


def recv_ckpt(
    host: Host,
    host_info: adaptr_core.HostInfo,
    peer_host_info: adaptr_core.HostInfo,
    new_num_hosts: int,
    master_addr: str,
    **kwargs,
) -> None:
    """Callback to receive checkpoint from peer

    Args:
        host (Host): Host object.
        host_info (adaptr_core.HostInfo): Host information.
        peer_host_info (adaptr_core.HostInfo): Peer host information.
        new_num_hosts (int): Updated number of hosts participating in training.
        master_addr (str): Updated torch master address.
    """
    logging.info(f"{host.host_name}: Executing recv_ckpt callback")

    # Set MASTER_ADDR environment variable
    os.environ["MASTER_ADDR"] = master_addr

    # Initialize distributed process group
    torch.distributed.init_process_group(
        backend="gloo",
        rank=host_info.host_rank,
        world_size=new_num_hosts,
    )
    num_workers = torch.cuda.device_count()
    ckpt_keys = [
        f"ckpt_host_{host.host_name}_localrank_{i}" for i in range(num_workers)
    ]
    ckpts = [None] * (num_workers + 1)

    # Receive checkpoint objects
    logging.info("Receiving checkpoint from peer")
    start = time.time()
    torch.distributed.recv_object_list(ckpts, peer_host_info.host_rank)
    logging.info(f"Took {(time.time() - start):.2f} seconds to receive checkpoints")
    start = time.time()

    use_backup = ckpts[0]

    # Save checkpoint objects to Redis
    for ckpt_key, ckpt in zip(ckpt_keys, ckpts[1:]):
        if use_backup:
            ckpt_key += "_backup"
        host.redis_client.set(ckpt_key, ckpt)
        logging.info(f"Checkpoint {ckpt_key} saved in Redis")
    logging.info(f"Took {(time.time() - start):.2f} seconds to save checkpoints")
    torch.distributed.barrier()
    logging.info(f"Took {(time.time() - start):.2f} seconds to pass barrier")
    torch.distributed.destroy_process_group()
    logging.info(f"{host.host_name}: Recv checkpoint callback completed")


def no_op_ckpt(
    host: Host,
    host_info: adaptr_core.HostInfo,
    peer_host_info: adaptr_core.HostInfo,
    new_num_hosts: int,
    master_addr: str,
    **kwargs,
) -> None:
    """Callback for hosts not participating in syncing state. This is essentially a no-op, however these processes still have to participate in creating the distributed process group.

    Args:
        host (Host): Host object.
        host_info (adaptr_core.HostInfo): Host information.
        peer_host_info (adaptr_core.HostInfo): Peer host information.
        new_num_hosts (int): Updated number of hosts participating in training.
        master_addr (str): Updated torch master address.
    """
    logging.info(f"{host.host_name}: Executing no_op_ckpt callback")

    # Set MASTER_ADDR environment variable
    os.environ["MASTER_ADDR"] = master_addr

    torch.distributed.init_process_group(
        backend="gloo",
        rank=host_info.host_rank,
        world_size=new_num_hosts,
    )

    torch.distributed.barrier()
    torch.distributed.destroy_process_group()
    logging.info(f"{host.host_name}: No-op checkpoint callback completed")
