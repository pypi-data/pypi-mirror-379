import argparse
from typing import Optional

from agix.orchestrator import QualiaHub


def run_hub(args: argparse.Namespace) -> None:
    """Lanza un QualiaHub local."""
    if not args.start:
        print("Use --start para iniciar el hub")
        return

    hub = QualiaHub()
    if args.dry_run:
        print(f"Hub listo en http://{args.host}:{args.port}")
        return
    hub.run(host=args.host, port=args.port)


def build_parser(parser: Optional[argparse.ArgumentParser] = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser(description="Inicia un QualiaHub local")

    parser.add_argument("--start", action="store_true", help="Inicia el hub")
    parser.add_argument("--host", default="127.0.0.1", help="Host de escucha")
    parser.add_argument("--port", type=int, default=9000, help="Puerto del hub")
    parser.add_argument("--dry-run", action="store_true", help="Solo mostrar información y salir")
    return parser
