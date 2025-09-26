import adaptr.src.core.python.device_info as device_info
import adaptr.src.core.python.mesh as mesh
import logging
import re
from typing import Any


def is_set(value):
    """Check if a value is set.

    Args:
        value: The value to check.

    Returns:
        bool: True if the value is set, False otherwise.
    """
    return value is not None and value != -1


def compare_workers(
    worker_info1: device_info.WorkerInfo,
    worker_info2: device_info.WorkerInfo,
    compare_coords=False,
) -> bool:
    """Compares two workers based on their attributes.

    Args:
        worker_info1 (device_info.WorkerInfo): The first worker to compare.
        worker_info2 (device_info.WorkerInfo): The second worker to compare.
        compare_coords (bool): Whether to compare the coordinates of the workers.

    Returns:
        bool: True if the workers have the same attribute values, False otherwise.
    """
    # TODO: Add this comparison directly to the WorkerInfo class

    if not isinstance(worker_info1, device_info.WorkerInfo) or not isinstance(
        worker_info2, device_info.WorkerInfo
    ):
        raise ValueError("worker_info objects must be of type device_info.WorkerInfo.")

    if worker_info1.worker_id != worker_info2.worker_id:
        logging.info(
            f"WorkerInfo IDs do not match: {worker_info1.worker_id} and {worker_info2.worker_id}"
        )
        return False
    if worker_info1.worker_name != worker_info2.worker_name:
        logging.info(
            f"WorkerInfo names do not match: {worker_info1.worker_name} and {worker_info2.worker_name}"
        )
        return False
    if worker_info1.local_rank != worker_info2.local_rank:
        if is_set(worker_info1.local_rank) != is_set(worker_info2.local_rank):
            logging.info(
                f"WorkerInfo local ranks do not match: {worker_info1.local_rank} and {worker_info2.local_rank}"
            )
            return False
    if worker_info1.global_rank != worker_info2.global_rank:
        if is_set(worker_info1.global_rank) != is_set(worker_info2.global_rank):
            logging.info(
                f"WorkerInfo global ranks do not match: {worker_info1.global_rank} and {worker_info2.global_rank}"
            )
            return False
    if worker_info1.state.name != worker_info2.state.name:
        logging.info(
            f"WorkerInfo states do not match: {worker_info1.state} and {worker_info2.state}"
        )
        return False

    if compare_coords:
        if worker_info1.coords != worker_info2.coords:
            logging.info(
                f"WorkerInfo coords do not match: {worker_info1.coords} and {worker_info2.coords}"
            )
            return False

    return True


def compare_hosts(
    host_info1: device_info.HostInfo,
    host_info2: device_info.HostInfo,
    compare_coords=False,
) -> bool:
    """Compares two hosts based on their attributes.

    Args:
        host_info1 (HostInfo): The first host to compare.
        host_info2 (HostInfo): The second host to compare.
        compare_coords (bool): Whether to compare the coordinates of the workers.

    Returns:
        bool: True if the hosts have the same attribute values, False otherwise.
    """
    if not isinstance(host_info1, device_info.HostInfo) or not isinstance(
        host_info2, device_info.HostInfo
    ):
        raise ValueError("host_info objects must be of type device_info.HostInfo.")

    if host_info1.host_address != host_info2.host_address:
        logging.info(
            f"HostInfo addresses do not match: {host_info1.host_address} and {host_info2.host_address}"
        )
        return False
    if host_info1.host_id != host_info2.host_id:
        logging.info(
            f"HostInfo IDs do not match: {host_info1.host_id} and {host_info2.host_id}"
        )
        return False
    if host_info1.host_name != host_info2.host_name:
        logging.info(
            f"HostInfo names do not match: {host_info1.host_name} and {host_info2.host_name}"
        )
        return False
    if host_info1.host_serial_number != host_info2.host_serial_number:
        logging.info(
            f"HostInfo serial numbers do not match: {host_info1.host_serial_number} and {host_info2.host_serial_number}"
        )
        return False
    if host_info1.subblock_id != host_info2.subblock_id:
        logging.info(
            f"HostInfo subblock IDs do not match: {host_info1.subblock_id} and {host_info2.subblock_id}"
        )
        return False
    if host_info1.superblock_id != host_info2.superblock_id:
        logging.info(
            f"HostInfo superblock IDs do not match: {host_info1.superblock_id} and {host_info2.superblock_id}"
        )
        return False
    if host_info1.zone != host_info2.zone:
        logging.info(
            f"HostInfo zones do not match: {host_info1.zone} and {host_info2.zone}"
        )
        return False
    if host_info1.state.name != host_info2.state.name:
        logging.info(
            f"HostInfo states do not match: {host_info1.state} and {host_info2.state}"
        )
        return False
    if len(host_info1.workers) != len(host_info2.workers):
        logging.info(
            f"HostInfo has different number of workers: {len(host_info1.workers)} and {len(host_info2.workers)}"
        )
        return False

    for worker1, worker2 in zip(
        sorted(host_info1.workers, key=lambda x: x.global_rank),
        sorted(host_info2.workers, key=lambda x: x.global_rank),
    ):
        if not compare_workers(worker1, worker2, compare_coords):
            return False
    return True


def get_torch_master_address(mesh: mesh.Mesh) -> str:
    """Get address to set as `MASTER_ADDR`

    Returns:
        str: The address of the torch master address.
    """
    return mesh.get_worker_from_rank(0).host.host_address.split(":")[0]


def destringify_kwargs(string_kwargs: str | None) -> dict[str, Any]:
    """Convert kwargs in string format to usable dictionary.

    Args:
        string_kwargs: The string containing comma separated kwargs with format 'KEY=VALUE'.

    Returns:
        dict: The dictionary representation of the kwargs.
    """

    def is_digit(string):
        return bool(re.match(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)", string))

    result = {}
    if string_kwargs is None or len(string_kwargs) == 0:
        return result

    kwargs = string_kwargs.split(",")
    for kwarg in kwargs:
        key, value = kwarg.split("=")
        if is_digit(value):
            try:
                value = int(value)
            except ValueError:
                value = float(value)
        result[key] = value

    return result
