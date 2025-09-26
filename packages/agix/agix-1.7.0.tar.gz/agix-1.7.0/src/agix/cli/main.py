# src/agix/cli/main.py

import argparse
from src.agix.cli import qualia_shell
from src.agix.cli import qualia_shell, repl
from src.agix.cli.commands import (
    simulate,
    inspect,
    evaluate,
    train_ml,
    razonar,
    serve,
    autoagent,
    train_ml,
    experiment,
    razonar,
    serve,
    hub,
)


def main():
    parser = argparse.ArgumentParser(
        description="AGI Core CLI - Interfaz de línea de comandos para simulación, inspección y evaluación de agentes."
    )

    subparsers = parser.add_subparsers(title="comandos disponibles", dest="command")

    # Subcomando: simulate
    sim_parser = subparsers.add_parser(
        "simulate", help="Simula un agente", description="Simula un agente AGI simple en un entorno mínimo"
    )
    simulate.build_parser(sim_parser)

    # Subcomando: autoagent
    auto_parser = subparsers.add_parser(
        "autoagent",
        help="Ejecuta el bucle AutoAgent",
        description="Lanza un ciclo de agente y entorno",
    )
    autoagent.build_parser(auto_parser)

    # Subcomando: inspect
    insp_parser = subparsers.add_parser(
        "inspect", help="Inspecciona el agente", description="Inspecciona el estado reflexivo del agente AGI"
    )
    inspect.build_parser(insp_parser)

    # Subcomando: evaluate
    eval_parser = subparsers.add_parser(
        "evaluate", help="Evalúa el agente", description="Evaluación del agente AGI"
    )
    evaluate.build_parser(eval_parser)

    # Subcomando: experiment
    exp_parser = subparsers.add_parser(
        "experiment",
        help="Ejecuta experimentos",
        description="Ejecuta series de pruebas comparativas",
    )
    experiment.build_parser(exp_parser)

    # Subcomando: train_ml
    train_parser = subparsers.add_parser(
        "train_ml", help="Entrena un modelo ML", description="Entrena un modelo de aprendizaje automático"
    )
    train_ml.build_parser(train_parser)

    # Subcomando: qualia
    qualia_parser = subparsers.add_parser(
        "qualia", help="Shell interactivo de Qualia", description="Interactúa con QualiaSpirit"
    )
    qualia_shell.build_parser(qualia_parser)

    # Subcomando: repl
    repl_parser = subparsers.add_parser(
        "repl",
        help="REPL interactivo",
        description="Ejecuta ciclos paso a paso con agentes",
    )
    repl.build_parser(repl_parser)

    # Subcomando: razonar
    raz_parser = subparsers.add_parser(
        "razonar",
        help="Demostraci\u00f3n de LogicCore",
        description="Procesa hechos y aplica reglas b\u00e1sicas",
    )
    razonar.build_parser(raz_parser)

    # Subcomando: serve
    serve_parser = subparsers.add_parser(
        "serve",
        help="Inicia el servidor REST",
        description="Lanza la API REST de AGIX",
    )
    serve.build_parser(serve_parser)

    # Subcomando: hub
    hub_parser = subparsers.add_parser(
        "hub",
        help="Inicia un QualiaHub local",
        description="Arranca un hub de orquestaci\u00f3n de m\u00f3dulos",
    )
    hub.build_parser(hub_parser)
    # Parsear argumentos
    args = parser.parse_args()

    if args.command == "simulate":
        simulate.run_simulation(args)
    elif args.command == "inspect":
        inspect.run_inspection(args)
    elif args.command == "evaluate":
        evaluate.run_evaluation(args)
    elif args.command == "experiment":
        experiment.run_experiment(args)
    elif args.command == "train_ml":
        train_ml.run_training(args)
    elif args.command == "autoagent":
        autoagent.run_autoagent(args)
    elif args.command == "razonar":
        razonar.run_reasoning(args)
    elif args.command == "serve":
        serve.run_server(args)
    elif args.command == "hub":
        hub.run_hub(args)
    elif args.command == "repl":
        repl.run_repl(args)
    elif args.command == "qualia":
        qualia_shell.run_shell(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
