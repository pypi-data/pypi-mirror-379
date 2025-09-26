# src/agix/evaluation/formal/cognitive_games.py

import random

class TheoryOfMindGame:
    """
    Juego simple para evaluar teoría de la mente en agentes.
    El agente debe predecir la acción de otro agente (modelo mental).
    """

    def __init__(self, agent_under_test, simulated_agent):
        """
        agent_under_test: el agente que debe inferir la intención del otro
        simulated_agent: el agente simulado cuya acción se intentará predecir
        """
        self.agent = agent_under_test
        self.other = simulated_agent
        self.state_space = ["A", "B", "C"]

    def reset(self):
        self.state = random.choice(self.state_space)
        self.goal = random.choice(self.state_space)
        return {"state": self.state, "goal": self.goal}

    def step(self):
        """
        Ejecuta una predicción: el agente debe inferir qué acción tomará el otro agente.
        """
        obs = {"state": self.state, "goal": self.goal}
        predicted_action = self.agent.predict_others_action(obs)
        actual_action = self.other.decide(obs)

        success = predicted_action == actual_action
        return success
