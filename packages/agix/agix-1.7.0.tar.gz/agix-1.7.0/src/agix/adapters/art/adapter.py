import numpy as np

from src.agix.adapters.base import DomainAdapter


class ArtAdapter(DomainAdapter):
    """Normaliza vectores de pixeles y traduce acciones a estilos artísticos."""

    def adapt_input(self, observation) -> np.ndarray:
        vec = np.asarray(observation, dtype=float)
        if vec.size < 10:
            vec = np.pad(vec, (0, 10 - vec.size), constant_values=0)
        vec = vec[:10]
        if vec.max() > 0:
            vec = vec / 255.0
        return vec

    def adapt_output(self, action: int) -> str:
        styles = ["abstracto", "realista", "impresionista"]
        return styles[action % len(styles)]
