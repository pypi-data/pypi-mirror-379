from __future__ import annotations

"""Evaluación sencilla de la auto-organización del agente.

Este módulo genera escenarios sintéticos de interacción entre módulos y
calcula un puntaje de auto-organización para cada uno de ellos.
"""

from dataclasses import dataclass
from typing import Dict, List
import random
import importlib.util
from pathlib import Path

# Carga dinámica para evitar dependencias pesadas de ``agix.metacognition``
_spec = importlib.util.spec_from_file_location(
    "_self_org",
    Path(__file__).resolve().parents[1] / "metacognition" / "self_organization.py",
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)  # type: ignore[attr-defined]
SelfOrganizationMonitor = _module.SelfOrganizationMonitor


@dataclass
class Scenario:
    """Representa un escenario simplificado de actividad interna."""

    active_modules: List[str]
    dependencies: Dict[str, List[str]]
    activation_times: List[float]


def generate_random_scenario(rng: random.Random, num_modules: int = 3) -> Scenario:
    """Genera un escenario aleatorio de módulos y dependencias."""

    modules = [f"m{i}" for i in range(num_modules)]
    dependencies: Dict[str, List[str]] = {}
    for m in modules:
        others = [o for o in modules if o != m]
        dep_count = rng.randint(0, len(others))
        dependencies[m] = rng.sample(others, dep_count)
    activation_times = sorted(rng.uniform(0, 10) for _ in range(num_modules))
    return Scenario(modules, dependencies, list(activation_times))


def evaluate_scenario(scenario: Scenario) -> float:
    """Calcula el puntaje de auto-organización para un escenario."""

    monitor = SelfOrganizationMonitor(
        active_modules=scenario.active_modules,
        dependencies=scenario.dependencies,
        activation_times=scenario.activation_times,
    )
    return monitor.compute_score()


def run(num_scenarios: int = 5, seed: int | None = None) -> List[float]:
    """Genera ``num_scenarios`` escenarios y registra sus puntajes.

    Devuelve una lista con los puntajes calculados para cada escenario.
    """

    rng = random.Random(seed)
    scores: List[float] = []
    for idx in range(1, num_scenarios + 1):
        scenario = generate_random_scenario(rng, rng.randint(1, 5))
        score = evaluate_scenario(scenario)
        scores.append(score)
        print(f"Escenario {idx}: score={score:.3f}")
    if scores:
        avg = sum(scores) / len(scores)
        print(f"Puntaje promedio: {avg:.3f}")
    return scores
