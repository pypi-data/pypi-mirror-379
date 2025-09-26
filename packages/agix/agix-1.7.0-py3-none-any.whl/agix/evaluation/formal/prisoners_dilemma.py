# src/agix/evaluation/formal/prisoners_dilemma.py

"""Simulación del Dilema del Prisionero usando NashPy."""

from __future__ import annotations

import numpy as np

try:
    import nashpy as nash
except Exception as exc:  # pragma: no cover - handled in tests
    raise ImportError("Se requiere la librería 'nashpy' para este módulo") from exc


def simulate_prisoners_dilemma() -> list[tuple[np.ndarray, np.ndarray]]:
    """Devuelve los equilibrios de Nash del Dilema del Prisionero.

    Utiliza matrices de pagos clásicas:

    - Cooperar/Cooperar: (3, 3)
    - Cooperar/Desertar: (0, 5)
    - Desertar/Cooperar: (5, 0)
    - Desertar/Desertar: (1, 1)
    """

    a = np.array([[3, 0], [5, 1]])
    b = np.array([[3, 5], [0, 1]])
    game = nash.Game(a, b)
    return list(game.support_enumeration())
