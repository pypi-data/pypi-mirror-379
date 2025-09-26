import numpy as np

from src.agix.adapters.base import DomainAdapter


class BiologyAdapter(DomainAdapter):
    """Procesa cadenas de ADN en vectores y mapea acciones a etiquetas biológicas."""

    def adapt_input(self, observation: str) -> np.ndarray:
        counts = [observation.count(n) for n in "ACGT"]
        vec = np.array(counts, dtype=float)
        if vec.size < 10:
            vec = np.pad(vec, (0, 10 - vec.size), constant_values=0)
        return vec[:10]

    def adapt_output(self, action: int) -> str:
        labels = ["gen", "proteína", "enzima"]
        return labels[action % len(labels)]
