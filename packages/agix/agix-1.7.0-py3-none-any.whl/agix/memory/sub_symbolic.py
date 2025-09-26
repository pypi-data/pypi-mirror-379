import numpy as np
from typing import Dict

class LatentRepresentation:
    """
    Representación subsimbólica (embedding) de conceptos, experiencias o percepciones.
    """

    def __init__(self, dim: int = 32):
        self.dim: int = dim
        self.embeddings: Dict[str, np.ndarray] = {}

    def encode(self, key: str) -> np.ndarray:
        """
        Devuelve el embedding de un concepto. Si no existe, lo crea aleatoriamente.
        """
        if key not in self.embeddings:
            self.embeddings[key] = np.random.normal(0, 1, self.dim)
        return self.embeddings[key]

    def similarity(self, key1: str, key2: str) -> float:
        v1 = self.encode(key1)
        v2 = self.encode(key2)
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

    def distance(self, key1: str, key2: str) -> float:
        v1 = self.encode(key1)
        v2 = self.encode(key2)
        return float(np.linalg.norm(v1 - v2))

    def project(self, key: str, direction: np.ndarray, alpha: float = 0.1):
        """
        Proyecta un vector en una dirección dada (por ejemplo, durante aprendizaje o reflexión).
        """
        self.embeddings[key] = self.encode(key) + alpha * direction
