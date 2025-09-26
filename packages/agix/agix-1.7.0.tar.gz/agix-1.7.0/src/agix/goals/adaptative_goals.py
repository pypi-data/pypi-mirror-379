# adaptive_goals.py


from typing import Callable, Any, Dict, List

from src.agix.goals.goal_engine import Goal, GoalEngine


class AdaptiveGoalStrategy:
    """
    Estrategia para adaptar metas en tiempo real según factores internos o externos.
    """

    def __init__(self, nombre: str, condicion: Callable[[Goal], bool], modificador: Callable[[Goal], None]):
        """
        - nombre: nombre simbólico de la estrategia (ej. 'repriorizar según ansiedad')
        - condicion: función que decide si se aplica esta estrategia a una meta
        - modificador: función que modifica la meta si se cumple la condición
        """
        self.nombre = nombre
        self.condicion = condicion
        self.modificador = modificador

    def aplicar(self, goal: Goal) -> bool:
        if self.condicion(goal):
            self.modificador(goal)
            return True
        return False


class AdaptiveGoalEngine(GoalEngine):
    """
    Motor de metas extendido con estrategias adaptativas.
    """

    def __init__(self):
        super().__init__()
        self.estrategias: List[AdaptiveGoalStrategy] = []

    def registrar_estrategia(self, estrategia: AdaptiveGoalStrategy):
        self.estrategias.append(estrategia)

    def adaptar_metas(self):
        for meta in self.metas_activas():
            for estrategia in self.estrategias:
                estrategia.aplicar(meta)

    def diagnostico_adaptativo(self) -> str:
        resumen = [f"{m.descripcion}: prioridad {m.prioridad}" for m in self.metas_activas()]
        return "Estado adaptativo actual:\n" + "\n".join(resumen)
