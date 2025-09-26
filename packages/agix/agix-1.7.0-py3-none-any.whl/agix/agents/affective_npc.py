# agix/agents/affective_npc.py

from __future__ import annotations

from typing import List, Optional

from src.agix.agents.base import AGIAgent
from src.agix.qualia.spirit import QualiaSpirit


class AffectiveNPC(AGIAgent):
    """Agente no jugador con estado emocional simple y memoria experiencial."""

    def __init__(self, action_space_size: int = 2, qualia: Optional[QualiaSpirit] = None):
        qualia = qualia or QualiaSpirit(nombre="NPC")
        super().__init__(name="AffectiveNPC", qualia=qualia)
        self.action_space_size = action_space_size
        self.last_observation: str | None = None
        self.last_action: int = 0
        self.reward_history: List[float] = []

    # ------------------------------------------------------------------
    def perceive(self, observation):
        """Guarda la última observación percibida y actualiza el estado emocional."""
        if isinstance(observation, (list, tuple)):
            self.last_observation = str(list(observation))
        else:
            self.last_observation = str(observation)
        super().perceive(observation)

    def decide(self, pad: 'PADState | None' = None) -> int:
        """Decide la acción basándose en el historial de recompensas y emociones."""
        pad = super().decide(pad)
        avg_reward = sum(self.reward_history) / len(self.reward_history) if self.reward_history else 0.0
        alegria = 0.0
        if self.qualia:
            alegria = self.qualia.estado_emocional.emociones.get("alegría", 0.0)
        if avg_reward + alegria >= 0:
            self.last_action = 0
        else:
            self.last_action = 1 % self.action_space_size
        return self.last_action

    def learn(self, reward, done: bool = False):
        """Actualiza el estado emocional y registra la experiencia."""
        self.reward_history.append(float(reward))
        if self.qualia:
            emocion = "alegría" if reward >= 0 else "tristeza"
            self.feel(f"reward:{reward}", abs(float(reward)), emocion)
        if self.last_observation is not None:
            self.record_experience(
                self.last_observation,
                str(self.last_action),
                f"reward:{reward}",
                exito=reward >= 0,
            )

    def reset(self):
        super().reset()
        self.last_observation = None
        self.last_action = 0
        self.reward_history.clear()
