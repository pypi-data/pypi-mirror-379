"""Subpaquete de procesos cualitativos y estado emocional."""



from .qualia_engine import QualiaEngine

__all__ = [
    "ConceptClassifier",
    "HeuristicQualiaSpirit",
    "EmotionalRNN",
    "AffectiveVector",
    "QualiaMiddleware",
    "QualiaEngine",
    "QualiaSpiritCore",
]


def __getattr__(name):
    if name == "ConceptClassifier":
        from .concept_classifier import ConceptClassifier

        return ConceptClassifier
    if name == "HeuristicQualiaSpirit":
        from .heuristic_spirit import HeuristicQualiaSpirit

        return HeuristicQualiaSpirit
    if name == "EmotionalRNN":
        from .emotional_rnn import EmotionalRNN

        return EmotionalRNN

    if name == "AffectiveVector":
        from .afe_vec import AffectiveVector

        return AffectiveVector

    if name == "QualiaMiddleware":
        from .middleware import QualiaMiddleware
        return QualiaMiddleware
    if name == "QualiaSpiritCore":
        from .qualia_spirit_core import QualiaSpiritCore
        return QualiaSpiritCore

    raise AttributeError(name)
