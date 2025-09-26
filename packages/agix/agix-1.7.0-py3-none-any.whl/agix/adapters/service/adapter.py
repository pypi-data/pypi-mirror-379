from typing import Any, Dict

from ..base import DomainAdapter


class ServiceAdapter(DomainAdapter):
    """Adaptador para exponer agentes vía servicios HTTP."""

    def adapt_input(self, request: Dict[str, Any]) -> Any:
        """Convierte un payload HTTP en la observación interna."""
        if not isinstance(request, dict):
            raise ValueError("La petición debe ser un diccionario JSON")
        if "observation" not in request:
            raise ValueError("Falta la clave 'observation' en la petición")
        return request["observation"]

    def adapt_output(self, action: Any) -> Dict[str, Any]:
        """Formatea la acción del agente para responder al cliente."""
        return {"action": action}

