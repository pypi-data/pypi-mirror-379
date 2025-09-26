# agi_lab/environments/env_base.py

from abc import ABC, abstractmethod
import numpy as np

class AGIEnvironment(ABC):
    """
    Interfaz base para entornos compatibles con agentes de AGI.
    Inspirado en Gym, pero más general para tareas cognitivas simbólicas o conexionistas.
    """

    def __init__(self):
        self.observation_space = None
        self.action_space = None

    @abstractmethod
    def reset(self):
        """
        Reinicia el entorno a su estado inicial y devuelve la primera observación.
        """
        pass

    @abstractmethod
    def step(self, action):
        """
        Ejecuta una acción y devuelve:
        - nueva observación
        - recompensa
        - done (booleano si el episodio termina)
        - info (diccionario opcional)
        """
        pass

    @abstractmethod
    def render(self):
        """
        Representa visualmente el entorno (opcional).
        """
        pass

class SimpleEnvironment:
    """
    Entorno simulado mínimo para pruebas de agentes.
    Genera observaciones aleatorias y recompensa al azar.
    """
    def __init__(self, input_size=8, action_space_size=4, max_steps=10):
        self.input_size = input_size
        self.action_space_size = action_space_size
        self.max_steps = max_steps
        self.steps = 0

    def reset(self):
        self.steps = 0
        return np.random.rand(self.input_size)

    def step(self, action):
        self.steps += 1
        reward = 1.0 if action == 0 else 0.0
        done = self.steps >= self.max_steps
        obs = np.random.rand(self.input_size)
        return obs, reward, done, {}
