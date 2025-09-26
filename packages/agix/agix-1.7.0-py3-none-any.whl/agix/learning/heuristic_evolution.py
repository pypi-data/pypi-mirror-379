"""Herramientas heurísticas de evolución para agentes genéticos."""

from __future__ import annotations

from typing import List

import numpy as np

from src.agix.memory.experiential import GestorDeMemoria


class HeuristicEvolution:
    """Generación y selección de parámetros basada en heurísticas."""

    def __init__(self, param_len: int = 10):
        self.param_len = param_len

    # ------------------------------------------------------------------
    def generar_parametros(self, memoria: GestorDeMemoria) -> np.ndarray:
        """Crea un vector de parámetros usando estadísticas de la memoria."""
        if not memoria.experiencias:
            return np.random.uniform(-1, 1, self.param_len)

        ratio_exito = sum(exp.exito for exp in memoria.experiencias) / len(memoria.experiencias)
        base = np.full(self.param_len, ratio_exito)
        ruido = 0.1 * np.random.normal(size=self.param_len)
        return base + ruido

    # ------------------------------------------------------------------
    def seleccionar_mejores(self, poblacion: List[np.ndarray], fitness: List[float]) -> List[np.ndarray]:
        """Devuelve la mitad superior de la población según fitness."""
        if not poblacion or not fitness:
            return []
        indices = np.argsort(fitness)[::-1]
        top_n = max(1, len(poblacion) // 2)
        return [poblacion[i] for i in indices[:top_n]]
