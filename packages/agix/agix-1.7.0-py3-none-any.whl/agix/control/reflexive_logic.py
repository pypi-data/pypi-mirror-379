# reflexive_logic.py

from typing import List, Dict, Any


class ReflexiveLogic:
    """
    Módulo de lógica introspectiva.
    Analiza decisiones pasadas, patrones de acción y evalúa la coherencia entre metas, acciones y estados.
    """

    def __init__(self):
        self.registro_reflexivo: List[Dict[str, Any]] = []

    def registrar_evento(self, contexto: Dict[str, Any], accion: str, resultado: Any):
        """
        Guarda un evento significativo para análisis posterior.
        """
        self.registro_reflexivo.append({
            "contexto": contexto,
            "accion": accion,
            "resultado": resultado
        })

    def evaluar_coherencia(self) -> float | None:
        """
        Evalúa qué tan coherente ha sido el comportamiento del agente.
        Retorna un valor entre 0.0 y 1.0 o ``None`` si no hay registros.
        """
        if not self.registro_reflexivo:
            return None

        decisiones_correctas = sum(1 for evento in self.registro_reflexivo if self._es_coherente(evento))
        return decisiones_correctas / len(self.registro_reflexivo)

    def _es_coherente(self, evento: Dict[str, Any]) -> bool:
        """
        Criterio provisional de coherencia.
        Aquí puedes introducir inferencia simbólica más compleja en el futuro.
        """
        resultado = evento.get("resultado", {})
        return resultado.get("exito", False)

    def resumen_reflexivo(self) -> str:
        """
        Genera un resumen textual del análisis introspectivo.
        """
        total = len(self.registro_reflexivo)
        coh = self.evaluar_coherencia()
        return f"Eventos analizados: {total} | Coherencia global: {coh:.2f}"
