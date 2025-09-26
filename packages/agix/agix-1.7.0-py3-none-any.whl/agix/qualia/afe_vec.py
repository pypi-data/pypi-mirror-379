"""Representación vectorial fija de estados emocionales."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Dict, Iterable

import numpy as np


@dataclass
class AffectiveVector:
    """Vector afectivo con emociones en orden fijo."""

    values: np.ndarray

    EMOTIONS: ClassVar[tuple[str, ...]] = (
        "alegría",
        "tristeza",
        "miedo",
        "enojo",
        "sorpresa",
        "curiosidad",
    )

    def __post_init__(self) -> None:
        expected = len(self.EMOTIONS)
        if self.values.shape != (expected,):
            raise ValueError(f"values must have shape ({expected},)")
        self.values = self.values.astype(float)

    # ------------------------------------------------------------------
    def to_dict(self) -> Dict[str, float]:
        """Convierte el vector en un diccionario de emociones."""
        return {e: float(self.values[i]) for i, e in enumerate(self.EMOTIONS)}

    # ------------------------------------------------------------------
    @classmethod
    def from_dict(
        cls, emociones: Dict[str, float] | Iterable[tuple[str, float]]
    ) -> "AffectiveVector":
        """Crea un ``AffectiveVector`` a partir de un diccionario."""
        if isinstance(emociones, dict):
            src = emociones
        else:
            src = dict(emociones)
        vec = np.array([src.get(e, 0.0) for e in cls.EMOTIONS], dtype=float)
        return cls(vec)

    # ------------------------------------------------------------------
    def __len__(self) -> int:  # útil en algunos contextos
        return len(self.EMOTIONS)
