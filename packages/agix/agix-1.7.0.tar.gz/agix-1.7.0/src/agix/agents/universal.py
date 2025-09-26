# src/agix/agents/universal.py

from agix.metacognition.manager import MetacognitionManager


class UniversalAgent:
    """
    Agente cognitivo universal capaz de modificar su arquitectura interna
    en tiempo de ejecución mediante autoevaluación o condiciones ambientales.
    """

    def __init__(self, modules=None):
        """
        modules: diccionario de componentes funcionales {nombre: módulo}
        """
        self.modules = modules or {}
        self.metacognition = MetacognitionManager()

    def add_module(self, name, module):
        """
        Agrega un nuevo módulo funcional al agente en tiempo de ejecución.
        """
        self.modules[name] = module

    def remove_module(self, name):
        """
        Elimina un módulo funcional del agente.
        """
        if name in self.modules:
            del self.modules[name]

    def reconfigure(self, new_configuration):
        """
        Redefine completamente los módulos del agente.
        new_configuration: diccionario con la nueva arquitectura
        """
        self.modules = new_configuration

    def evaluate_self(self):
        """
        Evalúa la coherencia de sus acciones y ajusta módulos si es necesario.
        """
        coherence = self.metacognition.self_assess()
        if coherence < 0.5 and "policy" in self.modules:
            del self.modules["policy"]
        return coherence

    def act(self, observation):
        """
        Ejecuta una acción en base a los módulos disponibles.
        """
        if "policy" in self.modules:
            return self.modules["policy"].decide(observation)
        return None
