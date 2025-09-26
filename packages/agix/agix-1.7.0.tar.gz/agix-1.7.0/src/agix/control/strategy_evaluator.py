# strategy_evaluator.py

from typing import Dict, List


class StrategyPerformanceTracker:
    """Gestiona y resume el rendimiento de distintas estrategias."""

    def __init__(self) -> None:
        # Historial de recompensas por estrategia
        self.history: Dict[str, List[float]] = {}

    def register_result(self, name: str, reward: float) -> None:
        """Registra un nuevo resultado de recompensa para la estrategia."""
        self.history.setdefault(name, []).append(reward)

    def summary(self, name: str) -> Dict[str, float]:
        """Calcula promedio y tasa de éxito (>=0.5) para la estrategia."""
        rewards = self.history.get(name, [])
        if not rewards:
            return {"promedio": 0.0, "tasa_exito": 0.0}

        avg = sum(rewards) / len(rewards)
        success_count = sum(1 for r in rewards if r >= 0.5)
        success_rate = success_count / len(rewards)
        return {"promedio": avg, "tasa_exito": success_rate}

    def low_performance(self, name: str, threshold: float = 0.3, min_samples: int = 3) -> bool:
        """Indica si la estrategia tiene bajo rendimiento promedio."""
        rewards = self.history.get(name, [])
        if len(rewards) < min_samples:
            return False
        avg = sum(rewards) / len(rewards)
        return avg < threshold
