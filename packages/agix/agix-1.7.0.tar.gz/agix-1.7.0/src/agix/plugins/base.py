"""Interfaces para extensiones de estrategias."""

from abc import ABC, abstractmethod
from typing import Any


class StrategyPlugin(ABC):
    """Interfaz mínima para plugins de estrategia."""

    @abstractmethod
    def name(self) -> str:
        """Nombre único del plugin."""
        raise NotImplementedError

    @abstractmethod
    def apply(self, data: Any) -> Any:
        """Aplica la estrategia a los datos proporcionados."""
        raise NotImplementedError
