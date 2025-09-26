from __future__ import annotations

from typing import Dict, List


class IntentionEvaluator:
    """Evalúa intenciones, metas y conductas de un agente."""

    def simular_consecuencias(self, accion: Dict) -> Dict:
        """
        Predice resultados futuros de una acción utilizando una heurística 
        inspirada en lógica difusa y teoría de juegos.

        La acción puede contener campos como::
            {
                'beneficio': float [0,1],
                'riesgo': float [0,1],
                'cooperacion': float [0,1]
            }
        Devuelve un resumen con ganancia esperada y nivel de riesgo percibido.
        """
        beneficio = float(accion.get('beneficio', 0.0))
        riesgo = float(accion.get('riesgo', 0.0))
        cooperacion = float(accion.get('cooperacion', 0.5))

        # Lógica difusa: membership simple para éxito y fracaso
        prob_exito = max(0.0, min(1.0, beneficio * (1 - riesgo)))
        prob_fracaso = 1 - prob_exito

        # Teoría de juegos simplificada: incentivo a cooperar o competir
        payoff_cooperar = beneficio * cooperacion
        payoff_competir = beneficio * (1 - cooperacion) - riesgo
        decision = 'cooperar' if payoff_cooperar >= payoff_competir else 'competir'

        return {
            'prob_exito': round(prob_exito, 3),
            'prob_fracaso': round(prob_fracaso, 3),
            'decision_recomendada': decision,
        }

    def evaluar_conflictos(self, metas: List[Dict]) -> float:
        """
        Puntúa la coherencia y los posibles conflictos entre metas internas.

        Cada meta puede definirse como::
            {
                'nombre': str,
                'prioridad': float [0,10],
                'incompatibles': List[str]
            }
        Retorna un índice normalizado entre 0 y 1 donde 1 indica alto conflicto.
        """
        if len(metas) < 2:
            return 0.0

        conflicto_total = 0.0
        comparaciones = 0
        for i in range(len(metas)):
            for j in range(i + 1, len(metas)):
                m1, m2 = metas[i], metas[j]
                diff_prioridad = abs(m1.get('prioridad', 0) - m2.get('prioridad', 0)) / 10
                inc1 = 1.0 if m2.get('nombre') in m1.get('incompatibles', []) else 0.0
                inc2 = 1.0 if m1.get('nombre') in m2.get('incompatibles', []) else 0.0
                conflicto = min(1.0, diff_prioridad + max(inc1, inc2))
                conflicto_total += conflicto
                comparaciones += 1
        return round(conflicto_total / comparaciones, 3)

    def juzgar_conducta(self, historial: List[Dict]) -> Dict:
        """
        Genera un informe moral y motivacional a partir de un historial de
        acciones recientes del agente.

        Cada elemento del historial puede tener::
            {
                'etica': float [0,1],
                'motivacion': float [0,1]
            }
        El informe final contiene promedios y un veredicto simbólico.
        """
        if not historial:
            return {'etica_promedio': 1.0, 'motivacion_promedio': 0.0, 'veredicto': 'sin datos'}

        etica_media = sum(h.get('etica', 0.0) for h in historial) / len(historial)
        motiv_media = sum(h.get('motivacion', 0.0) for h in historial) / len(historial)

        if etica_media >= 0.6 and motiv_media >= 0.5:
            veredicto = 'conducta positiva'
        elif etica_media < 0.4:
            veredicto = 'conducta cuestionable'
        else:
            veredicto = 'conducta neutral'

        return {
            'etica_promedio': round(etica_media, 3),
            'motivacion_promedio': round(motiv_media, 3),
            'veredicto': veredicto,
        }
