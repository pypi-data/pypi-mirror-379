"""Herramientas para monitorizar la auto-organización del sistema."""

from __future__ import annotations

from typing import Iterable
import statistics


class SelfOrganizationMonitor:
    """Evalúa la complejidad y coherencia del sistema.

    Parámetros:
        active_modules: nombres de los módulos actualmente activos.
        dependencies: mapa que relaciona cada módulo con sus dependencias.
        activation_times: momentos de activación de cada módulo.
    """

    def __init__(
        self,
        active_modules: Iterable[str] | None = None,
        dependencies: dict[str, list[str]] | None = None,
        activation_times: Iterable[float] | None = None,
    ) -> None:
        self.active_modules = list(active_modules or [])
        self.dependencies = dependencies or {}
        self.activation_times = list(activation_times or [])

    def module_complexity(self) -> float:
        """Calcula la complejidad según los módulos activos.

        Devuelve un valor normalizado en el rango ``0-1`` donde valores
        altos indican una mayor cantidad de módulos interactuando.
        """
        count = len(self.active_modules)
        return count / (count + 1)

    def interdependency_complexity(self) -> float:
        """Normaliza las interdependencias entre módulos.

        Un mayor número de conexiones implica una organización más densa.
        El resultado se limita al rango ``0-1``.
        """
        n = len(self.active_modules)
        if n <= 1:
            return 0.0
        total_possible = n * (n - 1)
        actual = sum(len(deps) for deps in self.dependencies.values())
        return min(actual / total_possible, 1.0)

    def temporal_coherence(self) -> float:
        """Mide la regularidad temporal de las activaciones.

        Valores cercanos a ``1`` reflejan activaciones periódicas y
        predecibles, mientras que un ``0`` indica completa irregularidad.
        """
        times = self.activation_times
        if len(times) < 2:
            return 0.0
        intervals = [t2 - t1 for t1, t2 in zip(times[:-1], times[1:])]
        if len(intervals) < 2:
            return 1.0
        std = statistics.pstdev(intervals)
        return 1 / (1 + std)

    def compute_score(self) -> float:
        """Devuelve una puntuación de auto-organización entre 0 y 1."""
        metrics = [
            self.module_complexity(),
            self.interdependency_complexity(),
            self.temporal_coherence(),
        ]
        score = statistics.fmean(metrics)
        return max(0.0, min(score, 1.0))
