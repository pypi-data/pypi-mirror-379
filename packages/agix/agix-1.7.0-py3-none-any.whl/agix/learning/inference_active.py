# inference_active.py

import numpy as np
from typing import List
from typing import Any


class ActiveInferenceAgent:
    """
    Agente que utiliza inferencia activa para minimizar la entropía de sus creencias
    sobre el entorno y sus estados internos.
    """

    def __init__(self, action_space: List, state_space: List, prior_beliefs: np.ndarray = None):
        self.action_space = action_space
        self.state_space = state_space
        self.beliefs = (
            prior_beliefs
            if prior_beliefs is not None
            else np.ones(len(state_space)) / len(state_space)
        )

    def update_beliefs(self, observation: Any):
        """
        Actualiza las creencias con una regla bayesiana simple.
        """
        likelihood = self.compute_likelihood(observation)
        self.beliefs *= likelihood
        self.beliefs /= np.sum(self.beliefs)

    def compute_likelihood(self, observation: Any) -> np.ndarray:
        """
        Debe devolver una probabilidad condicional P(observation | state).
        """
        raise NotImplementedError("Debe implementarse compute_likelihood().")

    def select_action(self):
        """
        Selecciona una acción. Por defecto, aleatoria.
        Idealmente se extenderá para minimizar la entropía esperada.
        """
        return np.random.choice(self.action_space)

