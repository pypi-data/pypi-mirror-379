"""AGI core package."""

import logging

if not logging.getLogger().handlers:
    logging.basicConfig(level=logging.INFO)

__version__ = "1.1.0"

__all__ = [
    "agents",
    "architecture",
    "cli",
    "control",
    "dashboard",
    "autoagent",
    "autonarrative",
    "environments",
    "learning",
    "memory",
    "perception",
    "reasoning",
    "experiments",
    "server",
    "orchestrator",
    "security",
    "metacognition",
    "ethics",
    "language",
    "logic_engines",
    "modules",
]
