# variational.py

import numpy as np
from typing import Callable, List


class VariationalPolicyOptimizer:
    """
    Optimizador de políticas con principios variacionales.
    Permite regular la exploración mediante entropía controlada.
    """

    def __init__(self, policy_model: Callable[[np.ndarray], np.ndarray], entropy_weight: float = 0.1):
        """
        policy_model: función que mapea un estado a una distribución de acciones.
        entropy_weight: peso asignado a la entropía para regular la exploración.
        """
        self.policy_model = policy_model
        self.entropy_weight = entropy_weight

    def compute_entropy(self, action_probs: np.ndarray) -> float:
        """
        Calcula la entropía Shannon de la distribución de acciones.
        """
        return -np.sum(action_probs * np.log(action_probs + 1e-10))

    def optimize(self, states: List[np.ndarray], rewards: List[float]):
        """
        Método principal de optimización basado en principios variacionales.
        Debe implementarse en subclases según la técnica elegida.
        """
        raise NotImplementedError("Debe implementarse un método de optimización específico.")
