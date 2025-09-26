from kubernetes import client, config
import logging
import os
import subprocess


def get_pod_on_host(
    api_instance: client.CoreV1Api, host_name: str, namespace: str = "default"
):
    """
    Gets the name of a running pod on the specified host.

    Args:
      api_instance: An instance of the Kubernetes CoreV1Api client.
      node_name: The name of the node.
      namespace: The namespace to search in.

    Returns:
      The name of the first running pod found on the node, or None if no running pod is found.
    """
    try:
        pods = api_instance.list_namespaced_pod(
            namespace=namespace, field_selector=f"spec.nodeName={host_name}"
        )
        for pod in pods.items:
            if pod.status.phase == "Running" and "daemon" not in pod.metadata.name:
                return pod.metadata.name
        return None

    except client.rest.ApiException:
        logging.exception(f"Error getting pods on node {host_name}.")
        return None


class KubernetesCallbacks:
    """
    Kubernetes-specific implementation of OrchestratorCallbacks.
    """

    def reset_host(self, host_name: str) -> None:
        """
        Resets the specified host in Kubernetes.

        Args:
            host_name: The host name (node name) of the host to reboot.
            namespace: The namespace where the pod is running.
        """
        pass

    def drain_host(
        self,
        host_name: str,
    ) -> None:
        """
        Cordons and drains the specified host in a Kubernetes cluster.

        Args:
            host_name: The host name (node name) of the machine to quarantine.
        """
        config.load_incluster_config()
        self.cordon_host(host_name)
        self.delete_pod(host_name)

    def cordon_host(
        self,
        host_name: str,
    ) -> None:
        """
        Uncordons the specified host in a Kubernetes cluster.

        Args:
            host_name: The host name (node name) of the machine to quarantine.
        """
        config.load_incluster_config()

        cordon_result = subprocess.run(
            ["kubectl", "cordon", host_name],
            check=True,
            capture_output=True,
            shell=False,
        )

        if cordon_result.returncode == 0:
            logging.info(f"Node {host_name} successfuly cordoned.")
        else:
            logging.exception(f"Node {host_name} failed to cordone!")

    def uncordon_host(
        self,
        host_name: str,
    ) -> None:
        """
        Uncordons the specified host in a Kubernetes cluster.

        Args:
            host_name: The host name (node name) of the machine to quarantine.
        """
        config.load_incluster_config()

        uncordon_result = subprocess.run(
            ["kubectl", "uncordon", host_name],
            check=True,
            capture_output=True,
            shell=False,
        )

        if uncordon_result.returncode == 0:
            logging.info(f"Node {host_name} successfuly uncordoned.")
        else:
            logging.exception(f"Node {host_name} failed to uncordone!")

    def delete_pod(self, host_name, namespace: str | None = None) -> None:
        """Reboots all pods associated with a Kubernetes Job.

        Args:
            job_name: The job to reboot.
            namespace: The namespace where the pod and Job are running.
        """
        if namespace is None:
            namespace = os.environ["JOB_NAMESPACE"]

        config.load_incluster_config()
        api_core = client.CoreV1Api()

        pod_name = get_pod_on_host(api_core, host_name, namespace)

        delete_result = subprocess.run(
            ["kubectl", "delete", "pod", pod_name, "--force"],
            check=True,
            capture_output=True,
            shell=False,
        )

        if delete_result.returncode == 0:
            logging.info(f"Workload pod on {host_name} successfuly deleted.")
        else:
            logging.exception(f"Workload pod on {host_name} failed to delete!")

    def reset_gpu(
        self,
        host_name: str,
        gpu_local_rank: str,
    ) -> None:
        """
        Resets a specific GPU on a given host.

        Args:
            host name: The host name (node name) of the host.
            gpu_local_rank: The local rank of the GPU to reset.
        """
        pass
