# agi_lab/agents/genetic.py

import numpy as np
from typing import Optional

from src.agix.agents.base import AGIAgent
from src.agix.qualia.spirit import QualiaSpirit


class GeneticAgent(AGIAgent):
    """
    Agente basado en evolución genética.
    Utiliza una política representada por un vector de parámetros que evoluciona
    mediante selección, cruce y mutación.
    """

    def __init__(
        self,
        action_space_size,
        chromosome_length=10,
        mutation_rate=0.1,
        qualia: Optional[QualiaSpirit] = None,
    ):
        super().__init__(name="GeneticAgent", qualia=qualia)
        self.action_space_size = action_space_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.chromosome = np.random.uniform(-1, 1, size=(chromosome_length,))
        self.last_observation = None

    def perceive(self, observation):
        self.last_observation = observation
        super().perceive(observation)

    def decide(self, pad: 'PADState | None' = None):
        pad = super().decide(pad)
        if self.last_observation is None:
            return np.random.randint(self.action_space_size)

        # Simple política lineal sobre la observación
        obs_vector = np.asarray(self.last_observation).flatten()
        obs_vector = obs_vector[:self.chromosome_length]  # truncar si es más larga
        weighted_sum = np.dot(self.chromosome, obs_vector)
        action = int(abs(weighted_sum)) % self.action_space_size
        return action

    def learn(self, reward, done=False):
        """
        Ajusta el cromosoma con una mutación proporcional al reward recibido.
        Esto es un placeholder de mutación local.
        """
        mutation = np.random.normal(0, self.mutation_rate, size=self.chromosome.shape)
        self.chromosome += reward * mutation

    def evolve(self, other_agent):
        """
        Crea un descendiente cruzando cromosomas con otro agente.
        """
        child = GeneticAgent(self.action_space_size, self.chromosome_length, self.mutation_rate)
        mask = np.random.randint(0, 2, size=self.chromosome.shape)
        child.chromosome = mask * self.chromosome + (1 - mask) * other_agent.chromosome
        return child

    def reset(self):
        super().reset()
        self.chromosome = np.random.uniform(-1, 1, size=(self.chromosome_length,))
