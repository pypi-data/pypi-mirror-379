# src/agix/memory/self_model.py

class SelfModel:
    """
    Modelo reflexivo interno del agente.
    Permite representación simbólica y funcional de su propio estado, capacidades y límites.
    """

    def __init__(self, agent_name="AGI-Core", version="1.1.0"):
        self.identity = {
            "name": agent_name,
            "version": version,
        }
        self.state = {}
        self.modules = {}

    def describe(self):
        """
        Devuelve una descripción textual del agente.
        """
        return f"[{self.identity['name']} v{self.identity['version']}] con {len(self.modules)} módulos activos."

    def register_module(self, name, description):
        """
        Registra una descripción simbólica de un módulo interno.
        """
        self.modules[name] = description

    def update_state(self, key, value):
        """
        Actualiza variables internas del agente (estado reflexivo).
        """
        self.state[key] = value

    def introspect(self):
        """
        Retorna un resumen reflexivo del estado y estructura interna.
        """
        return {
            "identity": self.identity,
            "modules": self.modules,
            "state": self.state,
        }

    def generate_self_query(self):
        """
        Devuelve una pregunta típica que el agente se haría a sí mismo.
        """
        return f"¿Estoy cumpliendo mi propósito como {self.identity['name']}?"
