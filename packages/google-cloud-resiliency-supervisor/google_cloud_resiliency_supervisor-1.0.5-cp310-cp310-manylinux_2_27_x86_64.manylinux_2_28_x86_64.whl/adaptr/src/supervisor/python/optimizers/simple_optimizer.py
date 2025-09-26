"""Simple implementation of BaseOptimizer class."""

from adaptr.src.supervisor.python.optimizers.base_optimizer import BaseOptimizer
from adaptr.src.supervisor.python.elastic_strategies.base_strategy import BaseStrategy
from adaptr.src.supervisor.python.elastic_strategies.hot_swap_strategy import (
    HotSwapStrategy,
)
from adaptr.src.supervisor.python.elastic_strategies.reset_strategy import ResetStrategy
from adaptr.src.core.python.mesh import Mesh


class SimpleOptimizer(BaseOptimizer):
    """Optimzer that attempts to reset the workload first, and falls back to hot-swapping if necessary."""

    def __init__(self, mesh: Mesh):
        self.mesh = mesh
        reset_strategy = ResetStrategy(mesh)
        hot_swap_strategy = HotSwapStrategy(mesh)
        elastic_strategies = [reset_strategy, hot_swap_strategy]

        super().__init__(mesh, elastic_strategies)

    def get_best_strategy(self, generated_results: dict[str, Mesh]) -> BaseStrategy:
        """Returns the best strategy based on the generated results.

        Args:
            generated_results (dict[BaseStrategy, Mesh]): A dictionary containing the generated results,

        Returns:
            BaseStrategy: The best strategy.
        """

        if "reset_strategy" in generated_results:
            return self.strategy_registry["reset_strategy"]
        else:
            self.strategy_registry["reset_strategy"].reset_counter()
            return self.strategy_registry["hot_swap_strategy"]
