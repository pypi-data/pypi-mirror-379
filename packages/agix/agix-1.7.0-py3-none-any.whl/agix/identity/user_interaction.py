"""Sesión de interacción con el usuario que actualiza la identidad."""
from __future__ import annotations

from src.agix.identity.self_model import SelfModel
from src.agix.autonarrative.autonarrative_core import AutonarrativeCore, Experience


class UserInteractionSession:
    """Gestiona el diálogo con un usuario y su impacto en la identidad."""

    def __init__(self, self_model: SelfModel, narrative: AutonarrativeCore) -> None:
        self.self_model = self_model
        self.narrative = narrative
        self.history: list[tuple[str, str]] = []

    def _derive_trait(self, message: str) -> str | None:
        tokens = [t.strip().lower() for t in message.split() if t.strip()]
        return tokens[0] if tokens else None

    def receive_message(self, message: str) -> str:
        """Procesa un mensaje del usuario y devuelve la respuesta."""
        response = f"Entendido: {message}"
        self.history.append((message, response))

        trait = self._derive_trait(message)
        if trait:
            self.self_model.add_trait(trait)

        exp_text = f"U:{message} | A:{response}"
        metadata = {"traits": [trait] if trait else []}
        self.narrative.store_experience(Experience(text=exp_text, metadata=metadata))
        return response
