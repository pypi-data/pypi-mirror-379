# meta_learning.py

import numpy as np

from src.agix.evaluation.metrics import EvaluationMetrics
from src.agix.memory.narrative import NarrativeMemoryTree


class MetaLearner:
    """
    Clase base para meta-aprendizaje de políticas AGI.
    Aplica transformaciones de segundo orden sobre agentes (π → π′),
    con posibles estrategias basadas en evolución o gradientes.
    """

    def __init__(self, strategy: str = "evolution"):
        self.strategy = strategy
        self.history = []  # historial de eficiencia

    def transform(self, agent):
        """
        Modifica internamente la política del agente.
        Devuelve una versión ajustada del mismo.
        """
        if self.strategy == "gradient":
            return self.gradient_update(agent)
        elif self.strategy == "evolution":
            return self.evolutionary_tweak(agent)
        else:
            raise NotImplementedError(f"Estrategia de meta-aprendizaje '{self.strategy}' no implementada.")

    def gradient_update(self, agent):
        # Placeholder para integración futura con frameworks autodiferenciables.
        return agent

    def evolutionary_tweak(self, agent):
        """
        Introduce una ligera mutación en el genotipo del agente, si existe.
        """
        if hasattr(agent, "chromosome"):
            agent.chromosome += 0.01 * np.random.normal(size=agent.chromosome.shape)
        return agent

    # --- nueva funcionalidad ---
    def adapt_memory(self, agent, reward_history):
        """Ajusta K y D de la memoria narrativa según carga y recompensa."""
        tree = getattr(agent, "memory", None)
        if not isinstance(tree, NarrativeMemoryTree):
            return agent

        avg_reward = EvaluationMetrics.average_reward(reward_history)
        load = tree.load_factor()

        if load > 0.75 and avg_reward >= 0.5:
            tree.K += 1
            tree.D += 1
        elif load < 0.25 and avg_reward < 0.2:
            tree.K = max(1, tree.K - 1)
            tree.D = max(1, tree.D - 1)

        self.history.append({"K": tree.K, "D": tree.D, "load": load, "reward": avg_reward})
        return agent
