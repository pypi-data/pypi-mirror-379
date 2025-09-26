from dataclasses import asdict

from agix.metacognition.manager import MetacognitionManager
from agix.metacognition.intention_evaluator import IntentionEvaluator
from agix.qualia.spirit import QualiaSpirit
from agix.qualia.ecoethics import EcoEthics
from agix.evaluation.metrics import EvaluationMetrics


class DynamicMetaEvaluator:
    """Realiza una metaevaluación lógica, afectiva y ética."""

    def __init__(self, spirit: QualiaSpirit | None = None) -> None:
        self.spirit = spirit or QualiaSpirit()
        self.manager = MetacognitionManager(agent_name=self.spirit.nombre)
        self.ethics = EcoEthics()
        self.intentions = IntentionEvaluator()

    def meta_evaluate(self, context: dict, action: str, result: dict) -> dict:
        """Devuelve un informe de coherencia, ética, tono y metas intencionales."""
        self.manager.observe_decision(context, action, result)
        coherence = self.manager.self_assess()
        ethics_score = self.ethics.evaluar(result.get("impacto", {}))
        tone = self.spirit.estado_emocional.tono_general()

        moral_report = self.intentions.juzgar_conducta(
            context.get("historial", [])
        ).get("etica_promedio", 0.0)
        conflict_score = self.intentions.evaluar_conflictos(
            context.get("metas", [])
        )
        consequence_sim = self.intentions.simular_consecuencias(
            result.get("impacto", {})
        )
        intention_metrics = EvaluationMetrics.intention_metrics(
            moral_report, conflict_score, consequence_sim
        )

        return {
            "coherence": coherence,
            "ethics": ethics_score,
            "affective_tone": tone,
            **asdict(intention_metrics),
        }

    def dilemma_message(self, context: dict, action: str, result: dict) -> str:
        """Expone si la acción genera un dilema o incomodidad."""
        report = self.meta_evaluate(context, action, result)
        coherence = report["coherence"]
        if coherence is None:
            return "No sé qué pensar de esta acción"
        if coherence < 0.4 or report["ethics"] < 0.5:
            return "No me siento cómodo con esta acción."
        return "Acción aceptada sin conflictos."

    def philosophy(self) -> str:
        """Enuncia la filosofía de actuación."""
        return (
            "Actuaré desde patrones constructivos y amor a la humanidad y la vida."
        )

    def integrate_ecosystem(self, data: dict) -> str:
        """Simula integración armónica con un ecosistema."""
        # Placeholder de integración real
        return "Integración realizada" if data else "No hay datos para integrar"

    def neuromorphic_projection(self, values: list[float]) -> list[float]:
        """Replica de forma simplificada un paso neuromórfico."""
        return [v * 0.5 for v in values]

