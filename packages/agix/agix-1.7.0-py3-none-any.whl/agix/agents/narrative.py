# agix/agents/narrative.py

from __future__ import annotations

from typing import List, Optional
import numpy as np


from src.agix.agents.base import AGIAgent
from src.agix.qualia.spirit import QualiaSpirit
from src.agix.evaluation import NarrativeCompressionEvaluator
from src.agix.memory.narrative import MemoryNode
from src.agix.memory.episodic import EpisodicMemory
from src.agix.memory.symbolic import SymbolicConcept
from src.agix.reasoning.neuro_symbolic import NeuroSymbolicBridge


class NarrativeAgent(AGIAgent):
    """Agente especializado en procesar y recordar narrativas."""

    def __init__(
        self,
        k: int = 2,
        depth: int = 3,
        dim: int = 16,
        qualia: Optional[QualiaSpirit] = None,
    ):
        super().__init__(name="NarrativeAgent", qualia=qualia)
        self.memory = EpisodicMemory(k=k, depth=depth)
        self.bridge = NeuroSymbolicBridge(dim=dim)
        self.evaluator = NarrativeCompressionEvaluator
        self._last_story: str = ""

    # ------------------------------------------------------------------
    # Interfaces del AGIAgent
    # ------------------------------------------------------------------
    def perceive(self, observation):
        """Procesa una observación recibida por el agente."""
        if isinstance(observation, str):
            self.perceive_story(observation)
        super().perceive(observation)

    def decide(self, pad: 'PADState | None' = None):
        """Devuelve el fragmento más relevante almacenado."""
        pad = super().decide(pad)
        return self.recall_decision()

    def learn(self, reward, done=False):
        """El agente narrativo no implementa aprendizaje por refuerzo."""
        pass

    # ------------------------------------------------------------------
    # Funcionalidad narrativa
    # ------------------------------------------------------------------
    def perceive_story(self, text: str) -> None:
        """Fragmenta el texto e inserta cada parte en la memoria."""
        segments = [s.strip() for s in text.split('.') if s.strip()]
        for seg in segments:
            self.memory.insert(seg)
            self.bridge.add_concept(SymbolicConcept(seg))
        self._last_story = text

    def summarize(self) -> str:
        summary = self.memory.retrieve()
        if self._last_story:
            metrics = self.evaluator.evaluate(self.memory, self._last_story)
            summary += f"\n[alpha={metrics['alpha']:.2f}, precision={metrics['precision']:.2f}]"
        return summary

    def _all_nodes(self) -> List[MemoryNode]:
        """Devuelve todos los nodos de la memoria en recorrido DFS."""
        nodes: List[MemoryNode] = []
        stack = [self.memory.root]
        while stack:
            node = stack.pop()
            if node is not self.memory.root:
                nodes.append(node)
            stack.extend(node.children)
        return nodes

    def recall_decision(self) -> str:
        """Devuelve el fragmento más similar al concepto 'importante'."""
        target = self.bridge.symbolic_to_vector("importante")
        best_node = None
        best_score = -float("inf")
        for node in self._all_nodes():
            vec = node.to_embedding(self.bridge)
            score = float(np.dot(vec, target) / (np.linalg.norm(vec) * np.linalg.norm(target)))
            if score > best_score:
                best_score = score
                best_node = node
        return best_node.content if best_node else ""
