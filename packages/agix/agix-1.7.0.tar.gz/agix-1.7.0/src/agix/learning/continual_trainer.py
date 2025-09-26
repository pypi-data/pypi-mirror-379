"""Entrenador heurístico continuo."""

from __future__ import annotations

from src.agix.learning.heuristic_evolution import HeuristicEvolution
from src.agix.memory.experiential import GestorDeMemoria


class ContinuousHeuristicTrainer:
    """Actualiza cromosomas tras cada episodio usando la memoria acumulada."""

    def __init__(self, memory: GestorDeMemoria, param_len: int):
        self.memory = memory
        self.evolver = HeuristicEvolution(param_len)

    def add_experience(self, entrada: str, decision: str, resultado: str, exito: bool):
        """Registra una experiencia en la memoria."""
        self.memory.registrar(entrada, decision, resultado, exito)

    def end_episode(self, agent: "HeuristicGeneticAgent") -> None:
        """Recalibra el cromosoma del agente usando la memoria."""
        agent.chromosome = self.evolver.generar_parametros(self.memory)
