import numpy as np


from typing import Dict, List

from src.agix.memory.sub_symbolic import LatentRepresentation
from src.agix.memory.symbolic import Ontology, SymbolicConcept


class NeuroSymbolicBridge:
    """
    Puente bidireccional entre conceptos simbólicos y vectores subsimbólicos.
    Permite razonamiento y aprendizaje híbrido en un espacio coherente.
    """

    def __init__(self, dim: int = 32):
        self.ontology = Ontology()
        self.latents = LatentRepresentation(dim)
        self.concept_map: Dict[str, str] = {}  # nombre simbólico -> clave de embedding

    def add_concept(self, concept: SymbolicConcept):
        # Utiliza la ontología para registrar el concepto (o recuperarlo si ya existe)
        concept_obj = self.ontology.conceptualize(concept.name)
        # Conservar posibles atributos o relaciones ya especificados
        concept_obj.attributes.update(concept.attributes)
        concept_obj.relations.update(concept.relations)

        self.concept_map[concept_obj.name] = concept_obj.name
        self.latents.encode(concept_obj.name)

    def relate_concepts_semantically(self, threshold: float = 0.7):
        """
        Relaciona simbólicamente conceptos cuya representación latente es similar.
        """
        names = list(self.concept_map.keys())
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                sim = self.latents.similarity(names[i], names[j])
                if sim >= threshold:
                    self.ontology.relate_concepts(names[i], names[j], "similar")

    def explain_vector(self, vec: np.ndarray) -> str:
        """
        Devuelve el concepto más cercano a un vector dado (decodificación semántica).
        """
        best_name = None
        best_score = -float("inf")
        for name in self.concept_map:
            key_vec = self.latents.encode(name)
            score = np.dot(vec, key_vec) / (np.linalg.norm(vec) * np.linalg.norm(key_vec))
            if score > best_score:
                best_score = score
                best_name = name
        return best_name

    def symbolic_to_vector(self, name: str) -> np.ndarray:
        return self.latents.encode(name)

    def vector_to_symbolic(self, vec: np.ndarray) -> str:
        return self.explain_vector(vec)

    def get_ontology(self) -> Ontology:
        return self.ontology
