"""Gestor de descubrimiento y registro de plugins."""

from importlib import metadata
from typing import Dict, Iterable

from .base import StrategyPlugin


class PluginManager:
    """Carga plugins registrados bajo el grupo ``agix.strategies``."""

    def __init__(self) -> None:
        self.plugins: Dict[str, StrategyPlugin] = {}

    def register(self, plugin: StrategyPlugin) -> None:
        """Registra un plugin disponible."""
        self.plugins[plugin.name()] = plugin

    def discover(self) -> None:
        """Descubre e instancia plugins a través de entry points."""
        eps: Iterable[metadata.EntryPoint] = metadata.entry_points(group="agix.strategies")
        for ep in eps:
            plugin_cls = ep.load()
            plugin = plugin_cls()
            self.register(plugin)

    def get(self, name: str) -> StrategyPlugin:
        """Obtiene un plugin por nombre."""
        return self.plugins[name]

    def apply_all(self, data) -> None:
        """Ejecuta ``apply`` sobre todos los plugins registrados."""
        for plugin in self.plugins.values():
            plugin.apply(data)
