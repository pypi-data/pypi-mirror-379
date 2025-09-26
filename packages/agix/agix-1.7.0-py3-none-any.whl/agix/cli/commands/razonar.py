# src/agix/cli/commands/razonar.py
"""Subcomando para realizar razonamiento simb\u00f3lico simple."""

import argparse
from typing import Optional, List
import re

from src.agix.reasoning.logic_core import LogicCore, Fact, Rule

# Expresi\u00f3n regular para hechos tipo pred(arg1,arg2,...)
FACT_RE = re.compile(r"^(?P<pred>\w+)\((?P<args>[^()]*)\)$")


def parse_fact(text: str) -> Fact:
    """Convierte una cadena en un :class:`Fact`."""
    text = text.strip()
    match = FACT_RE.match(text)
    if match:
        pred = match.group("pred")
        args = [a.strip() for a in match.group("args").split(",") if a.strip()]
        return Fact(pred, args)
    return Fact(text, [])


def run_reasoning(args: argparse.Namespace) -> None:
    """Ejecuta un ejemplo b\u00e1sico de ``LogicCore``."""
    core = LogicCore()

    hechos_raw = args.hechos or "amigo(ana,juan);amigo(juan,maria)"
    for item in filter(None, [h.strip() for h in hechos_raw.split(';')]):
        core.add_fact(parse_fact(item))

    rule: Rule

    def condition(facts: List[Fact]) -> bool:
        nonlocal rule
        for f1 in facts:
            for f2 in facts:
                if (
                    f1.predicate == "amigo"
                    and f2.predicate == "amigo"
                    and len(f1.args) == 2
                    and len(f2.args) == 2
                    and f1.args[1] == f2.args[0]
                ):
                    rule.consequence = Fact("amigo", [f1.args[0], f2.args[1]])
                    return True
        return False

    rule = Rule(condition=condition, consequence=Fact("amigo", []), description="Transitividad de amistad")
    core.add_rule(rule)

    print("\nHechos iniciales:")
    for f in core.list_facts():
        print(f" - {f}")

    nuevos = core.infer()

    if nuevos:
        print("\nHechos inferidos:")
        for nf in nuevos:
            print(f" * {nf}")
    else:
        print("\nNo se infiri\u00f3 ning\u00fan hecho nuevo.")


def build_parser(parser: Optional[argparse.ArgumentParser] = None) -> argparse.ArgumentParser:
    """Construye el ``ArgumentParser`` para ``razonar``."""
    if parser is None:
        parser = argparse.ArgumentParser(description="Ejemplo de razonamiento simb\u00f3lico")

    parser.add_argument(
        "--hechos",
        type=str,
        help="Lista de hechos separados por ';', ej: 'amigo(ana,juan);amigo(juan,maria)'",
    )

    return parser


__all__ = ["run_reasoning", "build_parser"]
