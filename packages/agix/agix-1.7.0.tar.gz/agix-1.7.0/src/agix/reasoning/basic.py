from typing import Dict, List, Optional

from src.agix.emotion.emotion_simulator import PADState


class Reasoner:
    """
    Selecciona el modelo óptimo basado en precisión e interpretabilidad.
    Útil para elegir entre múltiples modelos evaluados bajo criterios cuantitativos.
    """

    def __init__(self) -> None:
        self._pad = PADState()

    def modular_por_emocion(self, pad: PADState) -> None:
        """Registra el estado PAD para modular futuras evaluaciones."""
        self._pad = pad

    def select_best_model(self, evaluations: List[Dict]) -> Dict[str, Optional[str | float]]:
        if not evaluations:
            return {
                "name": None,
                "accuracy": 0.0,
                "reason": "No se proporcionaron modelos para evaluar.",
            }

        factor = 1 + 0.1 * (
            self._pad.placer + self._pad.activacion + self._pad.dominancia
        )
        mod: List[Dict] = []
        for m in evaluations:
            acc = max(0.0, min(1.0, m.get("accuracy", 0.0) * factor))
            mod.append({**m, "accuracy": acc})

        evaluations_sorted = sorted(mod, key=lambda m: m.get("accuracy", 0.0), reverse=True)
        best_accuracy = evaluations_sorted[0]["accuracy"]

        candidates = [m for m in evaluations_sorted if m.get("accuracy") == best_accuracy]

        final = sorted(candidates, key=lambda m: m.get("interpretability", 0.0), reverse=True)[0]

        reason = (
            f"Modelo seleccionado: '{final['name']}'\n"
            f"- Precisión: {final['accuracy']:.2f}\n"
            f"- Interpretabilidad: {final['interpretability']:.2f}"
        )

        return {
            "name": final.get("name"),
            "accuracy": final.get("accuracy"),
            "reason": reason,
        }

