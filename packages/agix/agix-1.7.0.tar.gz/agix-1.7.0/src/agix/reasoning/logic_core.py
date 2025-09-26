# logic_core.py

from typing import List, Dict, Callable


class Fact:
    """
    Representa un hecho lógico atómico: predicado con argumentos.
    Ejemplo: amigo("ana", "juan")
    """
    def __init__(self, predicate: str, args: List[str]):
        self.predicate = predicate
        self.args = args

    def __str__(self):
        return f"{self.predicate}({', '.join(self.args)})"


class Rule:
    """
    Regla lógica tipo: si condición(es), entonces hecho.
    Ejemplo: si amigo(X, Y) y amigo(Y, Z) → amigo(X, Z)
    """
    def __init__(self, condition: Callable[[List[Fact]], bool], consequence: Fact, description: str = "", priority: float = 1.0, enabled: bool = True):
        self.condition = condition
        self.consequence = consequence
        self.description = description or str(consequence)
        self.priority = priority
        self.enabled = enabled


class LogicCore:
    """
    Núcleo de razonamiento lógico simbólico. Permite agregar hechos, reglas e inferir consecuencias.
    """

    def __init__(self):
        self.facts: List[Fact] = []
        self.rules: List[Rule] = []

    def add_fact(self, fact: Fact):
        self.facts.append(fact)

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def infer(self):
        """
        Aplica reglas sobre los hechos actuales y añade nuevas inferencias.
        """
        new_facts = []
        # Ordenamos las reglas por prioridad y omitimos las deshabilitadas
        ordered_rules = sorted(
            [r for r in self.rules if r.enabled], key=lambda r: r.priority, reverse=True
        )
        for rule in ordered_rules:
            if rule.condition(self.facts):
                if not any(f.__str__() == str(rule.consequence) for f in self.facts):
                    self.facts.append(rule.consequence)
                    new_facts.append(rule.consequence)
        return new_facts

    def mutate_rule_priority(self, rule: Rule, delta: float):
        """Ajusta la prioridad de una regla en `delta`."""
        if rule in self.rules:
            rule.priority += delta

    def toggle_rule(self, rule: Rule, active: bool):
        """Activa o desactiva una regla."""
        if rule in self.rules:
            rule.enabled = active

    def list_facts(self):
        return [str(f) for f in self.facts]

    def list_rules(self):
        return [r.description for r in self.rules]
