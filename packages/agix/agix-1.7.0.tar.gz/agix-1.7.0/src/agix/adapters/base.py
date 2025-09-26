from abc import ABC, abstractmethod
from typing import Any


class DomainAdapter(ABC):
    """Interfaz común para adaptar datos de entrada y salida de un agente."""

    @abstractmethod
    def adapt_input(self, observation: Any) -> Any:
        """Transforma la observación del entorno al formato del dominio."""
        raise NotImplementedError

    @abstractmethod
    def adapt_output(self, action: Any) -> Any:
        """Convierte la acción del agente a una representación interpretable."""
        raise NotImplementedError
