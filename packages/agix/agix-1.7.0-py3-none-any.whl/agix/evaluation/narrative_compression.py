import numpy as np
from difflib import SequenceMatcher
from typing import Sequence, Any, Dict


class NarrativeCompressionEvaluator:
    """Herramientas para evaluar la compresi\xc3\xb3n narrativa en la memoria."""

    @staticmethod
    def estimate_alpha(original_lengths: Sequence[float], recall_lengths: Sequence[float]) -> float:
        """Obtiene la pendiente \xce\xb1 mediante regresi\xc3\xb3n log-log."""
        if len(original_lengths) != len(recall_lengths):
            raise ValueError("Listas de distinta longitud")
        x = np.log(original_lengths)
        y = np.log(recall_lengths)
        slope, _ = np.polyfit(x, y, 1)
        return float(slope)

    @staticmethod
    def semantic_precision(original_text: str, recalled_text: str) -> float:
        """Calcula la similitud sem\xc3\xa1ntica entre dos textos."""
        return SequenceMatcher(None, original_text, recalled_text).ratio()

    @classmethod
    def evaluate(cls, memory_tree: Any, original_text: str) -> Dict[str, float]:
        """Recupera el recuerdo y devuelve alpha y precisi\xc3\xb3n."""
        recalled_text = memory_tree.retrieve()
        orig_len = len(original_text.split())
        recall_len = len(recalled_text.split())
        alpha = np.log(recall_len) / np.log(orig_len) if orig_len > 0 and recall_len > 0 else 0.0
        precision = cls.semantic_precision(original_text, recalled_text)
        return {"alpha": float(alpha), "precision": float(precision)}
