"""Módulos de orquestación y coordinación."""

from .hub import QualiaHub
from .virtual import VirtualQualia
from .emotion_hub import EmotionHub, EMOTIONAL_STATE
from .synthetic_loop import SyntheticLoop, run_cycle

__all__ = [
    "QualiaHub",
    "VirtualQualia",
    "EmotionHub",
    "EMOTIONAL_STATE",
    "SyntheticLoop",
    "run_cycle",
]
