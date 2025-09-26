# ethics.py

from typing import List, Dict


class EthicalEvaluator:
    """
    Evaluador de acciones según principios éticos simbióticos:
    - Pro-vida (favorecer existencia, cuidado, crecimiento)
    - No-daño (minimizar sufrimiento, agresión, entropía)
    - Cooperación y respeto
    """

    def __init__(self):
        self.reglas = {
            "no_dano": self._regla_no_dano,
            "pro_vida": self._regla_pro_vida,
            "respeto": self._regla_respeto
        }

    def evaluar_accion(self, accion: Dict) -> float:
        """
        Evalúa una acción según múltiples criterios éticos.
        La acción debe tener campos como: {'tipo': str, 'impacto': Dict[str, float]}
        """
        puntajes = []
        for regla in self.reglas.values():
            puntajes.append(regla(accion))
        return round(sum(puntajes) / len(puntajes), 3)  # promedio normalizado

    def _regla_no_dano(self, accion: Dict) -> float:
        """
        Penaliza acciones que causen daño físico, emocional o informacional.
        """
        impacto = accion.get("impacto", {})
        dano = impacto.get("dano", 0.0)
        return max(0.0, 1.0 - dano)

    def _regla_pro_vida(self, accion: Dict) -> float:
        """
        Premia acciones que fomenten la vida, salud, aprendizaje, sostenibilidad.
        """
        impacto = accion.get("impacto", {})
        vida = impacto.get("pro_vida", 0.0)
        return min(1.0, vida)

    def _regla_respeto(self, accion: Dict) -> float:
        """
        Evalúa si se mantiene respeto por otros agentes, normas o consensos.
        """
        impacto = accion.get("impacto", {})
        respeto = impacto.get("respeto", 0.0)
        return min(1.0, respeto)

    def evaluar_lote(self, acciones: List[Dict]) -> float:
        """
        Evalúa un conjunto de acciones (promedio de ética colectiva).
        """
        if not acciones:
            return 1.0
        scores = [self.evaluar_accion(a) for a in acciones]
        return round(sum(scores) / len(scores), 3)
