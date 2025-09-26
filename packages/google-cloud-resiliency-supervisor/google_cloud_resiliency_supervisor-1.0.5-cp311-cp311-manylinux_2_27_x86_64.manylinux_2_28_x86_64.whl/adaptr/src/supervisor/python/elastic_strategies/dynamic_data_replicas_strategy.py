from collections import Counter, defaultdict
import copy

from adaptr.src.supervisor.python.elastic_strategies.base_strategy import (
    BaseStrategy,
    ScaleDirection,
)

from adaptr.src.core.python.mesh import Mesh
from adaptr.src.core.python.device_info import DeviceState, HostInfo
from adaptr.src.core.python.utils import get_torch_master_address

import adaptr_core
import logging


class DynamicDataReplicasStrategy(BaseStrategy):
    """
    DynamicDataReplicaStrategy is an elastic strategy that adjusts the number of data replicas.
    This strategy requires that the number of data replicas > 1.
    When a worker or host fails, this strategy will remove the data replica(s) that contain the failed worker(s) and rely on the remaining data replicas for training.
    When new workers or hosts are added, this strategy can add back data replica groups.
    Existing data replicas can send over their state to new data replicas since each data replica will have the same state.

    TODO:
    - This strategy currently only supports data replica groups that are within a single superblock.
    - This strategy only supports hosts with 8 GPUs.
    - This strategy assumes that maximum number of active workers is the number of workers used when initializing training.
    - This strategy does not support adding multiple data replica groups to a single host at once.
    - When scaling up, this strategy assumes that the number of active data replicas > number of new data replicas.
        This is so a peer host for each new data replica can be identified without having to reference a peer host multiple times
    """

    def __init__(
        self,
        adaptr_mesh: Mesh,
        data_replica_groups: list[int],
        num_workers_in_data_replica: int,
        num_hosts_in_data_replica: int,
    ):
        """Initializes the DynamicDataReplicasStrategy.

        Args:
            adaptr_mesh (Mesh): Mesh object
            data_replica_groups (list[int]): Data replica groups at the beginning of training.
            num_workers_in_data_replica (int): The total number of workers in each data replica. This number should be constant throughout training.
            num_hosts_in_data_replica (int): The total number of hosts in each data replica. This number should be constant throughout training.
        """
        super().__init__(adaptr_mesh, "dynamic_data_replicas")

        self.adaptr_mesh = adaptr_mesh
        self.data_replica_groups = data_replica_groups
        self.num_workers_in_data_replica = num_workers_in_data_replica
        self.num_hosts_in_data_replica = num_hosts_in_data_replica
        self.num_workers_per_host_per_data_replica = (
            num_workers_in_data_replica // num_hosts_in_data_replica
        )

    def deferred_init(
        self,
    ):
        logging.info(f"Deferred initialization for strategy {self.name}.")
        # Check that each data replica group is within a superblock.
        for data_replica_group in self.data_replica_groups:
            superblock_counts = Counter(
                self.adaptr_mesh.get_worker_from_rank(rank).host.superblock_id
                for rank in data_replica_group
            )
            unique_superblock_count = len(superblock_counts)
            if unique_superblock_count > 1:
                raise ValueError(
                    f"Data replica group {data_replica_group} spans multiple superblocks, which is not supported by this strategy."
                )

        # Map coordinates to respective data replica groups.
        self.data_replica_coords_map = defaultdict(list)
        for data_replica_group in self.data_replica_groups:
            # Convert data_replica_group to a list of coordinates.
            data_replica_coord_group = []
            for global_rank in data_replica_group:
                data_replica_coord_group.append(
                    self.adaptr_mesh.get_worker_from_rank(global_rank).coords
                )

            for coord in data_replica_coord_group:
                self.data_replica_coords_map[tuple(coord)] = data_replica_coord_group

        # Store coordinates of active data replicas.
        self.active_data_replica_groups_in_coords_per_superblock = defaultdict(list)
        all_data_replica_groups_in_coords = self.get_all_data_replica_groups_in_coords()
        for data_replica_group_in_coords in all_data_replica_groups_in_coords:
            # Iterate through coords and determine that all workers are in the same superblock.
            superblock_counts = Counter(
                self.adaptr_mesh.get_worker_from_coords(coord).host.superblock_id
                for coord in data_replica_coord_group
            )
            unique_superblock_count = len(superblock_counts)
            if unique_superblock_count > 1:
                raise ValueError(
                    f"Data replica group {data_replica_group_in_coords} spans multiple superblocks, which is not supported by this strategy."
                )
            superblock_id = list(superblock_counts.keys())[0]
            self.active_data_replica_groups_in_coords_per_superblock[
                superblock_id
            ].append(data_replica_group_in_coords)

        # Store coordinates of removed data replicas.
        self.removed_data_replica_groups_in_coords_per_superblock = []

        # Store coordinates of new data replicas.
        self.new_data_replica_groups_in_coords_per_superblock = defaultdict(list)

        # Store number of data replicas that can be added to each superblock.
        self.superblocks_that_can_scale_up = {}

        # Determine how coordinates correspond to ranks.
        # This is helpful for remapping ranks during scale up events.
        all_devices = self.adaptr_mesh.get_all_workers()
        coords_sorting = []
        all_devices.sort(key=lambda x: x.global_rank)
        for device in all_devices:
            coords = device.coords
            for idx, coord in enumerate(coords):
                if coord != 0 and idx not in coords_sorting:
                    coords_sorting.insert(0, idx)
        coords_sorting = tuple(coords_sorting)

        # Define key for how to sort coordinates such that
        # their ranks are in ascending order.
        def sorting_key(coords):
            return tuple(coords[idx] for idx in coords_sorting)

        self.coords_sorting_key = sorting_key

    #### Helper functions ####
    def get_data_replica_coords(self, coords: tuple[int, ...]) -> list[int]:
        """Returns the coords of the data replica group that corresponds to the given coordinates.

        Args:
            coords (tuple(int)): The coordinates of the data replica groups.

        Returns:
            list[int]: The coords of the data replica group.
        """
        return self.data_replica_coords_map[coords]

    def get_all_data_replica_groups_in_coords(self):
        """Returns the coords for all data replica groups."""
        unique_data_replica_groups = set(
            tuple(group) for group in self.data_replica_coords_map.values()
        )
        unique_data_replica_groups = [
            list(group) for group in unique_data_replica_groups
        ]
        return list(unique_data_replica_groups)

    def get_all_active_data_replica_groups_in_coords(
        self, include_new_data_replica_groups=True
    ):
        """Returns the coords for all active data replica groups."""
        all_active_data_replica_groups_in_coords = []
        for (
            _,
            data_replica_groups_in_coords,
        ) in self.active_data_replica_groups_in_coords_per_superblock.items():
            for data_replica_group_in_coords in data_replica_groups_in_coords:
                all_active_data_replica_groups_in_coords.append(
                    data_replica_group_in_coords
                )

        if include_new_data_replica_groups:
            return all_active_data_replica_groups_in_coords

        for new_data_replica_group in self.get_all_new_data_replica_groups_in_coords():
            all_active_data_replica_groups_in_coords.remove(new_data_replica_group)

        return all_active_data_replica_groups_in_coords

    def get_all_removed_data_replica_groups_in_coords(self):
        """Returns the coords for all removed data replica groups."""
        return self.removed_data_replica_groups_in_coords_per_superblock

    def get_all_new_data_replica_groups_in_coords(self):
        """Returns the coords for all new data replica groups."""
        all_new_data_replica_groups_in_coords = []
        for (
            _,
            data_replica_groups_in_coords,
        ) in self.new_data_replica_groups_in_coords_per_superblock.items():
            for data_replica_group_in_coords in data_replica_groups_in_coords:
                all_new_data_replica_groups_in_coords.append(
                    data_replica_group_in_coords
                )
        return all_new_data_replica_groups_in_coords

    def add_target_hosts_to_mesh(
        self, mesh: Mesh, target_hosts: list[HostInfo]
    ) -> Mesh:
        """Adds target hosts to the mesh.

        Args:
            mesh (Mesh): The mesh to add target hosts to.
            target_hosts (list[HostInfo]): List of target hosts to add to the mesh.
        Returns:
            Mesh: The mesh with target hosts added.
        """
        logging.info(f"Add target hosts to mesh for strategy {self.name}.")
        copy_target_hosts = copy.deepcopy(target_hosts)

        # Add target hosts to the mesh.
        for target_host in copy_target_hosts:
            # If target_host is not in the mesh, add it. If it is, update its state.
            if target_host.host_id not in [
                host.host_id for host in mesh.get_all_hosts()
            ]:
                mesh.add_physical_host_info(target_host)
            else:
                mesh.update_virtual_host_info(target_host.host_id, target_host.state)

            # If target_worker is not in the mesh, add it. If it is, update its state.
            for target_worker in target_host.workers.values():
                if target_worker.worker_id not in [
                    worker.worker_id for worker in mesh.get_all_workers()
                ]:
                    mesh.add_physical_worker_info(target_worker)
                    mesh.get_host(target_host.host_id).register_workers([target_worker])
                else:
                    mesh.update_virtual_worker_info(
                        target_worker.worker_id, target_worker.state
                    )
        return mesh

    def cleanup_mesh(self, mesh: Mesh) -> Mesh:
        """Removes all UNAVAILABLE hosts and workers from the mesh

        Args:
            mesh (Mesh): Mesh object to clean.

        Returns:
            Mesh: Cleaned Mesh object.
        """
        logging.info(f"Cleanup mesh for strategy {self.name}.")

        # Iterate through all hosts and workers, removing any that are UNAVAILABLE.
        for host in mesh.get_all_hosts():
            if host.state == DeviceState.UNAVAILABLE:
                mesh.remove_physical_host_info(host.host_id)
            else:
                for worker in list(host.workers.values()):
                    if worker.state == DeviceState.UNAVAILABLE:
                        mesh.remove_physical_worker_info(worker.worker_id)
                        host.unregister_workers([worker])

        return mesh

    def update_ranks(self, mesh: Mesh) -> Mesh:
        """Update host and worker ranks based on the mesh.

        Args:
            mesh (Mesh): Mesh object.

        Returns:
            Mesh: Mesh object with updated ranks.
        """
        # Get list of all hosts
        for host in mesh.get_all_hosts():
            if host.get_num_active_workers() == 0:
                if host.state == DeviceState.ACTIVE:
                    raise ValueError(
                        f"Host {host.host_id} has no active workers but is in an ACTIVE state."
                    )
                host.host_rank = None
            for worker in host.workers.values():
                if worker.state != DeviceState.ACTIVE:
                    if worker.local_rank is not None or worker.global_rank is not None:
                        raise ValueError(
                            f"Worker {worker.worker_id} is not in an ACTIVE state but has a rank."
                        )

        # Get list of all workers that have coordinates.
        all_active_workers = [
            worker
            for worker in list(mesh.get_all_workers())
            if worker.state == DeviceState.ACTIVE
        ]

        # Rerank workers based on their coordinates.
        all_active_workers.sort(key=lambda x: self.coords_sorting_key(x.coords))

        # Assign new global and local ranks to each host and worker.
        global_rank = 0
        local_rank = 0
        host_rank = -1
        prev_host = None
        for worker in all_active_workers:
            if worker.host != prev_host:
                host_rank += 1
                local_rank = 0
                worker.host.host_rank = host_rank
                prev_host = worker.host

            worker.global_rank = global_rank
            worker.local_rank = local_rank
            global_rank += 1
            local_rank += 1

    #### Strategy functions ####
    def can_apply_strategy(
        self, scale_direction: ScaleDirection, target_hosts: list[HostInfo]
    ) -> bool:
        """
        Applies strategy to training workload based on the scale direction and updated mesh.

        Args:
            scale_direction (ScaleDirection): The direction of scaling.
            target_hosts (list[HostInfo]): List of hosts with new updates.

        Returns:
            bool: True if the strategy can be applied to the training workload, False otherwise.
        """
        logging.info(
            f"Check if strategy {self.name} can be applied to scale {scale_direction} event."
        )

        # If target_hosts is empty, training state has not changed, so strategy cannot be applied.
        if len(target_hosts) == 0:
            return False

        # Clear superblocks that can scale up.
        self.superblocks_that_can_scale_up = {}

        if scale_direction == ScaleDirection.UP:
            # Number of available hosts that have the sufficient number of workers.
            num_available_hosts_per_superblock = Counter()

            # Count number of available hosts within target_hosts that have the sufficient number of workers.
            num_available_workers_per_host = Counter()
            for host in target_hosts:
                if host.state != DeviceState.UNAVAILABLE:
                    num_available_workers = len(
                        [
                            worker
                            for worker in host.workers.values()
                            if worker.state == DeviceState.AVAILABLE
                        ]
                    )
                    num_available_workers_per_host[
                        (host.host_id, host.superblock_id)
                    ] += num_available_workers

            # Count number of available workers for each host.
            for host in self.adaptr_mesh.get_all_hosts():
                if host.state != DeviceState.UNAVAILABLE:
                    if host.host_id not in [
                        target_host.host_id for target_host in target_hosts
                    ]:
                        num_available_workers = len(
                            [
                                worker
                                for worker in host.workers.values()
                                if worker.state == DeviceState.AVAILABLE
                            ]
                        )
                        num_available_workers_per_host[
                            (host.host_id, host.superblock_id)
                        ] += num_available_workers

            # Count the number of hosts that have the sufficient number of workers to be added to a new data replica.
            for (
                host_id,
                superblock_id,
            ), num_available_workers in num_available_workers_per_host.items():
                if num_available_workers >= self.num_workers_per_host_per_data_replica:
                    num_available_hosts_per_superblock[superblock_id] += 1

            # Count number of data replicas that can be added to each superblock.
            for (
                superblock_id,
                num_available_hosts,
            ) in num_available_hosts_per_superblock.items():
                if num_available_hosts >= self.num_hosts_in_data_replica:
                    self.superblocks_that_can_scale_up[superblock_id] = (
                        num_available_hosts // self.num_hosts_in_data_replica
                    )

            if len(self.superblocks_that_can_scale_up) > 0:
                logging.info(
                    f"Strategy {self.name} can be applied to scale {scale_direction} event."
                )
                return True

        if scale_direction == ScaleDirection.DOWN:
            if self.adaptr_mesh.get_active_workers_count() > 0:
                logging.info(
                    f"Strategy {self.name} can be applied to scale {scale_direction} event."
                )
                return True

        logging.info(
            f"Strategy {self.name} cannot be applied to scale {scale_direction} event."
        )
        return False

    def generate_mesh(
        self, scale_direction: ScaleDirection, target_hosts: list[HostInfo]
    ) -> Mesh:
        """Generates a new mesh based on the given scale direction and target hosts.

        Args:
            scale_direction (ScaleDirection): The direction in which the mesh should be scaled.
            target_hosts (list[HostInfo]): List of hosts with new updates.

        Returns:
            Mesh: The generated mesh.
        """
        logging.info(
            f"Generate mesh for strategy {self.name} in scale {scale_direction} event."
        )
        # Reset state for new data replica groups.
        self.new_data_replica_groups_in_coords_per_superblock = defaultdict(list)

        generated_mesh = copy.deepcopy(self.adaptr_mesh)
        generated_mesh = self.add_target_hosts_to_mesh(generated_mesh, target_hosts)

        # If scale_direction is UP, this means that there are enough available hosts to add at least 1 new data replica.
        if scale_direction == ScaleDirection.UP:
            # Define list of new data replicas to add, `new_data_replicas_per_superblock`. Each data replica contains workers that are all in the same superblock.
            new_data_replicas_per_superblock = {}
            for (
                superblock_id,
                num_data_replicas_to_add,
            ) in self.superblocks_that_can_scale_up.items():
                new_data_replicas_per_superblock[superblock_id] = []
                new_data_replica = []

                # Iterate through hosts, where workers are added to the new data replica if the host has enough available workers.
                for host in generated_mesh.get_all_hosts():
                    available_workers = [
                        worker
                        for worker in host.workers.values()
                        if worker.state == DeviceState.AVAILABLE
                    ]
                    if (
                        len(available_workers)
                        >= self.num_workers_per_host_per_data_replica
                    ):
                        for count, worker in enumerate(available_workers):
                            # If the host has more available workers than the required number of workers per host per data replica, only add the required number of workers.
                            if count == self.num_workers_per_host_per_data_replica:
                                break
                            new_data_replica.append(worker)

                    if len(new_data_replica) == self.num_workers_in_data_replica:
                        new_data_replicas_per_superblock[superblock_id].append(
                            new_data_replica
                        )
                        new_data_replica = []

            # Assign coordinates to new data replicas and set worker states to ACTIVE.
            for (
                superblock_id,
                new_data_replicas,
            ) in new_data_replicas_per_superblock.items():
                for new_data_replica in new_data_replicas:
                    # Get new data replica coordinates and remove them from self.removed_data_replica_groups_in_coords_per_superblock
                    new_data_replica_coords = (
                        self.removed_data_replica_groups_in_coords_per_superblock.pop(0)
                    )

                    # Add new data replica coordinates to self.new_data_replica_groups_in_coords_per_superblock
                    self.new_data_replica_groups_in_coords_per_superblock[
                        superblock_id
                    ].append(new_data_replica_coords)

                    # Add new data replica coordinates to self.active_data_replica_groups_in_coords_per_superblock
                    self.active_data_replica_groups_in_coords_per_superblock[
                        superblock_id
                    ].append(new_data_replica_coords)

                    # NOTE: This coordinate assignment is experimental and may need to be adjusted.
                    for worker, coords in zip(
                        new_data_replica, new_data_replica_coords
                    ):
                        worker.coords = coords
                        # Add worker to the mesh. This will set the worker state to ACTIVE and update coords->worker mapping.
                        # However, global_rank and local_rank will not be updated since they are yet to be assigned.
                        generated_mesh.add_virtual_worker_info(worker)

            # Increase virtual slice dimension by 1
            generated_mesh.virtual_mesh_dimensions["dp"] += len(
                self.get_all_new_data_replica_groups_in_coords()
            )

        # If scale_direction is DOWN, this means that one of the target hosts contains a worker that is UNAVAILABLE.
        # Remove each data replica group from the virtual mesh that contains the UNAVAILABLE worker.
        if scale_direction == ScaleDirection.DOWN:
            # Iterate through each worker in each target host. If target_worker is UNAVAILABLE, remove workers from the target worker's data replica group.
            for target_host in target_hosts:
                for target_worker in target_host.workers.values():
                    if target_worker.state == DeviceState.UNAVAILABLE:
                        # Update State of target worker to UNAVAILABLE
                        generated_mesh.get_worker(
                            target_worker.worker_id
                        ).state = DeviceState.UNAVAILABLE

                        # Get coords of target worker
                        target_worker_coords = generated_mesh.get_worker(
                            target_worker.worker_id
                        ).coords

                        # Virtually remove workers from the target worker's data replica group
                        removed_data_replica_coords = self.get_data_replica_coords(
                            target_worker_coords
                        )

                        # Check that target worker has not already been removed
                        if (
                            removed_data_replica_coords
                            not in self.get_all_removed_data_replica_groups_in_coords()
                        ):
                            # Virtually remove workers from the target worker's data replica group
                            for coords in removed_data_replica_coords:
                                worker_to_remove = (
                                    generated_mesh.get_worker_from_coords(coords)
                                )
                                generated_mesh.remove_virtual_worker_info(
                                    worker_to_remove
                                )

                            # Add removed data replica coordinates to self.removed_data_replica_groups_in_coords_per_superblock
                            self.removed_data_replica_groups_in_coords_per_superblock.append(
                                removed_data_replica_coords
                            )

                            # Remove removed data replica coordinates from self.active_data_replica_groups_in_coords_per_superblock
                            self.active_data_replica_groups_in_coords_per_superblock[
                                target_host.superblock_id
                            ].remove(removed_data_replica_coords)

            # Update mesh dimensions
            generated_mesh.virtual_mesh_dimensions["dp"] -= len(
                self.get_all_removed_data_replica_groups_in_coords()
            )

        self.update_ranks(generated_mesh)

        # Populate updated virtual mappings
        generated_mesh.update_rank_mapping()

        # Cleanup mesh
        generated_mesh = self.cleanup_mesh(generated_mesh)

        # Check that generated mesh is ready to use for training before returning
        if not generated_mesh.ready_to_use():
            raise ValueError("Generated mesh is not ready to use for training")
        logging.info(
            f"Leaving generate_mesh for strategy {self.name} in scale {scale_direction} event."
        )
        return generated_mesh

    def generate_commands(
        self, scale_direction: ScaleDirection, updated_mesh: Mesh
    ) -> adaptr_core.CommandSets:
        """Defines a set of commands based on scale direction and updated mesh to apply the strategy to the training workload.

        Args:
            scale_direction (ScaleDirection): The direction of scaling.
            updated_mesh (Mesh): The updated mesh resulting from `self.generate_mesh()`.
        Returns:
            adaptr_core.CommandSets: CommandSets required to apply the strategy to the training workload.
        """
        # Iterate through each host and worker in updated_mesh to generate host commands
        # Based on the following cases, each host and worker will have different callbacks that they will need to call
        # Host cases:
        # 1) Host was ACTIVE and is still ACTIVE: This means that a host actively in training is still in training. Callbacks needed at the host level: stop -> no_op_ckpt or send_ckpt -> start
        # 2) Host was AVAILABLE/did not exist and is now ACTIVE: This means that a host is added to training, meaning that host needs to copy state from another host in a different data replica. Callbacks needed at the host level: recv_ckpt -> start
        # 3) Host was ACTIVE and is now AVAILABLE: This means that a host is no longer participating in training. Since there are other data replicas, there is no need to save state. Callbacks needed at the host level: stop
        # 4) Host was AVAIALBLE/did not exist and is still AVAILABLE: This means that a host is not participating in training. Callbacks needed at the host level: None
        # 5) None of the above, will raise an error since strategy does not support this case

        # When using tensor paralleism != 8, there is an additional caveat to consider:
        # For Host case (1):
        # a) Old number of active workers < new number of active workers This means that new workers are added to training. Callbacks needed at the host level: recv_ckpt -> start
        # b) Old number of active workers = new number of active workers. This means that all workers active in training are still active in training. Callbacks needed at the host level: stop -> no_op_ckpt or send_ckpt -> start

        logging.info(
            f"Generate commands for strategy {self.name} in scale {scale_direction} event."
        )
        # Map existing data replica groups to new data replica groups. This map will determine peers for sending and receiving state.
        peer_host_ranks_map = {}

        if len(self.get_all_new_data_replica_groups_in_coords()) > len(
            self.get_all_active_data_replica_groups_in_coords(False)
        ):
            raise RuntimeError(
                "This strategy does not yet support adding more data replicas than the number of active data replicas."
            )

        if len(self.get_all_active_data_replica_groups_in_coords(False)) == 0:
            logging.warning(
                "All data replicas have been removed. There is no active training."
            )

        for new_data_replica_group, active_data_replica_group in zip(
            self.get_all_new_data_replica_groups_in_coords(),
            self.get_all_active_data_replica_groups_in_coords(False),
        ):
            for new_coord, active_coord in zip(
                new_data_replica_group, active_data_replica_group
            ):
                new_host = updated_mesh.get_worker_from_coords(new_coord).host
                active_host = updated_mesh.get_worker_from_coords(active_coord).host
                peer_host_ranks_map[new_host] = active_host
                peer_host_ranks_map[active_host] = new_host

        # Define host commands
        command_set = adaptr_core.CommandSet()
        command_set_list = []
        for host_info in updated_mesh.get_all_hosts():
            # Define host command
            command = adaptr_core.Command()

            # Determine old and new host states
            try:
                old_host_state = self.adaptr_mesh.get_host(host_info.host_id).state
                old_host_num_active_workers = self.adaptr_mesh.get_host(
                    host_info.host_id
                ).get_num_active_workers()
            except Exception:
                old_host_state = None
            new_host_state = host_info.state
            new_host_num_active_workers = host_info.get_num_active_workers()

            # Determine host case:
            host_case = -1

            # Host case 1 (or 2 when tp != 8)
            if (
                old_host_state == DeviceState.ACTIVE
                and new_host_state == DeviceState.ACTIVE
            ):
                if old_host_num_active_workers < new_host_num_active_workers:
                    host_case = 2
                else:
                    host_case = 1
            # Host case 2
            elif (
                old_host_state is None or old_host_state == DeviceState.AVAILABLE
            ) and new_host_state == DeviceState.ACTIVE:
                host_case = 2
            # Host case 3
            elif (
                old_host_state == DeviceState.ACTIVE
                and new_host_state == DeviceState.AVAILABLE
            ):
                host_case = 3
            # Host case 4
            elif (
                old_host_state is None or old_host_state == DeviceState.AVAILABLE
            ) and new_host_state == DeviceState.AVAILABLE:
                host_case = 4
            # Host case 5
            else:
                raise ValueError(
                    f"Strategy does not support changes in host state from {old_host_state} to {new_host_state}"
                )

            # Define callback names for host command metadata
            if host_case == 1:
                if host_info in peer_host_ranks_map:
                    command.peer_host_info = peer_host_ranks_map[
                        host_info
                    ].export_info()
                    command.callback_names = [
                        "stop",
                        "send_ckpt",
                        "start",
                    ]
                    command.callback_kwargs = [
                        "",
                        f"new_num_hosts={updated_mesh.get_active_hosts_count()},master_addr={get_torch_master_address(updated_mesh)}",
                        f"new_world_size={updated_mesh.get_active_workers_count()},new_num_hosts={updated_mesh.get_active_hosts_count()},master_addr={get_torch_master_address(updated_mesh)}",
                    ]
                else:
                    command.callback_names = [
                        "stop",
                        "no_op_ckpt",
                        "start",
                    ]
                    command.callback_kwargs = [
                        "",
                        f"new_num_hosts={updated_mesh.get_active_hosts_count()},master_addr={get_torch_master_address(updated_mesh)}",
                        f"new_world_size={updated_mesh.get_active_workers_count()},new_num_hosts={updated_mesh.get_active_hosts_count()},master_addr={get_torch_master_address(updated_mesh)}",
                    ]
            if host_case == 2:
                command.callback_names = [
                    "recv_ckpt",
                    "start",
                ]
                command.callback_kwargs = [
                    f"new_num_hosts={updated_mesh.get_active_hosts_count()},master_addr={get_torch_master_address(updated_mesh)}",
                    f"new_world_size={updated_mesh.get_active_workers_count()},new_num_hosts={updated_mesh.get_active_hosts_count()},master_addr={get_torch_master_address(updated_mesh)}",
                ]
                command.peer_host_info = peer_host_ranks_map[host_info].export_info()
            if host_case == 3:
                command.callback_names = ["stop"]
                command.callback_kwargs = [""]
            if host_case == 4:
                command.callback_names = []
                command.callback_kwargs = []

            # Add host info to host command
            command.host_info = host_info.export_info()

            # List of worker info to add to host command and host info respectively
            worker_info_list = [
                worker.export_info() for worker in host_info.workers.values()
            ]

            # Add worker info objects to host info
            command.host_info.workers = worker_info_list

            # Add host command to host commands list
            command_set_list.append(command)

        # Add host commands to host commands object
        command_set.set = command_set_list

        logging.info(
            f"Leaving generate_commands for strategy {self.name} in scale {scale_direction} event."
        )

        command_sets = adaptr_core.CommandSets()
        command_sets.sets = [command_set]

        return command_sets
