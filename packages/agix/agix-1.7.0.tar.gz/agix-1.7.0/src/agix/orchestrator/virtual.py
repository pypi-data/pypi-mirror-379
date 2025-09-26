from __future__ import annotations

"""Coordinador virtual de Qualia con reglas de seguridad."""

from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:  # pragma: no cover - handled at runtime
    yaml = None  # type: ignore

from agix.qualia.network import QualiaNetworkClient
from agix.security.blocker import verificar


class VirtualQualia:
    """Coordina varios :class:`QualiaNetworkClient` aplicando reglas básicas.

    La configuraci\u00f3n se carga desde un archivo YAML y puede incluir
    par\u00e1metros como ``memory_limit`` (n\u00famero m\u00e1ximo de estados
    recordados) y ``allow_events`` para habilitar o no la difusi\u00f3n de
    eventos.
    """

    def __init__(
        self,
        clients: Optional[List[QualiaNetworkClient]] = None,
        config_path: Optional[str] = None,
    ) -> None:
        self.clients: List[QualiaNetworkClient] = clients or []
        # Valores por defecto
        self.config: Dict[str, Any] = {
            "memory_limit": 10,
            "allow_events": True,
        }
        if config_path:
            self.load_config(config_path)
        self._memory: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    def load_config(self, path: str) -> None:
        """Carga la configuraci\u00f3n desde un archivo YAML."""
        if yaml is None:
            raise ImportError("PyYAML es requerido para cargar configuraciones")
        with open(path, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        if not isinstance(data, dict):
            raise ValueError("El archivo de configuraci\u00f3n debe contener un mapeo")
        self.config.update(data)

    # ------------------------------------------------------------------
    def add_client(self, client: QualiaNetworkClient) -> None:
        """Registra un nuevo cliente."""
        self.clients.append(client)

    # ------------------------------------------------------------------
    def broadcast_state(self, state: Dict[str, Any]) -> List[Any]:
        """Env\u00eda un estado a todos los clientes verificando seguridad."""
        if not verificar(str(state)):
            raise ValueError("Estado contiene patrones prohibidos")
        self._remember(state)
        responses = []
        for client in self.clients:
            responses.append(client.enviar_estado(state))
        return responses

    # ------------------------------------------------------------------
    def broadcast_event(self, event: str) -> List[Any]:
        """Difunde un evento si est\u00e1 permitido y es seguro."""
        if not self.config.get("allow_events", True):
            return []
        if not verificar(event):
            raise ValueError("Evento contiene patrones prohibidos")
        responses = []
        for client in self.clients:
            responses.append(client.difundir_evento(event))
        return responses

    # ------------------------------------------------------------------
    def _remember(self, state: Dict[str, Any]) -> None:
        """Almacena el estado respetando el l\u00edmite de memoria."""
        limit = int(self.config.get("memory_limit", 0))
        if limit <= 0:
            return
        self._memory.append(state)
        if len(self._memory) > limit:
            self._memory.pop(0)

    @property
    def memory(self) -> List[Dict[str, Any]]:
        """Devuelve una copia de la memoria interna."""
        return list(self._memory)


__all__ = ["VirtualQualia"]
