# src/agix/control/policy_optimization.py

import numpy as np

class PolicyOptimizer:
    """
    Optimizador de políticas con soporte para regularización por incertidumbre.
    Puede utilizarse con algoritmos como PPO, A2C o variaciones personalizadas.
    """

    def __init__(self, policy_model, learning_rate=0.01, entropy_coefficient=0.01):
        self.policy_model = policy_model
        self.learning_rate = learning_rate
        self.entropy_coefficient = entropy_coefficient

    def compute_loss(self, action_probs, advantages):
        """
        Calcula la pérdida compuesta por:
        - término de ventaja (mejorar política)
        - término de entropía (exploración)
        """
        log_probs = np.log(action_probs + 1e-10)
        entropy = -np.sum(action_probs * log_probs)
        policy_loss = -np.sum(log_probs * advantages)

        return policy_loss - self.entropy_coefficient * entropy

    def update_policy(self, states, actions, advantages):
        """
        Actualiza la política. Este método debe ser implementado por subclases
        específicas que definan cómo modificar los parámetros del modelo.
        """
        raise NotImplementedError("Debe implementarse update_policy().")
