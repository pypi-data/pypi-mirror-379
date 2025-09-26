"""Callbacks for interacting with a Kubernetes cluster."""

import copy
import datetime
import logging
import subprocess
import time
import typing

from kubernetes import client
from kubernetes import config
from supervisor.src.core.python import utils
import supervisor_core


class KubernetesCallbacks:
  """Kubernetes-specific implementation of OrchestratorCallbacks.

  This class provides methods for interacting with a Kubernetes cluster,
  such as resetting hosts, draining hosts, and restarting jobsets.
  """

  def __init__(self, supervisor_config: supervisor_core.SupervisorConfig):
    """Initializes the KubernetesCallbacks class.

    This method loads the Kubernetes configuration and initializes the
    necessary API clients. It also sets the namespace based on the
    JOB_NAMESPACE environment variable or defaults to "default".

    Args:
        supervisor_config: The SupervisorConfig object containing the
          configuration for the Kubernetes cluster.
    """
    try:
      config.load_incluster_config()
    except:
      config.load_kube_config()

    # Required Kubernetes API clients
    self.core_api = client.CoreV1Api()
    self.custom_api = client.CustomObjectsApi()

    # Workload related configuration
    self.namespace = supervisor_config.job_namespace
    self.pod_termination_threshold_s = (
        supervisor_config.pod_termination_threshold_s
    )
    self.jobset_downtime_threshold_s = (
        supervisor_config.jobset_downtime_threshold_s
    )
    self.jobset_replicated_job_name = (
        supervisor_config.jobset_replicated_job_name
    )
    self.jobset_workload_container_name = (
        supervisor_config.jobset_workload_container_name
    )
    self.num_nodes_per_dp = (
        supervisor_config.num_nodes_per_dp
        if supervisor_config.num_nodes_per_dp > 0
        else None
    )
    self.num_dp = (
        supervisor_config.num_dp_replicas
        if supervisor_config.num_dp_replicas > 0
        else None
    )
    self.max_num_dp = self.num_dp if self.num_dp > 0 else None

    # Jobset related state
    self.jobset_downtime = None
    self.jobset_name = None
    self.jobset_watcher = None

    self.logger = utils.setup_logger()

  def get_workload_info(self, host_name: str) -> None:
    """Gets the workload information for a given host.

    Args:
        host_name: The host name (node name) of the host to get the workload
          information for.
    """
    if self.jobset_name is None:
      jobset_name = self._get_jobset_name(host_name)

      if jobset_name is None:
        self.logger.warning(
            f'No jobset found on host {host_name}. Skipping workload info'
            ' retrieval.'
        )
      else:
        self.jobset_name = jobset_name

  def reset_host(self, host_name: str) -> None:
    """Resets the specified host in Kubernetes.

    Args:
        host_name: The host name (node name) of the host to reboot.
    """
    pass

  def drain_host(
      self,
      host_name: str,
  ) -> None:
    """Cordons and drains the specified host in a Kubernetes cluster.

    Args:
        host_name: The host name (node name) of the machine to quarantine.
    """
    self.cordon_host(host_name)
    self.delete_pod(host_name)

  def cordon_host(
      self,
      host_name: str,
  ) -> None:
    """Cordons the specified host in a Kubernetes cluster.

    Args:
        host_name: The host name (node name) of the machine to quarantine.
    """
    cordon_result = subprocess.run(
        ['kubectl', 'cordon', host_name],
        check=True,
        capture_output=True,
        shell=False,
    )

    if cordon_result.returncode == 0:
      self.logger.info(f'Successfully cordoned node {host_name}.')
    else:
      self.logger.exception(f'Failed to cordon node {host_name}.')

  def uncordon_host(
      self,
      host_name: str,
  ) -> None:
    """Uncordons the specified host in a Kubernetes cluster.

    Args:
        host_name: The host name (node name) of the machine to quarantine.
    """

    uncordon_result = subprocess.run(
        ['kubectl', 'uncordon', host_name],
        check=True,
        capture_output=True,
        shell=False,
    )

    if uncordon_result.returncode == 0:
      self.logger.info(f'Successfully uncordoned node {host_name}.')
    else:
      self.logger.exception(f'Failed to uncordon node {host_name}.')

  def delete_pod(self, host_name: str) -> None:
    """Deletes the pod running on the specified host.

    Args:
        host_name: The host name (node name) of the machine.
    """

    pod_name = self._get_pod_on_host(host_name)

    if not pod_name:
      self.logger.warning(
          f'No workload pod found on host {host_name}. Skipping pod deletion.'
      )
      return

    self._force_delete_pod(pod_name)

  def restart_jobset(
      self, host_name: str, scale_direction: str | None = None
  ) -> bool:
    """Restarts a jobset running on the specified host.

    This method can handle a jobset with hanging pods by:
    1. Getting the current jobset spec
    2. Deleting the hanging jobset
    3. Creating a new jobset

    Args:
        host_name: The host name (node name) associated with the jobset.
        scale_direction: Optional argument to scale the jobset replicas up or
          down. Valid values are 'up', 'down', or None (no scaling).

    Returns:
        True if the jobset was successfully restarted, False otherwise.

    Raises:
        ValueError: If the scale_direction is invalid.
    """
    try:
      if scale_direction not in ['up', 'down', None]:
        raise ValueError(f'Invalid scale direction: {scale_direction}')

      if scale_direction is not None and (self.num_nodes_per_dp is None):
        raise ValueError(
            'Cannot scale jobset if num_nodes_per_dp is not provided.'
        )

      if not self.jobset_name:
        self.logger.warning(
            f'No jobset found on host {host_name}. Cannot restart.'
        )
        return False

      self.logger.info(
          f'Retrieving jobset spec for {self.jobset_name} before deletion.'
      )
      new_spec = self._get_jobset_spec(self.jobset_name)
      if not new_spec:
        return False

      self.logger.info(f'Deleting jobset {self.jobset_name}.')
      if not self._delete_jobset(self.jobset_name):
        return False

      # Wait for the pod termination threshold to ensure that all pods are terminated
      self.logger.info(
          f'Waiting {self.pod_termination_threshold_s} seconds for pods to'
          ' terminate.'
      )
      time.sleep(self.pod_termination_threshold_s)

      # Scale the number of replicas if necessary
      if scale_direction == 'up' and self._can_scale_up():
        self.logger.info(
            f'Scaling jobset {self.jobset_name} up by'
            f' {self.num_nodes_per_dp} nodes.'
        )
        new_spec = self._scale_jobset_spec(new_spec, scale_direction)
        self.num_dp += 1

      elif scale_direction == 'down' and self._can_scale_down():
        self.logger.info(
            f'Scaling jobset {self.jobset_name} down by'
            f' {self.num_nodes_per_dp} nodes.'
        )
        new_spec = self._scale_jobset_spec(new_spec, scale_direction)
        self.num_dp -= 1

        # Cordon faulty host to avoid rescheduling post-scale down
        self.cordon_host(host_name)

      # Check for stuck pods and force delete them
      stuck_pods = self._get_stuck_pods(self.jobset_name)
      if stuck_pods:
        self.logger.warning(
            f'Found {len(stuck_pods)} pods stuck in terminating state in Jobset'
            f' {self.jobset_name}. Force deleting pods...'
        )
        for pod in stuck_pods:
          self._force_delete_pod(pod['name'])

      # Create new Jobset with updated spec
      if self._create_jobset(new_spec):
        self.logger.info(
            f'Successfully restarted jobset {self.jobset_name} as'
            f" {new_spec['metadata']['name']}"
        )
        return True

      return False

    except RuntimeError:
      self.logger.exception(
          f'An error occurred while restarting jobset {self.jobset_name}.'
      )
      return False

  def reset_gpu(
      self,
      host_name: str,
      gpu_local_rank: str,
  ) -> None:
    """Resets a specific GPU on a given host.

    Args: host name: The host name (node name) of the host.
        gpu_local_rank: The local rank of the GPU to reset.
    """
    pass

  def poll_jobset_status(self, host_name: str):
    """Polls the status of a Jobset and initiates resubmission if needed.

    This method checks for stuck pods and non-running pods in the jobset.
    If stuck pods are found, it restarts the jobset. If non-running pods
    persist for longer than the configured threshold, it also restarts the
    jobset.

    Args:
        host_name: The host name (node name) associated with the jobset.
    """

    try:
      if not self.jobset_name:
        self.logger.warning(
            f'No jobset found on host {host_name}. Skipping status check.'
        )
        return

      if not self._check_jobset_exists(self.jobset_name):
        return

      pod_status = self._get_jobset_pods_status(self.jobset_name)
      self.logger.info(f'Jobset {self.jobset_name} pod status: {pod_status}')

      if pod_status and not pod_status['all_running']:
        if self.jobset_downtime is None:
          self.jobset_downtime = time.time()
          self.logger.warning(
              f'Jobset {self.jobset_name} has non-running pods. '
              f"Pending: {len(pod_status['pending_pods'])}, "
              f"Other states: {len(pod_status['other_state_pods'])}. "
              f'Will check again in {self.jobset_downtime_threshold_s} seconds.'
          )
        else:
          if (
              time.time() - self.jobset_downtime
              > self.jobset_downtime_threshold_s
          ):
            self.logger.warning(
                f'Jobset {self.jobset_name} pods not running for more than'
                f' {self.jobset_downtime_threshold_s} seconds. Initiating'
                ' jobset restart...'
            )
            if self.restart_jobset(host_name):
              self.logger.info(
                  f'Successfully restarted jobset {self.jobset_name} after'
                  ' detecting non-running pods.'
              )
              self.jobset_downtime = None
            else:
              self.logger.exception(
                  f'Failed to restart jobset {self.jobset_name} after detecting'
                  ' non-running pods.'
              )

      elif pod_status and pod_status['all_running']:
        self.jobset_downtime = None
        self.logger.info(f'All pods in jobset {self.jobset_name} are running.')

      else:
        self.logger.warning(
            'Could not retrieve pod status for pods in jobset'
            f' {self.jobset_name}.'
        )

    except RuntimeError:
      self.logger.exception(
          f'Error while polling jobset {self.jobset_name} status.'
      )

  def _get_pod_on_host(self, host_name: str):
    """Gets the name of a running pod on the specified host.

    Args:
        host_name: The name of the host (node).

    Returns:
        The name of the first running pod found on the node, or None if no
        running pod is found.

    Raises:
        client.rest.ApiException: If there is an error getting the pod list.
    """
    try:
      pods = self.core_api.list_namespaced_pod(
          namespace=self.namespace, field_selector=f'spec.nodeName={host_name}'
      )
      for pod in pods.items:
        if pod.status.phase == 'Running' and 'daemon' not in pod.metadata.name:
          return pod.metadata.name
      return None

    except client.rest.ApiException:
      self.logger.exception(f'Error getting pods on node {host_name}.')
      return None

  def _force_delete_pod(self, pod_name: str) -> bool:
    """Force deletes a pod.

    Args:
        pod_name: The name of the pod to delete.
    """
    try:
      self.core_api.delete_namespaced_pod(
          name=pod_name,
          namespace=self.namespace,
          propagation_policy='Background',
          grace_period_seconds=0,
      )
      self.logger.info(f'Successfully deleted workload pod {pod_name}.')
    except client.ApiException:
      self.logger.exception(f'Failed to delete workload pod {pod_name}.')

  def _create_jobset(self, jobset_spec: dict) -> bool:
    """Creates a new jobset from the given spec.

    Args:
        jobset_spec: A dictionary representing the jobset specification.

    Returns:
        True if the jobset was successfully created, False otherwise.

    Raises:
        RuntimeError: If there is an error creating the jobset.
    """
    try:
      self.custom_api.create_namespaced_custom_object(
          group='jobset.x-k8s.io',
          version='v1alpha2',
          namespace=self.namespace,
          plural='jobsets',
          body=jobset_spec,
      )
      return True

    except RuntimeError:
      self.logger.exception(
          f"Error creating new jobset {jobset_spec['metadata']['name']}."
      )
      return False

  def _delete_jobset(self, jobset_name: str) -> bool:
    """Deletes the entire jobset.

    Args:
        jobset_name: The name of the jobset to delete.

    Returns:
        True if the jobset was successfully deleted, False otherwise.

    Raises:
        RuntimeError: If there is an error deleting the jobset.
    """
    try:
      self.custom_api.delete_namespaced_custom_object(
          group='jobset.x-k8s.io',
          version='v1alpha2',
          namespace=self.namespace,
          plural='jobsets',
          name=jobset_name,
          body=client.V1DeleteOptions(
              grace_period_seconds=0, propagation_policy='Background'
          ),
      )
      return True

    except RuntimeError:
      self.logger.exception(f'Error deleting jobset {jobset_name}.')
      return False

  def _check_jobset_exists(self, jobset_name: str) -> bool:
    """Checks if a jobset exists."""
    try:
      self.custom_api.get_namespaced_custom_object(
          group='jobset.x-k8s.io',
          version='v1alpha2',
          namespace=self.namespace,
          plural='jobsets',
          name=jobset_name,
      )
      return True

    except client.ApiException:
      self.logger.warning(
          f'Jobset {jobset_name} does not exist. This usually means the Jobset'
          ' was already deleted.'
      )
      self.logger.info(f'Resetting Jobset name to None.')
      self.jobset_name = None
      return False

  def _get_jobset_spec(self, jobset_name: str) -> dict | None:
    """Gets the current JobSet spec for resubmission.

    Args:
        jobset_name: The name of the jobset.

    Returns:
        A dictionary representing the jobset specification, or None if
        there is an error getting the spec.

    Raises:
        RuntimeError: If there is an error getting the jobset spec.
    """
    try:
      jobset = self.custom_api.get_namespaced_custom_object(
          group='jobset.x-k8s.io',
          version='v1alpha2',
          namespace=self.namespace,
          plural='jobsets',
          name=jobset_name,
      )

      # Create a clean copy for resubmission
      new_spec = copy.deepcopy(jobset)

      # Remove metadata that shouldn't be reused
      new_spec['metadata'].pop('resourceVersion', None)
      new_spec['metadata'].pop('uid', None)
      new_spec['metadata'].pop('creationTimestamp', None)
      new_spec['metadata'].pop('generation', None)

      return new_spec

    except client.ApiException:
      self.logger.warning(
          f'Failed to retrieve Jobset spec for {jobset_name}. This usually'
          ' means the Jobset was already deleted.'
      )
      self.jobset_name = None
      return None

    except RuntimeError:
      self.logger.exception(
          'An unexpected error occurred while retrieving Jobset spec for'
          f' {jobset_name}.'
      )
      return None

  def _get_jobset_name(self, host_name: str) -> str | None:
    """Gets the name of a JobSet running on the specified host.

    Args:
        host_name: The name of the host (node).

    Returns:
        The name of the JobSet running on the host, or None if no JobSet is
        found.

    Raises:
        client.rest.ApiException: If there is an error getting the jobset list.
    """
    try:
      pod_name = self._get_pod_on_host(host_name)

      if not pod_name:
        self.logger.info(
            f'No workload pod found on host {host_name}. Cannot determine'
            ' Jobset name.'
        )
        return None

      jobsets = self.custom_api.list_namespaced_custom_object(
          group='jobset.x-k8s.io',
          version='v1alpha2',
          namespace=self.namespace,
          plural='jobsets',
      )

      for jobset in jobsets.get('items', []):
        if jobset['metadata']['name'] in pod_name:
          return jobset['metadata']['name']

      self.logger.warning(
          f'No Jobset found on host {host_name} matching pod name {pod_name}.'
      )
      return None

    except client.ApiException:
      self.logger.exception(
          'A Kubernetes API error occurred while retrieving Jobsets on node'
          f' {host_name}.'
      )
      return None

  def _get_jobset_pods_status(self, jobset_name: str) -> dict | None:
    """Gets the status of all pods in the jobset.

    Args:
        jobset_name: The name of the jobset.

    Returns:
        A dictionary containing the status of all pods in the jobset, or
        None if there is an error getting the pod status. The dictionary
        includes the total number of pods, the number of running pods, a
        list of pending pods with their start times, a list of pods in
        other states with their phases, and a boolean indicating if all
        pods are running.

    Raises:
        RuntimeError: If there is an error getting the pod status.
    """
    try:
      # TODO: b/405128228 - Modify to use the list and watch API
      pods = self.core_api.list_namespaced_pod(
          namespace=self.namespace,
          label_selector=f'jobset.sigs.k8s.io/jobset-name={jobset_name}',
      )

      status: dict[str, typing.Any] = {
          'total_pods': 0,
          'running_pods': 0,
          'pending_pods': [],
          'other_state_pods': [],
          'all_running': False,
      }

      for pod in pods.items:
        status['total_pods'] += 1

        if pod.status.phase == 'Running':
          # Check if all containers in pod are running
          all_containers_running = all(
              container.state.running is not None
              for container in pod.status.container_statuses
              if container.state is not None
          )

          if all_containers_running:
            status['running_pods'] += 1
          else:
            status['other_state_pods'].append({
                'name': pod.metadata.name,
                'phase': pod.status.phase,
                'containers': [
                    {
                        'name': container.name,
                        'state': (
                            next(iter(container.state.to_dict().keys()))
                            if container.state
                            else 'unknown'
                        ),
                    }
                    for container in pod.status.container_statuses
                ],
            })
        elif pod.status.phase == 'Pending':
          status['pending_pods'].append(
              {'name': pod.metadata.name, 'start_time': pod.status.start_time}
          )
        else:
          status['other_state_pods'].append(
              {'name': pod.metadata.name, 'phase': pod.status.phase}
          )

      status['all_running'] = (
          status['running_pods'] == status['total_pods']
          and status['total_pods'] > 0
      )
      return status

    except client.ApiException:
      self.logger.exception(
          'An Kubernetes API error occurred while getting pod statuses for'
          f' Jobset {jobset_name}.'
      )
      return None

    except RuntimeError:
      self.logger.exception(
          'An error occurred while retrieving pod statuses for Jobset'
          f' {jobset_name}.'
      )
      return None

  def _get_stuck_pods(self, jobset_name: str) -> list[dict[str, typing.Any]]:
    """Find pods in the jobset that are stuck in Terminating state.

    Args:
        jobset_name: The name of the jobset.

    Returns:
        A list of stuck pods with their details.
    """
    stuck_pods = []

    try:
      # Get all pods for this jobset
      pods = self.core_api.list_namespaced_pod(
          namespace=self.namespace,
          label_selector=f'jobset.sigs.k8s.io/jobset-name={jobset_name}',
      )

      current_time = datetime.datetime.now()

      for pod in pods.items:
        # Check if pod is terminating
        if pod.metadata.deletion_timestamp:
          # Calculate how long it's been terminating
          deletion_time = pod.metadata.deletion_timestamp.replace(tzinfo=None)
          terminating_duration = (current_time - deletion_time).total_seconds()
          threshold = max(
              pod.spec.termination_grace_period_seconds,
              self.pod_termination_threshold_s,
          )

          if terminating_duration > threshold:
            stuck_pods.append({
                'name': pod.metadata.name,
                'node': pod.spec.node_name,
                'terminating_duration': terminating_duration,
                'pod': pod,
            })

    except RuntimeError:
      self.logger.exception(
          'An error occurred while checking for stuck pods in Jobset'
          f' {jobset_name}.'
      )

    return stuck_pods

  def _can_scale_up(self) -> bool:
    """Returns if the jobset can scale up one data parallel replica."""
    if self.num_dp is None or self.num_nodes_per_dp is None:
      self.logger.warning(
          'Skipping jobset scale up due to missing NUM_DP_REPLICAS or'
          ' NUM_NODES_PER_DP environment variables.'
      )
      return False

    can_scale_up = self.num_dp + 1 <= self.max_num_dp
    if not can_scale_up:
      self.logger.warning(
          f'Cannot scale up jobset {self.jobset_name} to {self.num_dp + 1} data'
          ' parallel replicas.'
      )

    return can_scale_up

  def _can_scale_down(self) -> bool:
    """Returns if the jobset can scale down one data parallel replica."""
    if self.num_dp is None or self.num_nodes_per_dp is None:
      self.logger.warning(
          'Skipping jobset scale down due to missing NUM_DP_REPLICAS or'
          ' NUM_NODES_PER_DP environment variables.'
      )
      return False

    can_scale_down = self.num_dp - 1 >= 1
    if not can_scale_down:
      self.logger.warning(
          f'Cannot scale down jobset {self.jobset_name} to'
          f' {self.num_dp - 1} data parallel replicas.'
      )

    return can_scale_down

  def _scale_jobset_spec(
      self,
      jobset_spec: dict[str, typing.Any],
      scale_direction: str,
  ) -> dict:
    """Scales the jobset spec replicas up or down."""

    if scale_direction not in ['up', 'down']:
      raise ValueError(f'Invalid scale direction: {scale_direction}')

    if self.jobset_replicated_job_name is None:
      raise ValueError(
          'Cannot scale jobset if jobset_replicated_job_name is not provided.'
      )

    if self.jobset_workload_container_name is None:
      raise ValueError(
          'Cannot scale jobset if jobset_workload_container_name is not'
          ' provided.'
      )

    if self.num_nodes_per_dp is None:
      raise ValueError(
          'Cannot scale jobset if num_nodes_per_dp is not provided.'
      )

    if self.num_dp is None:
      raise ValueError('Cannot scale jobset if num_dp is not provided.')

    jobset_name = jobset_spec['metadata']['name']
    nodes_to_add = 0

    if scale_direction == 'up':
      nodes_to_add = self.num_nodes_per_dp
      logging.info(
          f'Scaling jobset {jobset_name} replicas up by {nodes_to_add} nodes.'
      )
    elif scale_direction == 'down':
      nodes_to_add = -self.num_nodes_per_dp
      logging.info(
          f'Scaling jobset {jobset_name} replicas down by'
          f' {-nodes_to_add} nodes.'
      )

    # Get the index of the replicated job and container in the spec
    replicated_job_index = self._find_replicated_job_index(jobset_spec)
    container_index = self._find_container_index(
        jobset_spec, replicated_job_index
    )

    # Update the parallelism and completions
    jobset_spec['spec']['replicatedJobs'][replicated_job_index]['template'][
        'spec'
    ]['parallelism'] += nodes_to_add
    jobset_spec['spec']['replicatedJobs'][replicated_job_index]['template'][
        'spec'
    ]['completions'] += nodes_to_add

    # Update the NNODES env var
    env_vars = jobset_spec['spec']['replicatedJobs'][replicated_job_index][
        'template'
    ]['spec']['template']['spec']['containers'][container_index]['env']
    env_vars = [
        {'name': var['name'], 'value': str(int(var['value']) + nodes_to_add)}
        if var['name'] == 'NNODES'
        else var
        for var in env_vars
    ]
    jobset_spec['spec']['replicatedJobs'][replicated_job_index]['template'][
        'spec'
    ]['template']['spec']['containers'][container_index]['env'] = env_vars

    return jobset_spec

  def _find_replicated_job_index(
      self, jobset_spec: dict[str, typing.Any]
  ) -> int:
    """Finds the index of the replicated job in the jobset spec."""
    for i, job_spec in enumerate(jobset_spec['spec']['replicatedJobs']):
      if job_spec['name'] == self.jobset_replicated_job_name:
        return i
    raise ValueError(
        f'Replicated job {self.jobset_replicated_job_name} not found in jobset'
        ' spec.'
    )

  def _find_container_index(
      self, jobset_spec: dict[str, typing.Any], replicated_job_index: int
  ) -> int:
    """Finds the index of the workload container in the jobset spec."""
    for i, container_spec in enumerate(
        jobset_spec['spec']['replicatedJobs'][replicated_job_index]['template'][
            'spec'
        ]['template']['spec']['containers']
    ):
      if container_spec['name'] == self.jobset_workload_container_name:
        return i
    raise ValueError(
        f'Container {self.jobset_workload_container_name} not found in jobset'
        ' spec.'
    )
