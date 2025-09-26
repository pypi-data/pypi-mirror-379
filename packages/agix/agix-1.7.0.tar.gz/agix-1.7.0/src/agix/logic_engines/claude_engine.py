"""Motor para modelos Claude de Anthropic."""

from __future__ import annotations

from typing import Optional

from .base import LogicEngine


class ClaudeEngine(LogicEngine):
    """Integra la API de Anthropic para utilizar Claude."""

    def __init__(self, model: str = "claude-3-haiku", api_key: Optional[str] = None) -> None:
        self.model = model
        self.api_key = api_key
        self._client = None  # carga diferida

    def _ensure_client(self) -> None:
        if self._client is None:
            try:
                import anthropic
            except ImportError as exc:
                raise ImportError("Se requiere 'anthropic' para ClaudeEngine") from exc
            self._client = anthropic.Client(api_key=self.api_key)

    def infer(self, prompt: str) -> str:
        return self.generate(prompt)

    def generate(self, prompt: str) -> str:
        self._ensure_client()
        response = self._client.messages.create(
            model=self.model,
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}],
        )
        content = response.get("content")
        if isinstance(content, list) and content:
            item = content[0]
            return item.get("text", str(item))
        return str(content)
