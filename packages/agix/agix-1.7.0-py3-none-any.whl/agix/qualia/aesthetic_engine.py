# aesthetic_engine.py

from typing import Dict
import numpy as np


class AestheticEngine:
    """
    Motor de evaluación estética.
    Evalúa armonía, simetría y carga emocional simbólica en entradas cognitivas.
    """

    def __init__(self):
        self.preferencias = {
            "simetría": 0.7,
            "coherencia": 0.8,
            "emotividad": 0.9
        }

    def evaluar(self, entrada: Dict[str, float]) -> float:
        """
        Calcula una puntuación estética ponderada a partir de atributos:
        entrada = {
            "simetría": 0.6,
            "coherencia": 0.7,
            "emotividad": 0.9
        }
        """
        score = 0.0
        total_peso = sum(self.preferencias.values())

        for k, peso in self.preferencias.items():
            valor = entrada.get(k, 0.0)
            score += peso * valor

        return round(score / total_peso, 3)

    def clasificar(self, score: float) -> str:
        """
        Devuelve una categoría estética simbólica según el score.
        """
        if score > 0.85:
            return "sublime"
        elif score > 0.65:
            return "armonioso"
        elif score > 0.4:
            return "neutro"
        else:
            return "discordante"
