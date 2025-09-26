"""Estructuras para memoria narrativa jerárquica.

Basado en un árbol K-ario comprimido donde cada nodo almacena
un fragmento de narrativa. Permite insertar experiencias y
recuperar un resumen sintético.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

import numpy as np

from src.agix.memory.symbolic import SymbolicConcept
from src.agix.reasoning.neuro_symbolic import NeuroSymbolicBridge


@dataclass
class MemoryNode:
    """Nodo de memoria narrativa."""

    content: str
    level: int = 0
    children: List["MemoryNode"] = field(default_factory=list)

    def to_concept(self, bridge: NeuroSymbolicBridge) -> SymbolicConcept:
        """Convierte el contenido del nodo en un concepto simbólico."""
        return bridge.ontology.conceptualize(self.content)

    def to_embedding(self, bridge: NeuroSymbolicBridge) -> np.ndarray:
        """Obtiene el embedding asociado al contenido del nodo."""
        concept = self.to_concept(bridge)
        return bridge.latents.encode(concept.name)


class NarrativeMemoryTree:
    """Memoria narrativa en forma de árbol jerárquico."""

    def __init__(self, k: int = 2, depth: int = 3):
        self.K = k
        self.D = depth
        self.root = MemoryNode("ROOT", level=0)

    def insert(self, content: str) -> None:
        """Inserta un fragmento en el árbol."""

        self._insert_recursive(self.root, content)

    def _insert_recursive(self, node: MemoryNode, content: str) -> None:
        if node.level + 1 >= self.D:
            if len(node.children) >= self.K:
                node.children.pop(0)
            node.children.append(MemoryNode(content, level=node.level + 1))
            return

        if len(node.children) < self.K:
            node.children.append(MemoryNode(content, level=node.level + 1))
        else:
            self._insert_recursive(node.children[-1], content)

    def retrieve(self) -> str:
        """Devuelve un resumen jerárquico de los contenidos."""

        lines: List[str] = []

        def traverse(n: MemoryNode) -> None:
            if n is not self.root:
                lines.append("  " * n.level + f"- {n.content}")
            for child in n.children:
                traverse(child)

        traverse(self.root)
        return "\n".join(lines)

    # --- nuevas utilidades ---
    def node_count(self) -> int:
        """Cuenta todos los nodos del árbol."""
        count = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            count += 1
            stack.extend(node.children)
        return count

    def capacity(self) -> int:
        """Número máximo de recuerdos que puede almacenar."""
        return self.K ** self.D

    def load_factor(self) -> float:
        """Fracción de ocupación respecto a la capacidad."""
        leaves = max(self.node_count() - 1, 0)
        return leaves / max(self.capacity(), 1)

    def expand(self, depth_increment: int = 1, k_increment: int = 0) -> None:
        """Aumenta la profundidad o el ancho del árbol.

        Permite que la memoria narrativa crezca de forma gradual. ``depth_increment``
        añade nuevos niveles al árbol, mientras que ``k_increment`` incrementa el
        número máximo de hijos por nodo.
        """

        if depth_increment < 0 or k_increment < 0:
            raise ValueError("Los incrementos deben ser no negativos")

        self.D += depth_increment
        self.K += k_increment
