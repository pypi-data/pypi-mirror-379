from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Set

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
import uvicorn


class EmotionalState(dict):
    """Representa el estado emocional compartido con dimensiones PAD."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        """Inicializa el estado asegurando la presencia del vector PAD."""
        super().__init__(*args, **kwargs)
        self._ensure_pad()

    def _ensure_pad(self) -> None:
        self.setdefault(
            "pad",
            {"pleasure": 0.0, "arousal": 0.0, "dominance": 0.0},
        )

    def update(self, *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        """Actualiza el estado, separando el bloque PAD si existe."""
        pad = None
        if args:
            arg = dict(args[0])
            pad = arg.pop("pad", None)
            super().update(arg)
        if kwargs:
            pad = kwargs.pop("pad", pad)
            super().update(kwargs)
        if pad:
            self["pad"].update(pad)
        self._ensure_pad()

    def clear(self) -> None:  # type: ignore[override]
        """Resetea el estado dejando el vector PAD por defecto."""
        super().clear()
        self._ensure_pad()


def _state_path() -> Path:
    return Path(__file__).with_name("emotional_state.json")


EMOTIONAL_STATE = EmotionalState()


class EmotionHub:
    """Gestiona y sincroniza el estado emocional del sistema."""

    def __init__(self) -> None:
        self.state = EMOTIONAL_STATE
        self.app = FastAPI(title="Emotion Hub")
        self.clients: Set[WebSocket] = set()
        self._load_state()
        self._setup_routes()

    # ------------------------------------------------------------------
    def _load_state(self) -> None:
        path = _state_path()
        if path.exists():
            try:
                data = json.loads(path.read_text())
                if isinstance(data, dict):
                    self.state.update(data)
            except Exception:
                pass

    def _save_state(self) -> None:
        path = _state_path()
        path.write_text(json.dumps(self.state))

    # ------------------------------------------------------------------
    def _setup_routes(self) -> None:
        @self.app.get("/qualia")
        def _get_state():
            state = dict(self.state)
            pad = state.pop("pad", self.state["pad"])
            return JSONResponse({"state": state, "pad": pad})

        @self.app.post("/qualia")
        def _set_state(payload: Dict[str, Any]):
            self.state.update(payload)
            self._save_state()
            state = dict(self.state)
            pad = state.pop("pad", self.state["pad"])
            return JSONResponse({"status": "ok", "state": state, "pad": pad})

        @self.app.post("/qualia/sync")
        def _sync_state(payload: Dict[str, Any]):
            self.state.clear()
            self.state.update(payload)
            self._save_state()
            state = dict(self.state)
            pad = state.pop("pad", self.state["pad"])
            return JSONResponse({"status": "ok", "state": state, "pad": pad})

        @self.app.websocket("/ws/qualia")
        async def _ws(ws: WebSocket):
            await ws.accept()
            self.clients.add(ws)
            state = dict(self.state)
            pad = state.pop("pad", self.state["pad"])
            await ws.send_json({"state": state, "pad": pad})
            try:
                while True:
                    data = await ws.receive_json()
                    if isinstance(data, dict):
                        pad = data.pop("pad", None)
                        self.state.update(data)
                        if pad:
                            self.state.update({"pad": pad})
                        self._save_state()
                        current = dict(self.state)
                        p = current.pop("pad", self.state["pad"])
                        for client in list(self.clients):
                            await client.send_json({"state": current, "pad": p})
            except WebSocketDisconnect:
                self.clients.remove(ws)

    # ------------------------------------------------------------------
    def run(self, host: str = "127.0.0.1", port: int = 9010) -> None:
        """Arranca el servidor HTTP de EmotionHub."""
        uvicorn.run(self.app, host=host, port=port)
