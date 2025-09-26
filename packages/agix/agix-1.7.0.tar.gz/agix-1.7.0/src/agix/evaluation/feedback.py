"""Herramientas simples de retroalimentación para agentes AGIX."""

from typing import Any, Dict


def evaluar(entrada: Any, decision: Any, resultado: Any) -> Dict[str, Any]:
    """Evalúa una acción y su resultado devolviendo éxito y puntaje.

    La heurística básica considera un resultado numérico positivo como éxito
    o bien cadenas de texto que contengan términos asociados a un resultado
    satisfactorio ("exito", "ok", "success").
    """
    score = 0.0

    if isinstance(resultado, (int, float)):
        score = float(resultado)
    elif isinstance(resultado, str):
        lower = resultado.lower()
        if any(pal in lower for pal in ("exito", "éxito", "ok", "success")):
            score = 1.0
    exito = score > 0
    return {"exito": exito, "score": float(score)}

