from typing import List, Optional, Dict

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.agix.evaluation.metrics import EvaluationMetrics
from src.agix.qualia.qualia_core import EmotionalState

app = FastAPI(title="AGIX Dashboard")

# Estado emocional global y registros de recompensa
emotional_state = EmotionalState()
reward_history: List[float] = []
pad_state: Dict[str, float] = {
    "pleasure": 0.0,
    "arousal": 0.0,
    "dominance": 0.0,
}


class SyncPayload(BaseModel):
    emociones: dict
    pad: Optional[Dict[str, float]] = None


def register_reward(reward: float) -> None:
    """Añade una recompensa al historial."""
    reward_history.append(float(reward))


def register_emotion(tipo: str, intensidad: float) -> None:
    """Registra una emoción en el estado global."""
    emotional_state.sentir(tipo, intensidad)


@app.get("/qualia")
def get_qualia():
    """Devuelve el estado emocional actual."""
    return JSONResponse(
        {
            "emociones": emotional_state.emociones,
            "tono": emotional_state.tono_general(),
            "pad": pad_state,
        }
    )


@app.get("/metrics")
def get_metrics():
    """Calcula métricas básicas de aprendizaje."""
    return JSONResponse(
        {
            "average_reward": EvaluationMetrics.average_reward(reward_history),
            "max_reward": EvaluationMetrics.max_reward(reward_history),
            "std_reward": EvaluationMetrics.std_reward(reward_history),
            "success_rate": EvaluationMetrics.success_rate(reward_history),
        }
    )


@app.post("/qualia/sync")
def sync_qualia(payload: SyncPayload):
    """Actualiza el estado emocional desde otra instancia."""
    for tipo, valor in payload.emociones.items():
        register_emotion(tipo, float(valor))
    if payload.pad:
        pad_state.update(payload.pad)
    return JSONResponse({"status": "ok"})
