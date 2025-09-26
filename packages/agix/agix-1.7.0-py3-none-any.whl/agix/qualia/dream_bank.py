# dream_bank.py

from typing import List, Dict
import datetime
import json
import logging
from pathlib import Path


logger = logging.getLogger(__name__)


class DreamBank:
    """
    Memoria emocional-poética del agente.
    Almacena sueños, visiones o recuerdos simbólicos con tono afectivo.
    """

    def __init__(self):
        self.suenos: List[Dict] = []

    def registrar_sueno(self, contenido: str, emocion: str, intensidad: float):
        """
        Guarda un sueño con su carga emocional.
        """
        self.suenos.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "contenido": contenido,
            "emocion": emocion,
            "intensidad": round(intensidad, 3)
        })

    def resumen_reciente(self, n: int = 3) -> List[str]:
        """
        Devuelve una lista con los últimos N sueños en forma poética.
        """
        return [
            f"({s['emocion']} · {s['intensidad']}) {s['contenido']}"
            for s in self.suenos[-n:]
        ]

    def _resolver_ruta(self, ruta: str) -> Path:
        """Resuelve la ruta asegurando que esté dentro del directorio actual."""
        path = Path(ruta).expanduser().resolve()
        permitido = Path.cwd().resolve()
        try:
            path.relative_to(permitido)
        except ValueError as exc:
            logger.error("Intento de acceso fuera del directorio permitido: %s", path)
            raise PermissionError("Ruta fuera del directorio permitido") from exc
        return path

    def exportar(self, ruta: str = "qualia_state.json"):
        """
        Guarda los sueños en un archivo JSON.
        """
        try:
            path = self._resolver_ruta(ruta)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.suenos, f, indent=2, ensure_ascii=False)
        except Exception:
            logger.exception("Error exportando sueños a %s", ruta)
            raise

    def importar(self, ruta: str = "qualia_state.json"):
        """
        Carga los sueños desde un archivo existente.
        """
        try:
            path = self._resolver_ruta(ruta)
            with open(path, "r", encoding="utf-8") as f:
                self.suenos = json.load(f)
        except FileNotFoundError:
            self.suenos = []
        except PermissionError:
            raise
        except Exception:
            logger.exception("Error importando sueños desde %s", ruta)
            raise
