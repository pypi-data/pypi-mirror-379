"""Creación heurística de conceptos fusionando embeddings."""

from __future__ import annotations

from typing import List

import numpy as np

from src.agix.reasoning.neuro_symbolic import NeuroSymbolicBridge
from src.agix.memory.symbolic import SymbolicConcept


class HeuristicConceptCreator:
    """Genera nuevos conceptos simbólicos combinando otros existentes."""

    def __init__(self, dim: int = 32) -> None:
        self.bridge = NeuroSymbolicBridge(dim=dim)

    def create(self, base_concepts: List[str]) -> SymbolicConcept:
        """Fusiona los embeddings de ``base_concepts`` y registra un nuevo concepto."""
        if len(base_concepts) < 2:
            raise ValueError("Se requieren al menos dos conceptos para la fusión")

        # Asegurar que todos los conceptos estén registrados
        for name in base_concepts:
            self.bridge.add_concept(SymbolicConcept(name))

        vectors = [self.bridge.symbolic_to_vector(name) for name in base_concepts]
        fusion = np.mean(vectors, axis=0)

        new_name = "fused_" + "_".join(base_concepts)
        nuevo = SymbolicConcept(new_name)
        self.bridge.add_concept(nuevo)
        # Sobrescribir el embedding generado para reflejar la fusión heurística
        self.bridge.latents.embeddings[new_name] = fusion

        # Relacionar conceptualmente
        for name in base_concepts:
            self.bridge.ontology.relate_concepts(new_name, name, "fused_from")
        return nuevo


def generate_new_concept(lista_conceptos: List[str]) -> str:
    """Función de conveniencia que devuelve solo el nombre del concepto generado."""
    creator = HeuristicConceptCreator()
    concepto = creator.create(lista_conceptos)
    return concepto.name
