"""Entornos de videojuegos para AGI."""

from .env_base import AGIEnvironment
import numpy as np


class VideoGameEnvironment(AGIEnvironment):
    """Interfaz genérica para videojuegos basada en ``AGIEnvironment``.

    Permite conectar con engines como Pygame o Unity. La implementación por
    defecto genera observaciones aleatorias para propósitos de prueba.
    """

    def __init__(self, engine: str = "pygame", obs_size: int = 8, action_space_size: int = 4, max_steps: int = 10):
        super().__init__()
        self.engine = engine
        self.obs_size = obs_size
        self.action_space_size = action_space_size
        self.max_steps = max_steps
        self.steps = 0

    def reset(self):
        self.steps = 0
        # Aquí se inicializaría el motor de juego real
        return np.zeros(self.obs_size)

    def step(self, action):
        self.steps += 1
        reward = 1.0 if action == 0 else 0.0
        done = self.steps >= self.max_steps
        obs = np.random.rand(self.obs_size)
        return obs, reward, done, {}

    def render(self):
        # En una integración real se delegaría al motor seleccionado
        pass
