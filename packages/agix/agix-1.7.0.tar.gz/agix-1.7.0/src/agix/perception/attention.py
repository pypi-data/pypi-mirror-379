# attention.py

from typing import Dict, Any

from src.agix.emotion.emotion_simulator import PADState
from src.agix.perception.sensor_map import SensorMap


class AttentionFocus:
    """
    Representa el foco de atención del agente sobre sus entradas sensoriales.
    """

    def __init__(self, sensor_map: SensorMap):
        self.sensor_map = sensor_map
        self.pesos: Dict[str, float] = {}  # nombre_sensor → peso (importancia)
        self.umbral_atencion = 0.5         # mínimo para ser considerado relevante

    def asignar_peso(self, nombre_sensor: str, peso: float):
        """Asigna un peso (0–1) a un sensor, indicando su importancia perceptual."""
        self.pesos[nombre_sensor] = max(0.0, min(1.0, peso))

    def obtener_entradas_relevantes(self) -> Dict[str, Any]:
        """
        Devuelve las entradas sensoriales que superan el umbral de atención.
        """
        entradas_relevantes = {}
        for nombre, sensor in self.sensor_map.sensores.items():
            peso = self.pesos.get(nombre, 0.0)
            if peso >= self.umbral_atencion and sensor.ultima_entrada is not None:
                entradas_relevantes[nombre] = sensor.ultima_entrada
        return entradas_relevantes

    def redirigir_atencion(self, nuevos_pesos: Dict[str, float]):
        """Permite reasignar pesos de atención en bloque."""
        for nombre, peso in nuevos_pesos.items():
            self.asignar_peso(nombre, peso)

    def modular_por_emocion(self, pad: PADState) -> None:
        """Modula pesos y umbral de atención según el estado emocional PAD."""
        factor = 1 + 0.2 * pad.activacion + 0.1 * pad.placer
        for nombre in list(self.pesos.keys()):
            nuevo = self.pesos[nombre] * factor
            self.pesos[nombre] = max(0.0, min(1.0, nuevo))
        self.umbral_atencion = max(
            0.0,
            min(1.0, 0.5 - 0.1 * pad.placer - 0.1 * pad.dominancia + 0.1 * pad.activacion),
        )

    def diagnostico(self) -> str:
        """Devuelve un resumen textual del foco de atención actual."""
        relevantes = self.obtener_entradas_relevantes()
        return f"Atención activa en {list(relevantes.keys())}"
