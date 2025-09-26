from typing import Dict, List


class SymbolicConcept:
    """
    Representación simbólica de un concepto con atributos semánticos y relaciones.
    """
    def __init__(self, name: str):
        self.name: str = name
        self.attributes: Dict[str, str] = {}
        self.relations: Dict[str, List[str]] = {}

    def add_attribute(self, key: str, value: str):
        self.attributes[key] = value

    def relate(self, other_concept: 'SymbolicConcept', relation_type: str):
        if relation_type not in self.relations:
            self.relations[relation_type] = []
        self.relations[relation_type].append(other_concept.name)

    def describe(self) -> str:
        return f"{self.name} ({', '.join(f'{k}:{v}' for k,v in self.attributes.items())})"


class Ontology:
    """
    Ontología simbólica jerárquica basada en conceptos relacionados.
    """
    def __init__(self):
        self.concepts: Dict[str, SymbolicConcept] = {}

    def add_concept(self, concept: SymbolicConcept):
        self.concepts[concept.name] = concept

    def conceptualize(self, name: str) -> SymbolicConcept:
        """Devuelve un concepto existente o lo crea si no está registrado."""
        if name not in self.concepts:
            self.concepts[name] = SymbolicConcept(name)
        return self.concepts[name]

    def find_by_attribute(self, key: str, value: str) -> list:
        return [c for c in self.concepts.values() if c.attributes.get(key) == value]

    def get_concept(self, name: str) -> SymbolicConcept:
        return self.concepts.get(name)

    def relate_concepts(self, name1: str, name2: str, relation: str):
        if name1 in self.concepts and name2 in self.concepts:
            self.concepts[name1].relate(self.concepts[name2], relation)

    def __str__(self):
        return "\n".join(f"{c.name}: {c.relations}" for c in self.concepts.values())

