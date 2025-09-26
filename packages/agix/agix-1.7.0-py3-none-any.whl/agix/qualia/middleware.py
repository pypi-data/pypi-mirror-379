from __future__ import annotations

import logging
import threading
from typing import Any, Dict, Optional

import requests

from .network import QualiaNetworkClient
from .qualia_core import EmotionalState


logger = logging.getLogger(__name__)


class QualiaMiddleware:
    """Middleware que gestiona la sincronizaci\u00f3n emocional y la conexi\u00f3n de agentes."""

    def __init__(
        self,
        base_url: str,
        token: Optional[str] = None,
        heartbeat_interval: float = 30.0,
        session: Optional[Any] = None,
    ) -> None:
        self.session = session or requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        self.client = QualiaNetworkClient(base_url, session=self.session)
        self.state = EmotionalState()
        self.heartbeat_interval = heartbeat_interval
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    # ------------------------------------------------------------------
    def register_agent(self, name: str, metadata: Optional[Dict[str, Any]] = None) -> Any:
        """Registra un agente en el hub remoto."""
        return self.client.registrar_modulo(name, metadata or {})

    def push_state(self) -> Any:
        """Env\u00eda el estado emocional local al servidor remoto."""
        payload = {"emociones": self.state.emociones, "tono": self.state.tono_general()}
        return self.client.enviar_estado(payload)

    def pull_state(self) -> EmotionalState:
        """Actualiza el estado emocional local con la informaci\u00f3n remota."""
        data = self.client.obtener_estado()
        self.state.emociones = data.get("emociones", {})
        return self.state

    # ------------------------------------------------------------------
    def start_heartbeat(self) -> None:
        """Inicia un hilo que env\u00eda pings peri\u00f3dicamente."""
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._heartbeat_loop, daemon=True)
        self._thread.start()

    def stop_heartbeat(self) -> None:
        """Detiene el hilo de heartbeat."""
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=1)
            self._thread = None

    def _heartbeat_loop(self) -> None:
        while not self._stop_event.is_set():
            backoff = min(1.0, self.heartbeat_interval)
            for attempt in range(3):
                try:
                    self.client.difundir_evento("ping", timeout=self.client.timeout)
                    break
                except requests.RequestException as exc:
                    logger.error(
                        "Error en heartbeat (intento %s): %s", attempt + 1, exc
                    )
                    if attempt < 2:
                        self._stop_event.wait(backoff)
                        backoff *= 2
            self._stop_event.wait(self.heartbeat_interval)
