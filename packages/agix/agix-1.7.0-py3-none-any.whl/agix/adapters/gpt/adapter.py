from __future__ import annotations

from typing import Callable

from ..base import DomainAdapter
from src.agix.language.emotional_translator import SemanticEmotionalTranslator


class GPTQualiaAdapter(DomainAdapter):
    """Adaptador para interactuar con un modelo tipo GPT."""

    def __init__(
        self,
        client: Callable[[str], str],
        source_lang: str = "es",
        target_lang: str = "en",
    ) -> None:
        self.client = client
        self.translator = SemanticEmotionalTranslator()
        self.source_lang = source_lang
        self.target_lang = target_lang

    # ------------------------------------------------------------------
    def adapt_input(self, observation: str) -> str:
        """Prepara el mensaje para el modelo GPT."""
        return observation

    # ------------------------------------------------------------------
    def adapt_output(self, action: str) -> str:
        """Traduce términos emocionales en la respuesta."""
        return self.translator.translate(
            action, source_lang=self.source_lang, target_lang=self.target_lang
        )

    # ------------------------------------------------------------------
    def generate_reply(self, prompt: str) -> str:
        """Obtiene una respuesta del cliente GPT traduciendo las emociones."""
        prompt = self.adapt_input(prompt)
        raw = self.client(prompt)
        return self.adapt_output(raw)
