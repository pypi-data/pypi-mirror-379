from abc import ABC, abstractmethod


class OrchestratorCallbacks(ABC):
    """
    Abstract base class for orchestrator callbacks.
    """

    @abstractmethod
    def reboot_host(self, hostname: str, **kwargs) -> None:
        """
        Reboots the specified host.

        Args:
            hostname: The hostname of the host to reboot.
        """
        pass

    @abstractmethod
    def reboot_container(self, hostname: str, container_name: str, **kwargs) -> None:
        """
        Reboots the training container of the specified host.

        Args:
            hostname: The hostname of the host containing the training container.
            container_name: The name of the container to reboot.
        """
        pass

    @abstractmethod
    def quarantine_host(self, hostname: str, **kwargs) -> None:
        """
        Quarantines the specified host.

        Args:
            hostname: The hostname of the machine to quarantine.
        """
        pass

    @abstractmethod
    def unquarantine_host(self, hostname: str, **kwargs) -> None:
        """
        Unquarantines the specified host.

        Args:
            hostname: The hostname of the machine to quarantine.
        """
        pass

    @abstractmethod
    def reset_job(self, job_name: str, **kwargs) -> None:
        """
        Resets all of the containers associated with a job.

        Args:
            job_name: The name of the job to reboot.
        """
        pass

    @abstractmethod
    def reset_gpu(
        self, hostname: str, gpu_id: str, zone: str, project_id: str, **kwargs
    ) -> None:
        """
        Resets a specific GPU on a given host.

        Args:
            hostname: The hostname of the host.
            gpu_id: The ID of the GPU to reset.
            zone: The gcloud zone the host is in.
            project_id: The gcloud project ID.
        """
        pass
