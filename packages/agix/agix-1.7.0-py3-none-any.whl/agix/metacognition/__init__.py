"""Componentes de metacognición para AGIX."""

from .self_organization import SelfOrganizationMonitor
from .intention_evaluator import IntentionEvaluator
from .metareflection_engine import MetaReflectionEngine, InternalVoice

__all__ = [
    "MetaReflectionEngine",
    "InternalVoice",
    "IntentionEvaluator",
    "SelfOrganizationMonitor",
]

try:  # pragma: no cover - dependencias opcionales
    from .manager import MetacognitionManager
    from .dynamic_evaluator import DynamicMetaEvaluator

    __all__ += ["MetacognitionManager", "DynamicMetaEvaluator"]
except Exception:  # noqa: BLE001
    pass
