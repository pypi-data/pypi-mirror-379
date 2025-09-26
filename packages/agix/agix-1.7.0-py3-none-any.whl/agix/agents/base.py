# agi_lab/agents/base.py

from abc import ABC, abstractmethod
from typing import Any, Optional, TYPE_CHECKING

from src.agix.memory.experiential import GestorDeMemoria
from src.agix.evaluation import evaluar
from src.agix.qualia.spirit import QualiaSpirit
from src.agix.ethics import AlignmentInterface

if TYPE_CHECKING:  # pragma: no cover
    from src.agix.emotion import EmotionSimulator, PADState

class AGIAgent(ABC):
    """
    Clase base abstracta para agentes de AGI.
    Todos los agentes deben implementar los siguientes métodos clave:
    - percebir: procesar observaciones del entorno
    - decidir: tomar acciones
    - aprender: actualizar internamente según experiencia
    """

    def __init__(
        self,
        name: str = "AGIAgent",
        qualia: Optional[QualiaSpirit] = None,
        collective_client: Optional[Any] = None,
        emotion_simulator: Optional['EmotionSimulator'] = None,
    ):
        """Inicializa un agente de AGI.

        Parameters
        ----------
        name:
            Nombre del agente.
        qualia:
            Instancia ``QualiaSpirit`` para gestionar el estado emocional.
        collective_client:
            Cliente opcional para sincronizar emociones con una red colectiva.
        """
        self.name = name
        self.memory = GestorDeMemoria()
        self.internal_state = {}
        self.qualia = qualia
        self.collective_client = collective_client
        self.alignment = AlignmentInterface()
        if emotion_simulator is None:
            try:
                from src.agix.emotion.emotion_simulator import EmotionSimulator as _EmotionSimulator

                self.emotion_simulator = _EmotionSimulator()
            except Exception:  # pragma: no cover
                self.emotion_simulator = None
        else:
            self.emotion_simulator = emotion_simulator
        self._pad_estado: 'PADState | None' = None
        if self.qualia and self.emotion_simulator:
            self.qualia.emotion_simulator = self.emotion_simulator

    @abstractmethod
    def perceive(self, observation):
        """Procesa una observación del entorno y actualiza el simulador emocional."""
        if self.emotion_simulator and self.qualia:
            entradas = observation if isinstance(observation, dict) else {"observacion": observation}
            self_state = (
                self.qualia.self_model.introspect()
                if hasattr(self.qualia, "self_model")
                else self.internal_state
            )
            self.emotion_simulator.actualizar(
                entradas,
                self_state,
                self.qualia.estado_emocional,
            )

    @abstractmethod
    def decide(self, pad: 'PADState | None' = None):
        """Obtiene el estado PAD antes de decidir y lo pone a disposición del agente."""
        if pad is None and self.emotion_simulator:
            pad = self.emotion_simulator.estado()
        self._pad_estado = pad
        return pad

    @abstractmethod
    def learn(self, reward, done=False):
        """Actualiza el agente tras recibir recompensa."""
        pass

    def reset(self):
        """Reinicia el estado interno del agente."""
        self.internal_state.clear()

    # --------------------------------------------------------------
    def feel(self, evento: str, carga: float, tipo: str = "sorpresa") -> None:
        """Registra una experiencia emocional en ``QualiaSpirit`` si existe."""
        if self.qualia:
            self.qualia.experimentar(evento, carga, tipo)

    # --------------------------------------------------------------
    def sync_collective_emotions(self) -> None:
        """Sincroniza el estado emocional con la red colectiva."""
        if self.collective_client and self.qualia:
            self.collective_client.push_state(self.qualia.estado_emocional.emociones)

    def share_emotion(self, evento: str, carga: float) -> None:
        """Comparte una emoción puntual a través del cliente colectivo."""
        if self.collective_client:
            self.collective_client.share_emotion(evento, carga)

    # --------------------------------------------------------------
    def record_experience(
        self,
        entrada: str,
        decision: str,
        resultado: str,
        exito: bool | None = None,
        timestamp: str | None = None,
    ):
        """Almacena una experiencia completa en la memoria del agente."""
        if exito is None:
            evaluacion = evaluar(entrada, decision, resultado)
            exito = bool(evaluacion.get("exito"))
        juicio = None
        if isinstance(decision, dict):
            score, label = self.alignment.judge(decision)
            juicio = f"{label}:{score:.3f}"
        pad = self._pad_estado
        if pad is None and self.emotion_simulator:
            pad = self.emotion_simulator.estado()
        if self.memory:
            self.memory.registrar(
                entrada,
                decision,
                resultado,
                exito,
                juicio,
                timestamp,
                emocion=pad,
            )
        if self.qualia:
            emocion = "alegría" if exito else "tristeza"
            intensidad = 1.0 if exito else 0.3
            self.feel(resultado, intensidad, emocion)

    def __str__(self):
        return f"<AGIAgent: {self.name}>"
