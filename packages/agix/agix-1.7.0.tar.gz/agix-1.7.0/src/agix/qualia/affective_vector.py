from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class AffectiveVector:
    """Representación simple de un estado emocional."""

    values: Dict[str, float]

    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> "AffectiveVector":
        """Crea un vector a partir de un diccionario."""
        return cls(data.copy())

    def to_dict(self) -> Dict[str, float]:
        """Convierte el vector en un diccionario nuevo."""
        return self.values.copy()
