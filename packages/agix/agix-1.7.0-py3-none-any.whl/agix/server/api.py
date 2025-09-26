from __future__ import annotations

from dataclasses import asdict
from threading import Lock
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.agix.adapters.service import ServiceAdapter
from src.agix.architecture.ameta import AMetaArchitecture, AGIModule
from src.agix.memory import GestorDeMemoria


class PerceptionModule(AGIModule):
    """Módulo de percepción que pasa la observación sin cambios."""

    def process(self, observation: Any) -> Any:
        return observation


class InferenceModule(AGIModule):
    """Módulo de inferencia mínimo."""

    def process(self, data: Any) -> Any:
        return data


class DecisionModule(AGIModule):
    """Calcula una acción numérica simple a partir de la observación."""

    def process(self, inferred_state: Any) -> int:
        if isinstance(inferred_state, (list, tuple)):
            return len(inferred_state)
        if isinstance(inferred_state, (int, float)):
            return int(inferred_state)
        return 0


class MemoryModule(AGIModule):
    """Registra experiencias en ``GestorDeMemoria`` con sincronización."""

    def __init__(self, memory: GestorDeMemoria, lock: Lock) -> None:
        self.memory = memory
        self.lock = lock

    def process(self, experience: Any) -> None:
        """Registra experiencias manejando distintos formatos de entrada."""
        with self.lock:
            if isinstance(experience, tuple) and len(experience) == 2:
                obs, action = experience
                self.memory.registrar(str(obs), str(action), "", True)
            elif isinstance(experience, dict):
                self.memory.registrar(
                    str(experience.get("entrada", "")),
                    str(experience.get("decision", "")),
                    str(experience.get("resultado", "")),
                    bool(experience.get("exito", True)),
                )
            else:  # pragma: no cover - formatos no esperados
                raise ValueError("Formato de experiencia no soportado")


memory_manager = GestorDeMemoria()
memory_lock = Lock()
architecture = AMetaArchitecture(
    P=PerceptionModule(),
    I=InferenceModule(),
    D=DecisionModule(),
    M=MemoryModule(memory_manager, memory_lock),
)

service_adapter = ServiceAdapter()

app = FastAPI(title="AGIX API")


@app.post("/infer")
def infer(payload: Dict[str, Any]):
    """Procesa una observación y devuelve la acción calculada."""
    observation = service_adapter.adapt_input(payload)
    action = architecture.cycle(observation)
    return JSONResponse(service_adapter.adapt_output(action))


@app.post("/learn")
def learn(payload: Dict[str, Any]):
    """Guarda una experiencia completa proporcionada por el usuario."""
    architecture.modules["M"].process(payload)
    return JSONResponse({"status": "ok"})


@app.get("/memory")
def get_memory():
    """Devuelve las experiencias almacenadas."""
    with memory_lock:
        data = [asdict(exp) for exp in memory_manager.experiencias]
    return JSONResponse({"experiencias": data})

