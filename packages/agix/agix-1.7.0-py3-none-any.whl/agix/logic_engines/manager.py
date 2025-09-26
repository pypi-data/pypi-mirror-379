"""Gestor de motores lógicos."""

from importlib import metadata
from typing import Dict, Iterable

from .base import LogicEngine


class LogicEngineManager:
    """Carga motores registrados bajo el grupo ``agix.logic_engines``."""

    def __init__(self) -> None:
        self.engines: Dict[str, LogicEngine] = {}

    def register(self, engine: LogicEngine) -> None:
        """Registra un motor disponible."""
        self.engines[engine.__class__.__name__] = engine

    def discover(self) -> None:
        """Descubre e instancia motores a través de *entry points*."""
        eps: Iterable[metadata.EntryPoint] = metadata.entry_points(group="agix.logic_engines")
        for ep in eps:
            engine_cls = ep.load()
            engine = engine_cls()
            self.register(engine)

    def get(self, name: str) -> LogicEngine:
        """Obtiene un motor por nombre de clase."""
        return self.engines[name]
