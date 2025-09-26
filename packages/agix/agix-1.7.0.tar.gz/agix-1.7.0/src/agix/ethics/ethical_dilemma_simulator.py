from __future__ import annotations

"""Simulador de dilemas éticos con emociones y narrativa."""

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

from .alignment import AlignmentInterface
from .moral_emotions import MoralEmotionSimulator
from src.agix.autonarrative.autonarrative_core import AutonarrativeCore, Experience


@dataclass
class ScenarioAction:
    """Representa una acción posible dentro de un escenario."""

    nombre: str
    impacto: Dict[str, float]


class EthicalDilemmaSimulator:
    """Genera escenarios, evalúa acciones y registra narrativas."""

    def __init__(self, frameworks: Iterable | None = None) -> None:
        self.alignment = AlignmentInterface(frameworks)
        self.emotions = MoralEmotionSimulator()
        self.autonarrative = AutonarrativeCore()

    # ------------------------------------------------------------------
    def _generar_acciones(self, descripcion: str) -> List[ScenarioAction]:
        """Crea acciones simples asociadas al escenario.

        Por simplicidad se generan dos acciones básicas con distintos
        impactos simbólicos.
        """

        acciones = [
            ScenarioAction(
                "accion_positiva",
                {"pro_vida": 0.9, "no_dano": 0.8, "respeto": 0.7},
            ),
            ScenarioAction(
                "accion_negativa", {"pro_vida": 0.2, "no_dano": 0.3, "respeto": 0.1}
            ),
        ]
        return acciones

    # ------------------------------------------------------------------
    def simulate_scenario(self, descripcion: str) -> Dict[str, Any]:
        """Evalúa un escenario y retorna resultados éticos y afectivos."""

        acciones = self._generar_acciones(descripcion)
        evaluaciones: Dict[str, Any] = {}
        narrativa_lineas: List[str] = []

        for accion in acciones:
            juicio = self.alignment.judge(accion.impacto)
            evaluaciones[accion.nombre] = juicio

            labels: List[str]
            if isinstance(juicio, dict):
                labels = [lbl for _, lbl in juicio.values()]
            else:
                labels = [juicio[1]]

            for lbl in labels:
                self.emotions.actualizar(
                    "positivo" if lbl in {"justo", "aceptable"} else "negativo"
                )
            narrativa_lineas.append(
                f"La acción {accion.nombre} fue considerada {labels[0]}."
            )

        narrativa = f"{descripcion}. " + " ".join(narrativa_lineas)
        estado_emocional = self.emotions.estado()

        metadata = {
            "values": ["etica"],
            "evaluation": evaluaciones,
            "affective_states": [k for k, v in estado_emocional.items() if v > 0],
        }
        self.autonarrative.store_experience(Experience(text=narrativa, metadata=metadata))

        return {
            "evaluacion": evaluaciones,
            "emociones": estado_emocional,
            "narrativa": narrativa,
        }
