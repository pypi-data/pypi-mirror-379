from __future__ import annotations

"""Interface simple para evaluar alineamiento ético."""

from typing import Dict, Iterable, Tuple

from src.agix.qualia.ecoethics import EcoEthics
from .frameworks import (
    DeontologicalEthics,
    UtilitarianEthics,
    VirtueEthics,
)


class AlignmentInterface:
    """Evalúa acciones usando uno o varios marcos éticos."""

    def __init__(self, frameworks: Iterable | None = None):
        if frameworks is None:
            frameworks = [EcoEthics()]
        elif not isinstance(frameworks, (list, tuple)):
            frameworks = [frameworks]
        self.frameworks = list(frameworks)

    def judge(self, action: Dict[str, float]):
        """Devuelve los resultados de evaluación.

        Si sólo hay un marco configurado, retorna ``(score, clasificacion)``.
        Con múltiples marcos se devuelve un diccionario ``{nombre: (score, label)}``.
        """

        results = {}
        for marco in self.frameworks:
            score = marco.evaluar(action)
            label = marco.clasificar(score)
            results[marco.__class__.__name__] = (score, label)

        return next(iter(results.values())) if len(results) == 1 else results
