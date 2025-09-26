"""Módulo de simulación emocional usando el modelo PAD (placer, activación, dominancia)."""

from dataclasses import dataclass
from typing import Dict, Optional, List, Any

from agix.qualia.qualia_core import EmotionalState


@dataclass
class PADState:
    """Representa el estado emocional en términos PAD."""

    placer: float = 0.0
    activacion: float = 0.0
    dominancia: float = 0.0

    def clamp(self, minimo: float = -1.0, maximo: float = 1.0) -> None:
        """Limita cada dimensión entre un rango dado."""
        self.placer = max(min(self.placer, maximo), minimo)
        self.activacion = max(min(self.activacion, maximo), minimo)
        self.dominancia = max(min(self.dominancia, maximo), minimo)


class EmotionSimulator:
    """Simula cambios emocionales básicos mediante reglas heurísticas."""

    def __init__(self, pesos: Optional[Dict[str, PADState]] = None, moduladores: Optional[List[Any]] = None):
        # Pesos que mapean claves de entrada a modificaciones en el estado PAD
        self.pesos: Dict[str, PADState] = pesos or {}
        self._estado = PADState()
        self._moduladores: List[Any] = moduladores or []

    def registrar_modulador(self, modulador: Any) -> None:
        """Registra un objeto con método ``modular_por_emocion``."""
        self._moduladores.append(modulador)

    def actualizar(self, entradas: dict, self_state: dict, qualia: EmotionalState) -> None:
        """
        Actualiza el estado PAD en función de entradas externas, variables internas y
        el estado emocional global proveniente de ``qualia``.
        """
        # Aplicar pesos sobre entradas externas e internas
        for origen in (entradas, self_state):
            for clave, valor in origen.items():
                if clave in self.pesos:
                    peso = self.pesos[clave]
                    self._estado.placer += peso.placer * float(valor)
                    self._estado.activacion += peso.activacion * float(valor)
                    self._estado.dominancia += peso.dominancia * float(valor)

        # Influencia básica del tono emocional general
        tono = qualia.tono_general()
        if tono == "alegría":
            self._estado.placer += 0.1
        elif tono == "miedo":
            self._estado.activacion += 0.1
            self._estado.dominancia -= 0.1
        elif tono == "ira":
            self._estado.activacion += 0.2
            self._estado.dominancia += 0.1

        # Limitar valores al rango [-1, 1]
        self._estado.clamp()

        estado_actual = self.estado()
        for modulador in self._moduladores:
            if hasattr(modulador, "modular_por_emocion"):
                modulador.modular_por_emocion(estado_actual)

    def estado(self) -> PADState:
        """Devuelve una copia del estado PAD actual."""
        return PADState(
            placer=self._estado.placer,
            activacion=self._estado.activacion,
            dominancia=self._estado.dominancia,
        )
