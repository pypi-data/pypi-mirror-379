# sensor_map.py

from typing import Dict, Any, Callable


class Sensor:
    """
    Representa un sensor individual que puede recibir y procesar datos del entorno.
    """

    def __init__(self, nombre: str, tipo: str, procesador: Callable[[Any], Any] = None):
        """
        - nombre: identificador único del sensor
        - tipo: categoría (ej. 'visual', 'auditivo', 'interno', etc.)
        - procesador: función para transformar o validar los datos recibidos
        """
        self.nombre = nombre
        self.tipo = tipo
        self.procesador = procesador or (lambda x: x)
        self.ultima_entrada = None

    def recibir(self, datos: Any):
        """
        Recibe y procesa una nueva entrada sensorial.
        """
        self.ultima_entrada = self.procesador(datos)

    def obtener_estado(self) -> dict:
        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "ultima_entrada": self.ultima_entrada
        }


class SensorMap:
    """
    Mapa global de sensores activos. Puede usarse para construir un estado perceptual general.
    """

    def __init__(self):
        self.sensores: Dict[str, Sensor] = {}

    def registrar_sensor(self, sensor: Sensor):
        self.sensores[sensor.nombre] = sensor

    def enviar_entrada(self, nombre_sensor: str, datos: Any):
        if nombre_sensor in self.sensores:
            self.sensores[nombre_sensor].recibir(datos)

    def estado_completo(self) -> dict:
        return {nombre: sensor.obtener_estado() for nombre, sensor in self.sensores.items()}

    def sensores_por_tipo(self, tipo: str) -> list:
        return [s for s in self.sensores.values() if s.tipo == tipo]
