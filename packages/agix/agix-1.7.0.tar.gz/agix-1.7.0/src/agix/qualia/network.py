from __future__ import annotations

import json
from typing import Any, Dict, Optional

import logging
import requests

try:
    import websockets
except Exception:  # pragma: no cover - optional dependency
    websockets = None


logger = logging.getLogger(__name__)


class QualiaNetworkClient:
    """Cliente sencillo para sincronizar estados emocionales por red.

    Parameters
    ----------
    base_url:
        URL base del servidor remoto.
    session:
        Objeto de sesión compatible con ``requests``.
    timeout:
        Tiempo máximo en segundos para las peticiones HTTP.
    """

    def __init__(
        self, base_url: str, session: Optional[Any] = None, timeout: float = 5.0
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
        self.timeout = timeout

    # ----------------------------- HTTP ---------------------------------
    def enviar_estado(self, estado: Dict[str, Any]) -> Any:
        """Env\u00eda el estado emocional por HTTP POST."""
        url = f"{self.base_url}/qualia/sync"
        try:
            response = self.session.post(
                url, json=estado, timeout=self.timeout
            )
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            logger.error("Error al enviar estado: %s", exc)
            raise

    def obtener_estado(self) -> Dict[str, Any]:
        """Recupera el estado emocional remoto por HTTP."""
        url = f"{self.base_url}/qualia"
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            logger.error("Error al obtener estado: %s", exc)
            raise

    # ---------------------------- WebSocket ------------------------------
    async def enviar_estado_ws(self, estado: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Env\u00eda el estado emocional usando WebSocket si est\u00e1 disponible."""
        if websockets is None:
            raise RuntimeError("websockets no instalado")
        async with websockets.connect(f"{self.base_url}/ws") as ws:  # pragma: no cover - websocket
            await ws.send(json.dumps(estado))
            data = await ws.recv()
            return json.loads(data)
    def registrar_modulo(self, nombre: str, metadata: Dict[str, Any]) -> Any:
        """Registra un m\u00f3dulo en el QualiaHub remoto."""
        url = f"{self.base_url}/register"
        payload = {"name": nombre, "metadata": metadata}
        try:
            response = self.session.post(
                url, json=payload, timeout=self.timeout
            )
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            logger.error("Error al registrar m\u00f3dulo %s: %s", nombre, exc)
            raise

    def consultar_modulos(self) -> Dict[str, Any]:
        """Obtiene la lista de m\u00f3dulos registrados."""
        url = f"{self.base_url}/modules"
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            logger.error("Error al consultar m\u00f3dulos: %s", exc)
            raise

    def difundir_evento(self, evento: str, timeout: Optional[float] = None) -> Any:
        """Difunde un evento a trav\u00e9s del hub."""
        url = f"{self.base_url}/event"
        payload = {"event": evento}
        try:
            response = self.session.post(
                url, json=payload, timeout=timeout or self.timeout
            )
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            logger.error("Error al difundir evento %s: %s", evento, exc)
            raise
