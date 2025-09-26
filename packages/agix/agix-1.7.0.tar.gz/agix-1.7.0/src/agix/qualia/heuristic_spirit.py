"""HeuristicQualiaSpirit: version heurística del espíritu."""

from __future__ import annotations

from typing import Callable, List, Tuple

from .spirit import QualiaSpirit
from .heuristic_creator import HeuristicConceptCreator


class HeuristicQualiaSpirit(QualiaSpirit):
    """Extiende ``QualiaSpirit`` aplicando reglas heurísticas."""

    def __init__(self, nombre: str = "Qualia", edad_aparente: int = 7, plasticidad: bool = False) -> None:
        super().__init__(nombre=nombre, edad_aparente=edad_aparente, plasticidad=plasticidad)
        self.rules: List[Callable[[str, float], Tuple[str, float]]] = []

    # ------------------------------------------------------------------
    def add_rule(self, rule: Callable[[str, float], Tuple[str, float]]) -> None:
        """Registra una regla heurística para ajustar emoción e intensidad."""
        self.rules.append(rule)

    # ------------------------------------------------------------------
    def experimentar(self, evento: str, carga: float, tipo_emocion: str = "sorpresa") -> None:
        """Genera un concepto heurístico y aplica reglas antes de registrar."""
        concepto = self.creator.create([tipo_emocion, evento.replace(" ", "_")])
        emocion = concepto.name
        for rule in self.rules:
            emocion, carga = rule(emocion, carga)
        super().experimentar(evento, carga, emocion)
