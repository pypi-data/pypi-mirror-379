from __future__ import annotations

"""Simulador simple de emociones morales."""

from typing import Dict

from src.agix.qualia.affective_vector import AffectiveVector


class MoralEmotionSimulator(AffectiveVector):
    """Gestiona niveles de culpa, remordimiento y satisfacción."""

    def __init__(self) -> None:
        super().__init__({"culpa": 0.0, "remordimiento": 0.0, "satisfaccion": 0.0})

    def actualizar(self, juzgo: str) -> None:
        """Actualiza el estado emocional según el juicio ético recibido.

        Args:
            juzgo: Resultado de la evaluación ética. Puede ser "positivo" o "negativo".
        """

        if juzgo == "positivo":
            self.values["satisfaccion"] = min(self.values["satisfaccion"] + 0.1, 1.0)
            self.values["culpa"] = max(self.values["culpa"] - 0.1, 0.0)
            self.values["remordimiento"] = max(self.values["remordimiento"] - 0.1, 0.0)
        elif juzgo == "negativo":
            self.values["culpa"] = min(self.values["culpa"] + 0.1, 1.0)
            self.values["remordimiento"] = min(self.values["remordimiento"] + 0.1, 1.0)
            self.values["satisfaccion"] = max(self.values["satisfaccion"] - 0.1, 0.0)

    def estado(self) -> Dict[str, float]:
        """Devuelve una copia del estado emocional actual."""

        return self.to_dict()

    def reiniciar(self) -> None:
        """Resetea todos los valores a cero."""

        for clave in self.values:
            self.values[clave] = 0.0
