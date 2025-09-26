"""Mesh class for Adaptr."""

from adaptr.src.core.python.device_info import HostInfo, WorkerInfo, DeviceState


class Mesh:
    """Defines physical and virtual mesh of training job.
    This class is primarily used by elastic strategies and optimizer
    to understand training topology and keep it up-to-date as capacity fluctuates.
    """

    def __init__(
        self,
        dimensions: dict[str, int],
        all_parallel_groups: dict[str, list[list[int]]] = None,
    ):
        """Initializes the mesh.

        Args:
          dimensions (dict[str, int]): dictionary of dimensions of the mesh.
          all_parallel_groups (dict[str, list[list[int]]], optional): dictionary of parallel groups in the mesh.
        """

        # Dictionaries to track physical mapping
        # Maps worker_id to WorkerInfo
        self.physical_worker_map = {}
        # Maps host_id to HostInfo
        self.physical_host_map = {}

        # Dictionary to track virtual mapping
        # Map for rank to worker. This dictionary should only track running ranks.
        self.virtual_mesh_rank_to_worker = {}

        # Map for coords -> worker
        # Coordinates are fixed, meaning that no new coordinates are added after initialization.
        # This map is only updated when a new worker replaces an old worker,
        # allowing this class to track the old location of non-running workers.
        self.virtual_mesh_coords_to_worker = {}

        # Defining virtual shape
        if (all_parallel_groups is not None) and (
            dimensions.keys() != all_parallel_groups.keys()
        ):
            raise RuntimeError(
                "All dimensions must have corresponding parallel groups defined."
            )
        self.virtual_mesh_dimensions = dimensions
        self.virtual_parallel_groups = all_parallel_groups

        # Track number of hosts and workers runningly used in training
        self.running_host_count = 0
        self.running_worker_count = 0

    ##### Virtual mapping utility functions #####
    def get_running_workers_count(self) -> int:
        """Retrieves the number of running workers in the virtual mesh."""
        return self.running_worker_count

    def get_running_hosts_count(self) -> int:
        """Retrieves the number of running hosts in the virtual mesh."""
        return len(
            [host for host in self.get_all_hosts() if host.state == DeviceState.RUNNING]
        )

    def get_num_dimensions(self) -> int:
        """Retrieves the number of dimensions in the virtual mesh."""
        return len(self.virtual_mesh_dimensions)

    def set_worker_from_rank(self, rank: int, worker: WorkerInfo) -> None:
        """Sets the WorkerInfo associated with the given rank.

        Args:
            rank (int): The rank of the worker.
            worker (WorkerInfo): The WorkerInfo to associate with the rank.
        """
        self.virtual_mesh_rank_to_worker[rank] = worker

    def get_worker_from_rank(self, rank: int) -> WorkerInfo:
        """Retrieves the WorkerInfo associated with the given rank.

        Args:
            rank (int): The rank of the worker.

        Returns:
            WorkerInfo: The WorkerInfo associated with the given rank.
        """
        return self.virtual_mesh_rank_to_worker[rank]

    def set_coords_worker_mapping(self, worker: WorkerInfo) -> None:
        """Sets Mesh's virtual mapping to map worker's coords of the worker.
        This overwrites the previous mapping if applicable.

        Args:
            worker (WorkerInfo): The WorkerInfo object.
        """
        coords = worker.coords
        if len(coords) != len(self.virtual_mesh_dimensions):
            raise RuntimeError(
                "Worker's coordinates must match the number of dimensions in the virtual mesh."
            )
        # Overwrite/add new coords -> worker mapping
        self.virtual_mesh_coords_to_worker[coords] = worker

    def get_all_parallel_groups(self) -> dict[str, list[list[int]]]:
        """Retrieves all parallel groups in the virtual mesh.

        Returns:
            dict[str, list[list[int]]]: The parallel groups in the virtual mesh.
        """
        return self.virtual_parallel_groups

    def set_all_parallel_groups(
        self, all_parallel_groups: dict[str, list[list[int]]]
    ) -> None:
        """Sets all parallel groups in the virtual mesh.

        Args:
            all_parallel_groups (dict[str, list[list[int]]]): The parallel groups to set.
        """
        if all_parallel_groups.keys() != self.virtual_mesh_dimensions.keys():
            raise RuntimeError(
                "All dimensions must have corresponding parallel groups defined."
            )
        self.virtual_parallel_groups = all_parallel_groups

    def get_worker_from_coords(self, coords: tuple[int, ...]) -> WorkerInfo:
        """Retrieves the WorkerInfo object associated with the given coordinates.

        Args:
            coords (tuple[int, ...]): The coordinates of the worker in the virtual mesh.

        Returns:
            WorkerInfo: The WorkerInfo object associated with the given coordinates.
        """
        return self.virtual_mesh_coords_to_worker[coords]

    ##### Physical mapping utility functions #####
    def get_num_physical_hosts(self) -> int:
        """Retrieves the number of physical hosts in the mesh."""
        return len(self.physical_host_map)

    def get_num_physical_workers(self) -> int:
        """Retrieves the number of physical workers in the mesh."""
        return len(self.physical_worker_map)

    def get_worker(self, worker_id: str) -> WorkerInfo:
        """
        Retrieves a WorkerInfo object based on the provided worker ID.

        Args:
            worker_id (str): The ID of the worker to retrieve.

        Returns:
            WorkerInfo: The WorkerInfo object corresponding to the provided worker ID.
        """
        return self.physical_worker_map[worker_id]

    def get_host(self, host_id: str) -> HostInfo:
        """
        Retrieve a HostInfo object based on the provided host ID.

        Args:
            host_id (str): The ID of the host to retrieve.

        Returns:
            HostInfo: The HostInfo object corresponding to the provided host ID.
        """
        return self.physical_host_map[host_id]

    def get_all_workers(self) -> list[WorkerInfo]:
        """Retrieves all workers in the mesh."""
        return list(self.physical_worker_map.values())

    def get_all_hosts(self) -> list[HostInfo]:
        """Retrieves all hosts in the mesh."""
        return list(self.physical_host_map.values())

    ##### Physical mapping setup/update functions #####
    def add_physical_worker_info(self, worker: WorkerInfo) -> None:
        """Adds a physical worker info to the mesh.

        Args:
            worker (WorkerInfo): The physical worker info to be added.
        """
        self.physical_worker_map[worker.worker_id] = worker
        # If worker has a global rank upon initialization, it's state will be changed to RUNNING.
        # This will also change the state of the worker's host to RUNNING if it is not already RUNNING.
        if worker.global_rank not in [None, -1]:
            self.add_virtual_worker_info(worker)

    def remove_physical_worker_info(self, worker_id: str) -> None:
        """Removes a physical worker info from the mesh.

        Args:
            worker_id (str): The ID of the physical worker info to be removed.
        """
        worker_to_remove = self.physical_worker_map.pop(worker_id)
        self.remove_virtual_worker_info(worker_to_remove)

    def add_physical_host_info(self, new_host: HostInfo) -> None:
        """Adds a physical host info to the mesh.

        Args:
            host (HostInfo): The physical host info to be added.
        """

        self.physical_host_map[new_host.host_id] = new_host
        for worker in new_host.workers:
            self.add_physical_worker_info(worker)

    def remove_physical_host_info(self, host_id: str) -> None:
        """Removes a physical host info from the mesh.

        Args:
            host_id (str): The ID of the physical host info to be removed.
        """
        host_to_remove = self.get_host(host_id)
        self.physical_host_map.pop(host_id)
        for worker in host_to_remove.workers:
            self.remove_physical_worker_info(worker.worker_id)

    def replace_physical_host_info(
        self,
        old_host: HostInfo,
        new_host: HostInfo,
    ) -> None:
        """Replaces a physical host info with a new host.

        Args:
            old_host (HostInfo): The old physical host info to be replaced.
            new_host (HostInfo): The new physical host info to replace the old host.
        """
        # Iterate through each set of workers to update virtual attributes
        for new_worker, old_worker in zip(new_host.workers, old_host.workers):
            # Update ranks
            new_worker.global_rank = old_worker.global_rank
            # Update virtual coordinate mapping
            coords = old_worker.coords
            new_worker.coords = coords
            self.set_coords_worker_mapping(new_worker)

        # Remove new host to physical mesh
        self.remove_physical_host_info(old_host.host_id)

        # Add new host to physical mesh
        self.add_physical_host_info(new_host)

    ##### Virtual mapping setup/update functions #####
    def ready_to_use(self) -> bool:
        """Checks if the Mesh is ready to use or still needs to be setup."""
        # Physical mapping checks
        num_workers = 0
        for host in self.get_all_hosts():
            for worker in host.workers:
                if worker.worker_id not in self.physical_worker_map:
                    return False
                num_workers += 1
        if num_workers != self.get_num_physical_workers():
            return False

        # Virtual mapping checks
        running_worker_count = 0
        expected_ranks = list(range(self.running_worker_count))
        for worker in self.get_all_workers():
            # Check that running workers have set ranks and coords
            if worker.state == DeviceState.RUNNING:
                running_worker_count += 1
                if worker.global_rank is None:
                    return False
                if worker.coords is None:
                    return False
                if worker.global_rank not in self.virtual_mesh_rank_to_worker:
                    return False
                if worker.coords not in self.virtual_mesh_coords_to_worker:
                    return False
                if worker.global_rank in expected_ranks:
                    expected_ranks.remove(worker.global_rank)
            else:
                if worker.global_rank is not None or worker.global_rank is not None:
                    raise RuntimeError(
                        f"Worker {worker.worker_id} is not running but has a rank assigned."
                    )

        # Check if ranks are up-to-date with number of running workers
        if len(expected_ranks) != 0:
            return False
        # Check that there is at least 1 running worker,
        if running_worker_count == 0:
            return False
        # Check that the number of running workers match the Mesh's count
        if running_worker_count != self.running_worker_count:
            raise RuntimeError(
                f"Running worker count {running_worker_count} does not match Mesh's running worker count {self.running_worker_count}."
            )

        # Check that the number of running hosts match the Mesh's count
        # running_host_count = len(
        #     [host for host in self.get_all_hosts() if host.state == DeviceState.RUNNING]
        # )
        # if self.running_host_count != running_host_count:
        #     raise RuntimeError(
        #         f"Active host count {self.running_host_count} does not match Mesh's running host count {running_host_count}."
        #     )
        return True

    def add_virtual_worker_info(self, worker: WorkerInfo) -> None:
        """Adds a virtual worker's global rank mapping

        Args:
            worker (WorkerInfo): The virtual worker info to be added.
        """
        if worker.global_rank is not None:
            self.set_worker_from_rank(worker.global_rank, worker)

        worker.state = DeviceState.RUNNING

        if worker.coords is not None:
            self.set_coords_worker_mapping(worker)

        # Update running host and worker counts
        self.running_worker_count += 1
        if worker.host is not None and worker.host.state != DeviceState.RUNNING:
            worker.host.state = DeviceState.RUNNING
            self.running_host_count += 1

    def remove_virtual_worker_info(self, worker: WorkerInfo) -> None:
        """Removes a virtual worker's global rank mapping

        Args:
            worker (WorkerInfo): The virtual worker info to be removed.
        """
        # Remove rank -> worker mapping
        if worker.global_rank is not None:
            self.virtual_mesh_rank_to_worker.pop(worker.global_rank)

        # Upddate running host and worker counts
        if worker.state == DeviceState.RUNNING:
            worker.state = DeviceState.SPARE
            self.running_worker_count -= 1

        if (
            worker.host.state == DeviceState.RUNNING
            and worker.host.get_num_workers() == 0
        ):
            num_available_workers = len(
                [
                    worker
                    for worker in worker.host.workers
                    if worker.state == DeviceState.SPARE
                ]
            )
            if num_available_workers > 0:
                worker.host.state = DeviceState.SPARE
            else:
                worker.host.state = DeviceState.FAILED
            self.running_host_count -= 1

        # Unassign worker's global rank
        worker.global_rank = None
        worker.local_rank = None

    def update_virtual_host_info(
        self, host_id: str, new_state: DeviceState = None, new_host_rank: int = None
    ) -> None:
        """Updates the virtual host info with a new state.

        Args:
            host_id (str): The ID of the host to update.
            new_state (DeviceState): The new state for the host.
            new_host_rank (int): The new rank for the host.
        """
        mesh_host = self.get_host(host_id)

        # Update state
        if new_state is not None:
            if mesh_host.state != new_state:
                if (
                    mesh_host.state != DeviceState.RUNNING
                    and new_state == DeviceState.RUNNING
                ):
                    self.running_host_count += 1
                elif (
                    mesh_host.state == DeviceState.RUNNING
                    and new_state != DeviceState.RUNNING
                ):
                    self.running_host_count -= 1
                mesh_host.state = new_state

    def update_virtual_worker_info(
        self,
        worker_id: str,
        new_state: DeviceState = None,
        new_global_rank: int = None,
        new_local_rank: int = None,
    ) -> None:
        """Updates the virtual worker info with a new rank.

        Args:
            worker_id (str): The ID of the worker to update.
            new_state (DeviceState): The new state for the worker.
            new_global_rank (int): The new global rank for the worker.
            new_local_rank (int): The new local rank for the worker.
        """
        mesh_worker = self.get_worker(worker_id)

        # Update state
        if new_state is not None:
            if mesh_worker.state != new_state:
                # Update running worker count if needed
                if (
                    mesh_worker.state != DeviceState.RUNNING
                    and new_state == DeviceState.RUNNING
                ):
                    self.running_worker_count += 1
                elif (
                    mesh_worker.state == DeviceState.RUNNING
                    and new_state != DeviceState.RUNNING
                ):
                    self.running_worker_count -= 1
                mesh_worker.state = new_state

                # Update host state and running host count if needed
                host = mesh_worker.host
                if host is not None:
                    if (
                        host.state != DeviceState.RUNNING
                        and new_state == DeviceState.RUNNING
                    ):
                        host.state = DeviceState.RUNNING
                        self.running_host_count += 1
                    elif (
                        host.state == DeviceState.RUNNING
                        and host.get_num_workers() == 0
                    ):
                        num_available_workers = len(
                            [
                                worker
                                for worker in host.workers
                                if worker.state == DeviceState.SPARE
                            ]
                        )
                        if num_available_workers > 0:
                            host.state = DeviceState.SPARE
                        else:
                            host.state = DeviceState.FAILED
                        self.running_host_count -= 1

        # Update global rank
        if new_global_rank is not None and mesh_worker.global_rank != new_global_rank:
            if new_global_rank in self.virtual_mesh_rank_to_worker:
                raise RuntimeError(
                    f"Global rank {new_global_rank} already exists in the virtual mesh."
                )
            self.virtual_mesh_rank_to_worker.pop(mesh_worker.global_rank)
            mesh_worker.global_rank = new_global_rank
            self.set_worker_from_rank(new_global_rank, mesh_worker)

        # Update local rank
        if new_local_rank is not None:
            mesh_worker.local_rank = new_local_rank

    def generate_coords(self):
        """Generate coordinates for all workers in the virtual mesh."""
        if self.virtual_parallel_groups is None:
            raise RuntimeError(
                "All parallel groups must be defined before generating coordinates."
            )
        for key in self.virtual_parallel_groups.keys():
            self.ingest_all_groups_in_dim(key, self.virtual_parallel_groups[key])

    def ingest_group_in_dim(self, dim: str, group: list[int]) -> None:
        """Ingests a group of ranks in a given dim.

        Args:
          dim (str): string representing the dimension
          group (list[int]): list of ranks in the dim
        """
        if dim not in self.virtual_mesh_dimensions:
            raise RuntimeError(f"Dimension {dim} not found in virtual mesh dimensions.")
        if len(group) != self.virtual_mesh_dimensions[dim]:
            raise RuntimeError(
                f"Group size {len(group)} does not match dimension size {self.virtual_mesh_dimensions[dim]}."
            )

        dim_index = list(self.virtual_mesh_dimensions.keys()).index(dim)

        # Iterate through each element in group
        for group_index, rank in enumerate(group):
            if rank not in self.virtual_mesh_rank_to_worker:
                raise RuntimeError(
                    f"Rank {rank} not found in virtual mesh ranks: {self.virtual_mesh_rank_to_worker}."
                )
            worker = self.virtual_mesh_rank_to_worker[rank]

            # Define worker coords as tuple filled with None for each dimension
            if worker.coords is None:
                coords = [None] * len(self.virtual_mesh_dimensions)
                worker.coords = tuple(coords)

            # Verify that we are not updating a coordinate already set
            if worker.coords[dim_index] is not None:
                raise RuntimeError(
                    f"Worker {worker.worker_id} already has a coordinate in dimension {dim}. This should not happen."
                )
            updated_coords = list(worker.coords)
            updated_coords[dim_index] = group_index
            worker.coords = tuple(updated_coords)

            # Add coords -> worker mapping if coords is fully defined (i.e. does not contain None)
            if updated_coords.count(None) == 0:
                self.virtual_mesh_coords_to_worker[tuple(updated_coords)] = worker

    def ingest_all_groups_in_dim(self, dim: str, all_groups: list[list[int]]) -> None:
        """Ingests all groups of ranks in a given dim.

        Args:
          dim (str): string representing the dim
          all_groups (list[list[int]]): list of lists of ranks in the dim
        """
        for group in all_groups:
            self.ingest_group_in_dim(dim, group)

    def update_rank_mapping(self) -> None:
        """Updates the rank mapping based on the virtual worker to coords mapping.
        This function is the recommended method for updating rank mappings and
        should only be called once all Physical Workers have up-to-date ranks as previous rank mappings are wiped.
        """
        self.virtual_mesh_rank_to_worker = {}
        for worker in self.get_all_workers():
            self.set_worker_from_rank(worker.global_rank, worker)
