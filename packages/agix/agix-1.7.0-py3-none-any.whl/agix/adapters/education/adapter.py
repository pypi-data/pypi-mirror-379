import numpy as np
from ..base import DomainAdapter


class EducationAdapter(DomainAdapter):
    """Convierte interacciones genéricas a un formato educativo simple."""

    def adapt_input(self, observation: str) -> np.ndarray:
        """Codifica texto y lo expande a un vector de longitud 10."""
        length = len(observation)
        vec = np.full(10, float(length))
        return vec

    def adapt_output(self, action: int) -> str:
        """Mapea acciones numéricas a sugerencias pedagógicas."""
        mapping = {0: "continuar", 1: "repasar", 2: "evaluar"}
        return mapping.get(action, "continuar")
