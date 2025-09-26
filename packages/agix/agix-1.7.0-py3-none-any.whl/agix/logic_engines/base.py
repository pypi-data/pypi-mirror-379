from abc import ABC, abstractmethod


class LogicEngine(ABC):
    """Interfaz común para motores lógicos."""

    @abstractmethod
    def infer(self, prompt: str) -> str:
        """Realiza una inferencia a partir de un *prompt*."""
        raise NotImplementedError

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Genera texto a partir de un *prompt*."""
        raise NotImplementedError
