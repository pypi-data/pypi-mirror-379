"""Motor especializado para modelos BLOOM."""

from .hf_engine import HFEngine


class BLOOMEngine(HFEngine):
    """Configura ``HFEngine`` con un modelo BLOOM por defecto."""

    def __init__(self, model_name: str = "bigscience/bloom-560m") -> None:
        super().__init__(model_name=model_name)
