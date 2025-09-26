# src/agix/architecture/ameta.py

class AGIModule:
    """Clase base para módulos funcionales dentro de la arquitectura AGI."""
    def process(self, input_data):
        raise NotImplementedError("Cada módulo debe implementar su método 'process'.")


class AMetaArchitecture:
    """
    Arquitectura modular AGI basada en cinco bloques:
    P: Percepción, I: Inferencia, D: Decisión, E: Ejecución, M: Memoria
    """

    def __init__(self, P=None, I=None, D=None, E=None, M=None):
        self.modules = {
            "P": P,
            "I": I,
            "D": D,
            "E": E,
            "M": M
        }

    def perceive(self, observation):
        return self.modules["P"].process(observation) if self.modules["P"] else observation

    def infer(self, data):
        return self.modules["I"].process(data) if self.modules["I"] else data

    def decide(self, inferred_state):
        return self.modules["D"].process(inferred_state) if self.modules["D"] else None

    def execute(self, action):
        return self.modules["E"].process(action) if self.modules["E"] else None

    def memorize(self, experience):
        return self.modules["M"].process(experience) if self.modules["M"] else None

    def cycle(self, observation):
        """
        Ejecuta un ciclo completo: P → I → D → E + M
        """
        percept = self.perceive(observation)
        inferred = self.infer(percept)
        action = self.decide(inferred)
        self.execute(action)
        self.memorize((observation, action))
        return action
