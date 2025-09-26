"""Traducción sencilla de términos emocionales entre idiomas."""

from __future__ import annotations

from typing import Dict, Tuple


class SemanticEmotionalTranslator:
    """Realiza traducciones básicas de palabras emocionales."""

    def __init__(self) -> None:
        # Diccionario interno organizado por pares (origen, destino)
        base = {
            "felicidad": "happiness",
            "tristeza": "sadness",
            "ira": "anger",
            "miedo": "fear",
            "sorpresa": "surprise",
            "asco": "disgust",
        }
        self._dictionary: Dict[Tuple[str, str], Dict[str, str]] = {
            ("es", "en"): base,
            ("en", "es"): {v: k for k, v in base.items()},
        }

    # ------------------------------------------------------------------
    def add_mapping(self, source_lang: str, target_lang: str, mapping: Dict[str, str]) -> None:
        """Añade traducciones personalizadas."""
        self._dictionary[(source_lang, target_lang)] = mapping

    # ------------------------------------------------------------------
    def translate(self, text: str, source_lang: str = "es", target_lang: str = "en") -> str:
        """Traduce palabra o frase de un idioma a otro."""
        mapping = self._dictionary.get((source_lang, target_lang), {})
        words = text.split()
        translated = [mapping.get(w.lower(), w) for w in words]
        return " ".join(translated)
