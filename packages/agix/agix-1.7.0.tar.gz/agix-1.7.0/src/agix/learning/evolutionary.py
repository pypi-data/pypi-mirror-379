# evolutionary.py

import numpy as np
from typing import List

from src.agix.learning.meta_learning import MetaLearner


class EvolutionaryEngine:
    """
    Motor de evolución genética para agentes AGI.
    Aplica selección elitista, cruce, mutación y transformación meta-aprendizaje.
    """

    def __init__(self, mutation_rate: float = 0.1, elite_ratio: float = 0.2, meta_strategy: str = None):
        self.mutation_rate = mutation_rate
        self.elite_ratio = elite_ratio
        self.meta_learner = MetaLearner(strategy=meta_strategy) if meta_strategy else None

    def evaluate_population(self, agents: List, environment) -> np.ndarray:
        """
        Evalúa cada agente en el entorno y devuelve una lista de recompensas acumuladas.
        """
        scores = []
        for agent in agents:
            obs = environment.reset()
            total_reward = 0
            done = False
            while not done:
                agent.perceive(obs)
                action = agent.decide()
                obs, reward, done, _ = environment.step(action)
                agent.learn(reward)
                total_reward += reward
            scores.append(total_reward)
        return np.array(scores)

    def evolve(self, agents: List, scores: np.ndarray) -> List:
        """
        Realiza el ciclo evolutivo:
        1. Selección elitista
        2. Cruce genético
        3. Mutación
        4. (Opcional) Meta-aprendizaje
        """
        sorted_indices = np.argsort(scores)[::-1]
        elite_count = max(1, int(self.elite_ratio * len(agents)))
        elites = [agents[i] for i in sorted_indices[:elite_count]]

        new_population = elites.copy()
        while len(new_population) < len(agents):
            parents = np.random.choice(elites, 2, replace=True)
            child = parents[0].evolve(parents[1])

            if self.meta_learner:
                child = self.meta_learner.transform(child)

            new_population.append(child)

        return new_population
