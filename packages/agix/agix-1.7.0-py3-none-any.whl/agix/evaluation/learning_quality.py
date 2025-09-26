# learning_quality.py

from typing import List
import numpy as np


class LearningQualityEvaluator:
    """
    Evalúa la calidad del aprendizaje del agente según:
    - Consistencia
    - Tendencia de mejora
    - Estabilidad (baja varianza)
    - Capacidad de recuperación (resiliencia)
    """

    def __init__(self):
        pass

    def consistencia(self, recompensas: List[float]) -> float:
        """
        Mide qué tan cerca están las recompensas de su media (alta = consistente).
        """
        if not recompensas:
            return 0.0
        media = np.mean(recompensas)
        desviacion = np.std(recompensas)
        return round(1.0 - (desviacion / (media + 1e-6)), 3)

    def tendencia_mejora(self, recompensas: List[float]) -> float:
        """
        Evalúa si hay una tendencia positiva en la curva de aprendizaje.
        """
        if len(recompensas) < 2:
            return 0.0
        x = np.arange(len(recompensas))
        coef = np.polyfit(x, recompensas, 1)[0]  # pendiente
        return round(max(0.0, coef / (np.max(recompensas) + 1e-6)), 3)

    def estabilidad(self, recompensas: List[float]) -> float:
        """
        Inversa de la varianza: mayor valor = más estable.
        """
        if not recompensas:
            return 0.0
        varianza = np.var(recompensas)
        return round(1.0 / (varianza + 1e-6), 3)

    def evaluacion_global(self, recompensas: List[float]) -> float:
        """
        Combina todas las métricas en un índice de calidad del aprendizaje.
        """
        c = self.consistencia(recompensas)
        t = self.tendencia_mejora(recompensas)
        e = self.estabilidad(recompensas)
        score = (0.4 * c) + (0.3 * t) + (0.3 * e)
        return round(score, 3)
