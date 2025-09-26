"""Herramientas de bloqueo y verificación de comandos.

Para agregar un nuevo patrón, añade una expresión regular compilada a
``FORBIDDEN_PATTERNS`` y cubre la regla con una prueba de evasión en
``tests/test_security/test_blocker.py``.
"""

from __future__ import annotations

import re

FORBIDDEN_PATTERNS = [
    re.compile(r"import\s+os"),
    re.compile(r"import\s+sys"),
    re.compile(r"import\s+subprocess"),
    re.compile(r"os\s*\.\s*system"),
    re.compile(r"subprocess\s*\.\s*popen"),
    re.compile(r"eval\s*\("),
    re.compile(r"exec\s*\("),
]


def verificar(texto: str) -> bool:
    """Devuelve ``True`` si el texto no contiene patrones prohibidos."""
    lower = texto.lower()
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(lower):
            return False
    return True


__all__ = ["FORBIDDEN_PATTERNS", "verificar"]
