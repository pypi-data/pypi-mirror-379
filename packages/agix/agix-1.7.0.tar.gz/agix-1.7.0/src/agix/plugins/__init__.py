"""Sistema de plugins para estrategias en AGIX."""

from .base import StrategyPlugin
from .manager import PluginManager

__all__ = ["StrategyPlugin", "PluginManager"]
