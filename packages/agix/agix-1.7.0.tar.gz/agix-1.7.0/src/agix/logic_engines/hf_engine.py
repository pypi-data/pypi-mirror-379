"""Motor basado en modelos de Hugging Face."""

from __future__ import annotations

from typing import Optional

from .base import LogicEngine


class HFEngine(LogicEngine):
    """Utiliza la librería ``transformers`` para generar texto."""

    def __init__(self, model_name: str = "gpt2") -> None:
        self.model_name = model_name
        self._pipe = None  # carga diferida

    def _ensure_pipeline(self) -> None:
        if self._pipe is None:
            try:
                from transformers import pipeline
            except ImportError as exc:
                raise ImportError("Se requiere 'transformers' para HFEngine") from exc
            self._pipe = pipeline("text-generation", model=self.model_name)

    def infer(self, prompt: str) -> str:
        return self.generate(prompt)

    def generate(self, prompt: str) -> str:
        self._ensure_pipeline()
        result = self._pipe(prompt, max_new_tokens=50)
        return result[0]["generated_text"]
