"""Motor especializado para modelos LLaMA."""

from .hf_engine import HFEngine


class LLaMAEngine(HFEngine):
    """Configura ``HFEngine`` con un modelo LLaMA por defecto."""

    def __init__(self, model_name: str = "meta-llama/Llama-2-7b-hf") -> None:
        super().__init__(model_name=model_name)
