import argparse
from typing import Optional

import uvicorn

from agix.server import api


def run_server(args):
    """Lanza el servidor REST de AGIX."""
    if args.dry_run:
        print(f"Servidor listo en http://{args.host}:{args.port}")
        return
    uvicorn.run(api.app, host=args.host, port=args.port)


def build_parser(parser: Optional[argparse.ArgumentParser] = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser(description="Inicia el servidor REST de AGIX")
        
        parser.add_argument("--host", default="0.0.0.0", help="Host de escucha")
        parser.add_argument("--host", default="127.0.0.1", help="Host de escucha")
        parser.add_argument("--port", type=int, default=8000, help="Puerto del servidor")
        parser.add_argument("--dry-run", action="store_true", help="Solo mostrar información y salir")

    return parser
