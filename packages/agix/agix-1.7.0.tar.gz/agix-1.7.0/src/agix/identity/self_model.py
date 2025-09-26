"""Modelo interno simplificado del agente."""


class SelfModel:
    """Representa estado y módulos propios para introspección."""

    def __init__(self, agent_name: str = "AGI-Core", version: str = "1.1.0") -> None:
        self.identity = {
            "name": agent_name,
            "version": version,
        }
        self.state = {}
        self.modules = {}
        self.self_organization_score: float = 0.0
        self.traits: list[str] = []

    def register_module(self, name: str, description: str) -> None:
        """Registra una descripción simbólica de un módulo interno."""
        self.modules[name] = description

    def update_state(self, key: str, value) -> None:
        """Actualiza variables internas del agente (estado reflexivo)."""
        self.state[key] = value

    def update_self_organization(self, score: float) -> None:
        """Actualiza el puntaje de auto-organización del agente."""
        self.self_organization_score = score

    def introspect(self) -> dict:
        """Retorna un resumen reflexivo del estado y estructura interna."""
        return {
            "identity": self.identity,
            "modules": self.modules,
            "state": self.state,
            "traits": self.traits,
            "self_organization_score": self.self_organization_score,
        }

    def add_trait(self, trait: str) -> None:
        """Añade un rasgo identitario derivado de interacciones."""
        if trait not in self.traits:
            self.traits.append(trait)

    def generate_self_query(self) -> str:
        """Devuelve una pregunta típica que el agente se haría a sí mismo."""
        return f"¿Estoy cumpliendo mi propósito como {self.identity['name']}?"

    def is_proto_agent(self, threshold: float) -> bool:
        """Determina si el agente alcanza el umbral para ser considerado proto-agente."""
        return self.self_organization_score >= threshold

    @property
    def proto_agency(self) -> bool:
        """Indica si el agente ha alcanzado el estado de proto-agencia.

        Se utiliza un umbral fijo de ``0.5`` para determinar si el
        ``self_organization_score`` actual es suficiente para considerar al
        agente como proto-agente.
        """
        return self.is_proto_agent(0.5)

