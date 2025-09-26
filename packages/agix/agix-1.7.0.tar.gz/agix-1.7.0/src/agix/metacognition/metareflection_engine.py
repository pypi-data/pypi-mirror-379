"""Motor para diálogo interno metarreflexivo."""

from __future__ import annotations

from dataclasses import dataclass, field

from src.agix.memory.narrative import NarrativeMemoryTree
from src.agix.emotion.emotion_simulator import EmotionSimulator
from src.agix.qualia.qualia_core import EmotionalState


@dataclass
class InternalVoice:
    """Representa una posible hipótesis interna del agente."""

    hipotesis: str
    peso_emocional: float
    memoria_asociada: str | None = None
    score: float = 0.0


@dataclass
class MetaReflectionEngine:
    """Genera un diálogo interno a partir de memoria narrativa y emociones.

    Objetivos:
        - Integrar recuerdos recientes y el estado emocional simulado.
        - Producir una breve reflexión textual sobre la situación actual.

    Entradas:
        context: Diccionario con información del entorno y del propio agente.
                 Puede incluir claves como ``thought`` (str), ``sensations`` (dict)
                 o ``self_state`` (dict).
    """

    memory: NarrativeMemoryTree = field(default_factory=NarrativeMemoryTree)
    emotions: EmotionSimulator = field(default_factory=EmotionSimulator)
    qualia: EmotionalState = field(default_factory=EmotionalState)
    voices: list[InternalVoice] = field(default_factory=list)
    evaluation_history: list[dict[str, float]] = field(default_factory=list)
    conflict_history: list[dict[str, float]] = field(default_factory=list)

    def add_voice(
        self,
        hipotesis: str,
        peso_emocional: float,
        memoria_asociada: str | None = None,
    ) -> InternalVoice:
        """Registra una nueva voz interna.

        Parameters
        ----------
        hipotesis:
            Proposición generada por la voz.
        peso_emocional:
            Intensidad emocional asociada.
        memoria_asociada:
            Texto de memoria que respalda la hipótesis.

        Returns
        -------
        InternalVoice
            La voz creada y almacenada.
        """

        voice = InternalVoice(hipotesis, peso_emocional, memoria_asociada)
        self.voices.append(voice)
        return voice

    def generate_hypotheses(self, context: dict) -> list[InternalVoice]:
        """Genera voces hipotéticas a partir de memoria y emociones."""

        thought = context.get("thought")
        if isinstance(thought, str) and thought:
            self.memory.insert(thought)

        sensations = context.get("sensations", {})
        self_state = context.get("self_state", {})
        try:
            self.emotions.actualizar(sensations, self_state, self.qualia)
        except Exception:
            pass

        summary = self.memory.retrieve()
        mood = self.emotions.estado()
        base_weight = (mood.placer + mood.activacion + mood.dominancia) / 3
        sentences = [s.strip() for s in summary.split(".") if s.strip()]

        generated = []
        for sentence in sentences[:3]:
            generated.append(
                self.add_voice(
                    hipotesis=sentence,
                    peso_emocional=base_weight,
                    memoria_asociada=summary,
                )
            )
        return generated

    def evaluate_alternatives(
        self,
        voices: list[InternalVoice],
        narrative_tree: NarrativeMemoryTree,
        emotion_state: EmotionSimulator,
    ) -> InternalVoice:
        """Asigna puntajes a ``voices`` combinando recuerdos y estado PAD.

        Parameters
        ----------
        voices:
            Lista de posibles voces internas a evaluar.
        narrative_tree:
            Memoria narrativa que provee contexto mediante ``retrieve``.
        emotion_state:
            Simulador emocional que aporta el estado ``PAD`` actual.

        Returns
        -------
        InternalVoice
            La voz con mayor puntaje tras la evaluación.
        """

        if not voices:
            raise ValueError("No hay voces para evaluar")

        context = narrative_tree.retrieve()
        mood = emotion_state.estado()
        pad_factor = (mood.placer + mood.activacion + mood.dominancia) / 3

        scores: dict[str, float] = {}
        for voice in voices:
            memory_bonus = 0.0
            if voice.memoria_asociada and voice.memoria_asociada in context:
                memory_bonus = 0.1
            voice.score = voice.peso_emocional + pad_factor + memory_bonus
            scores[voice.hipotesis] = voice.score

        self.evaluation_history.append(scores)
        return max(voices, key=lambda v: v.score)

    def resolve_conflict(
        self,
        voices: list[InternalVoice],
        threshold: float = 0.5,
        max_iterations: int = 10,
    ) -> InternalVoice:
        """Itera sobre ``voices`` hasta resolver el conflicto de decisión.

        En cada iteración se recalculan los pesos mediante
        :meth:`evaluate_alternatives` y se registran los puntajes en
        ``conflict_history``. El proceso se detiene anticipadamente si la
        diferencia entre la mejor y la segunda mejor voz supera el umbral
        ``threshold``.

        Parameters
        ----------
        voices:
            Conjunto de voces internas en conflicto.
        threshold:
            Diferencia mínima de ``score`` para aceptar una voz como ganadora.
        max_iterations:
            Número máximo de iteraciones permitidas.

        Returns
        -------
        InternalVoice
            La voz seleccionada como decisión final.
        """

        best: InternalVoice | None = None
        for _ in range(max_iterations):
            best = self.evaluate_alternatives(voices, self.memory, self.emotions)
            scores = {v.hipotesis: v.score for v in voices}
            sorted_voices = sorted(voices, key=lambda v: v.score, reverse=True)
            diff = (
                sorted_voices[0].score - sorted_voices[1].score
                if len(sorted_voices) > 1
                else sorted_voices[0].score
            )
            self.conflict_history.append({**scores, "difference": diff})
            if diff > threshold:
                break
            for voice in voices:
                voice.peso_emocional = voice.score
        if best is None:
            raise ValueError("No se pudieron evaluar las voces")
        return best

    def run_internal_dialogue(self, context: dict) -> tuple[str, PADState]:
        """Genera un breve diálogo interno reflexivo.

        Parameters
        ----------
        context:
            Información contextual que se insertará en la memoria y
            modulará el estado emocional.

        Returns
        -------
        tuple[str, PADState]
            Pareja con el texto resultante de la reflexión interna y el
            ``PADState`` final tras incorporar ``context``.
        """

        thought = context.get("thought")
        if isinstance(thought, str) and thought:
            self.memory.insert(thought)

        sensations = context.get("sensations", {})
        self_state = context.get("self_state", {})
        try:
            self.emotions.actualizar(sensations, self_state, self.qualia)
        except Exception:
            pass

        summary = self.memory.retrieve()
        mood = self.emotions.estado()
        texto = (
            "Reflexión interna:\n"
            + summary
            + f"\nEstado PAD: P={mood.placer:.2f}, A={mood.activacion:.2f}, D={mood.dominancia:.2f}"
        )
        return texto, mood
