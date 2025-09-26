"""Herramientas para exportar evaluaciones a sistemas de prueba formal."""

from typing import Dict
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def _resolver_ruta(ruta: str | Path) -> Path:
    """Resuelve la ruta asegurando que esté dentro del directorio actual."""
    path = Path(ruta).expanduser().resolve()
    permitido = Path.cwd().resolve()
    try:
        path.relative_to(permitido)
    except ValueError as exc:
        logger.error("Intento de acceso fuera del directorio permitido: %s", path)
        raise PermissionError("Ruta fuera del directorio permitido") from exc
    return path


def export_to_coq(resultados: Dict[str, float], ruta: str | Path) -> str:
    """Guarda los resultados en un archivo Coq (.v)."""
    path = _resolver_ruta(ruta)
    with open(path, "w", encoding="utf-8") as f:
        f.write("(* Resultados generados por AGI Core *)\n")
        for nombre, valor in resultados.items():
            f.write(f"Definition {nombre} := {valor}.\n")
    return str(path)


def export_to_lean(resultados: Dict[str, float], ruta: str | Path) -> str:
    """Guarda los resultados en un archivo Lean (.lean)."""
    path = _resolver_ruta(ruta)
    with open(path, "w", encoding="utf-8") as f:
        f.write("-- Resultados generados por AGI Core\n")
        for nombre, valor in resultados.items():
            f.write(f"def {nombre} := {valor}\n")
    return str(path)

