"""Colección de agentes disponibles en AGIX."""

from .genetic import GeneticAgent
from .neuromorphic import NeuromorphicAgent
from .universal import UniversalAgent
from .narrative import NarrativeAgent
from .heuristic_genetic import HeuristicGeneticAgent
from .affective_npc import AffectiveNPC

__all__ = [
    "GeneticAgent",
    "NeuromorphicAgent",
    "UniversalAgent",
    "NarrativeAgent",
    "HeuristicGeneticAgent",
    "AffectiveNPC",
]
