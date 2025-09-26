from typing import Callable

from adaptr.src.supervisor.python.orchestrators.gke_callbacks import KubernetesCallbacks


def get_orchestrator_callbacks(orchestrator_type: str) -> dict[str, Callable]:
    """Factory function to get orchestrator-specific callbacks."""
    if orchestrator_type.lower() == "gke":
        callbacks = KubernetesCallbacks()
        return {
            "drain_host": callbacks.drain_host,
            "uncordon_host": callbacks.uncordon_host,
            "delete_pod": callbacks.delete_pod,
        }
    else:
        raise ValueError(f"Unsupported orchestrator type: {orchestrator_type}")
