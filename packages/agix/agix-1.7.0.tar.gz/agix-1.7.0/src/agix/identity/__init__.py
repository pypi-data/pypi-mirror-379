"""Submódulos relacionados con la identidad del agente."""

try:  # pragma: no cover - import opcional
    from .personality import PersonalityProfile
    __all__ = ["PersonalityProfile"]
except Exception:  # noqa: BLE001
    # Permite cargar submódulos de forma aislada sin depender de todo el paquete
    __all__ = []
