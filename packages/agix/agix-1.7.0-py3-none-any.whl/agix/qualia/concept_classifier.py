"""Clasificador conceptual basado en NeuroSymbolicBridge."""

from typing import Dict, List
import numpy as np

from src.agix.reasoning.neuro_symbolic import NeuroSymbolicBridge
from src.agix.memory.symbolic import SymbolicConcept


class ConceptClassifier:
    """Asigna categorías a conceptos según similitud latente."""

    def __init__(self, dim: int = 32) -> None:
        self.bridge = NeuroSymbolicBridge(dim=dim)
        self.centroids: Dict[str, np.ndarray] = {}
        self.examples: Dict[str, List[str]] = {}

    def register_category(self, name: str, examples: List[str]) -> None:
        """Registra una categoría con ejemplos iniciales."""
        self.examples[name] = examples
        vectors = []
        for ex in examples:
            self.bridge.add_concept(SymbolicConcept(ex))
            vectors.append(self.bridge.symbolic_to_vector(ex))
        self.centroids[name] = np.mean(vectors, axis=0)

    def categorize(self, text: str) -> str:
        """Devuelve la categoría más similar para el texto dado."""
        vec = self.bridge.symbolic_to_vector(text)
        best_name = None
        best_score = -float("inf")
        for name, centroid in self.centroids.items():
            score = float(np.dot(vec, centroid) / (np.linalg.norm(vec) * np.linalg.norm(centroid)))
            if score > best_score:
                best_score = score
                best_name = name
        return best_name if best_name is not None else ""
