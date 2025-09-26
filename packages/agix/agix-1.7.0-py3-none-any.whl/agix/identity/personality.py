from dataclasses import dataclass
from agix.qualia.qualia_core import EmotionalState


@dataclass
class PersonalityProfile:
    """Perfil simple de personalidad."""

    optimismo: float = 0.5
    introversion: float = 0.5
    energia: float = 0.5

    def apply(self, emotional_state: EmotionalState) -> None:
        """Ajusta ``emotional_state`` según los rasgos."""
        # Alegría aumenta con el optimismo
        emotional_state.sentir("alegría", self.optimismo)
        # Tristeza complementa el optimismo
        emotional_state.sentir("tristeza", max(0.0, 1 - self.optimismo))
        # Curiosidad depende de la energía atenuada por la introversión
        curiosidad = max(0.0, self.energia * (1 - self.introversion))
        if curiosidad:
            emotional_state.sentir("curiosidad", curiosidad)
