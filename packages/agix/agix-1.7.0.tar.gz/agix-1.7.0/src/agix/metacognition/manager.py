from src.agix.identity.self_model import SelfModel
from src.agix.control.reflexive_logic import ReflexiveLogic
from src.agix.metacognition.self_organization import SelfOrganizationMonitor
from src.agix.metacognition.metareflection_engine import MetaReflectionEngine
from src.agix.emotion import PADState
from src.agix.autonarrative.autonarrative_core import AutonarrativeCore
from src.agix.identity.user_interaction import UserInteractionSession
from src.agix.metacognition.decision_reviewer import DecisionReviewer
import time


class MetacognitionManager:
    """Coordina el modelo reflexivo y la evaluación de decisiones."""

    def __init__(self, agent_name: str = "AGI-Core", version: str = "1.1.0") -> None:
        self.self_model = SelfModel(agent_name=agent_name, version=version)
        self.logic = ReflexiveLogic()
        self.self_organization = SelfOrganizationMonitor()
        self.meta_reflection_engine = MetaReflectionEngine()
        self.autonarrative = AutonarrativeCore()
        self.interaction_session = UserInteractionSession(self.self_model, self.autonarrative)

    def observe_decision(self, context: dict, action: str, result: dict) -> None:
        """Registra una acción y su resultado para análisis posterior."""
        self.logic.registrar_evento(context, action, result)
        # Actualiza información de auto-organización
        modules = context.get("active_modules")
        if modules:
            self.self_organization.active_modules.extend(modules)
        dependencies = context.get("dependencies")
        if dependencies:
            for mod, deps in dependencies.items():
                self.self_organization.dependencies.setdefault(mod, [])
                self.self_organization.dependencies[mod].extend(deps)
        self.self_organization.activation_times.append(time.time())

        score = self.self_organization.compute_score()
        self.self_model.update_self_organization(score)

    def self_assess(self) -> float | None:
        """Evalúa la coherencia de las decisiones observadas."""
        coherence = self.logic.evaluar_coherencia()
        self.self_model.update_state("coherence", coherence)
        return coherence

    def inner_dialogue(self, context: dict) -> tuple[str, PADState]:
        """Genera un diálogo interno metarreflexivo.

        Parameters
        ----------
        context:
            Información contextual a procesar por el motor.

        Returns
        -------
        tuple[str, PADState]
            Reflexión textual y estado emocional ``PAD`` tras el diálogo.
        """

        return self.meta_reflection_engine.run_internal_dialogue(context)

    def process_user_input(self, message: str) -> str:
        """Procesa entrada de usuario, actualizando estado y narrativa."""
        response = self.interaction_session.receive_message(message)
        self.self_model.update_state(
            "last_interaction", {"user": message, "agent": response}
        )
        return response

    @property
    def proto_agency(self) -> bool:
        """Indica si el agente ha alcanzado el estado de proto-agencia."""
        return self.self_model.proto_agency

    # ------------------------------------------------------------------
    def review_decisions(self, max_items: int) -> dict:
        """Revisa decisiones previas y actualiza el ``SelfModel``.

        Parameters
        ----------
        max_items:
            Número máximo de decisiones recientes a reevaluar.

        Returns
        -------
        dict
            Análisis de aciertos, errores y tono emocional tras la revisión.
        """

        reviewer = DecisionReviewer(self.logic, self.autonarrative)
        analysis = reviewer.review(max_items)
        self.self_model.update_state("decision_review", analysis)
        return analysis
