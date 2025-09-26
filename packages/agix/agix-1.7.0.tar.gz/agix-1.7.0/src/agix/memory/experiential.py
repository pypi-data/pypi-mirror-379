"""Memoria de experiencias para agentes AGIX."""

from __future__ import annotations

import json
import logging
import sqlite3
import hashlib
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Any

from difflib import get_close_matches

try:  # pragma: no cover
    from src.agix.emotion.emotion_simulator import PADState
except Exception:  # pragma: no cover
    class PADState:  # type: ignore
        pass

logger = logging.getLogger(__name__)


@dataclass
class Experiencia:
    """Registro de una experiencia particular de un agente."""

    entrada: str
    decision: str
    resultado: str
    exito: bool
    juicio_etico: Optional[str] = None
    timestamp: Optional[str] = None
    firma: Optional[str] = None
    emocion: PADState | dict | None = None


class GestorDeMemoria:
    """Gestor simple de memoria experiencial."""

    def __init__(self, backend: str = "json", ruta: Optional[str] = None):
        self.backend = backend
        self.ruta = Path(ruta) if ruta else None
        self.experiencias: List[Experiencia] = []
        self.dialogos: List[tuple[str, str]] = []

    def _resolver_ruta(self, ruta: str | Path) -> Path:
        """Resuelve la ruta asegurando que esté dentro del directorio actual."""
        path = Path(ruta).expanduser().resolve()
        permitido = Path.cwd().resolve()
        try:
            path.relative_to(permitido)
        except ValueError as exc:
            logger.error(
                "Intento de acceso fuera del directorio permitido: %s", path
            )
            raise PermissionError("Ruta fuera del directorio permitido") from exc
        return path

    def registrar(
        self,
        entrada: str,
        decision: str,
        resultado: str,
        exito: bool,
        juicio_etico: Optional[str] = None,
        timestamp: Optional[str] = None,
        firma: Optional[str] = None,
    emocion: PADState | dict | None = None,
    ) -> Experiencia:
        """Registra una experiencia en memoria."""
        ts = timestamp or datetime.utcnow().isoformat()
        exp = Experiencia(
            entrada, decision, resultado, exito, juicio_etico, ts, firma, emocion
        )
        self.experiencias.append(exp)
        return exp

    def registrar_dialogo(
        self, mensaje_usuario: str, respuesta_agente: str
    ) -> None:
        """Guarda un par de diálogo entre el usuario y el agente."""
        self.dialogos.append((mensaje_usuario, respuesta_agente))

    def store_experience(self, data: Any) -> str:
        """Genera una firma \u00fanica para la experiencia y la registra."""
        firma = hashlib.sha256(repr(data).encode("utf-8")).hexdigest()
        self.registrar("qualia", "generate_state", repr(data), True, firma=firma)
        return firma

    def obtener_recientes(self, n: int = 5) -> List[Experiencia]:
        """Obtiene las experiencias m\u00e1s recientes."""
        return self.experiencias[-n:]

    # ------------------------------------------------------------------
    def guardar(self, ruta: Optional[str] = None) -> None:
        """Persiste las experiencias en el backend configurado."""
        ruta_final = Path(ruta) if ruta else self.ruta
        if ruta_final is None:
            raise ValueError("Se requiere una ruta para guardar la memoria")
        ruta_final = self._resolver_ruta(ruta_final)

        if self.backend == "json":
            data = {
                "experiencias": [
                    {
                        **asdict(e),
                        "emocion": asdict(e.emocion)
                        if isinstance(e.emocion, PADState)
                        else e.emocion,
                    }
                    for e in self.experiencias
                ],
                "dialogos": self.dialogos,
            }
            with open(ruta_final, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        elif self.backend == "sqlite":
            conn = sqlite3.connect(ruta_final)
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS experiencias (
                    entrada TEXT,
                    decision TEXT,
                    resultado TEXT,
                    exito INTEGER,
                    juicio_etico TEXT,
                    timestamp TEXT,
                    firma TEXT,
                    emocion TEXT
                )
                """
            )
            cur.executemany(
                "INSERT INTO experiencias VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                [
                    (
                        e.entrada,
                        e.decision,
                        e.resultado,
                        int(e.exito),
                        e.juicio_etico,
                        e.timestamp,
                        e.firma,
                        json.dumps(
                            asdict(e.emocion)
                            if isinstance(e.emocion, PADState)
                            else e.emocion
                        )
                        if e.emocion is not None
                        else None,
                    )
                    for e in self.experiencias
                ],
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS dialogos (
                    mensaje TEXT,
                    respuesta TEXT
                )
                """
            )
            cur.executemany(
                "INSERT INTO dialogos VALUES (?, ?)", self.dialogos
            )
            conn.commit()
            conn.close()
        else:
            raise ValueError(f"Backend no soportado: {self.backend}")

    # ------------------------------------------------------------------
    def cargar(self, ruta: Optional[str] = None) -> None:
        """Carga experiencias desde el backend indicado."""
        ruta_final = Path(ruta) if ruta else self.ruta
        if ruta_final is None:
            raise ValueError("Se requiere una ruta para cargar la memoria")
        ruta_final = self._resolver_ruta(ruta_final)

        if self.backend == "json":
            with open(ruta_final, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                self.experiencias = [Experiencia(**d) for d in data]
                self.dialogos = []
            else:
                self.experiencias = [
                    Experiencia(**d) for d in data.get("experiencias", [])
                ]
                self.dialogos = [tuple(d) for d in data.get("dialogos", [])]
        elif self.backend == "sqlite":
            conn = sqlite3.connect(ruta_final)
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS experiencias (
                    entrada TEXT,
                    decision TEXT,
                    resultado TEXT,
                    exito INTEGER,
                    juicio_etico TEXT,
                    timestamp TEXT,
                    firma TEXT,
                    emocion TEXT
                )
                """
            )
            cur.execute(
                "SELECT entrada, decision, resultado, exito, juicio_etico, timestamp, firma, emocion FROM experiencias"
            )
            rows = cur.fetchall()
            self.experiencias = [
                Experiencia(
                    entrada,
                    decision,
                    resultado,
                    bool(exito),
                    juicio,
                    timestamp,
                    firma,
                    json.loads(emocion) if emocion else None,
                )
                for entrada, decision, resultado, exito, juicio, timestamp, firma, emocion in rows
            ]
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS dialogos (
                    mensaje TEXT,
                    respuesta TEXT
                )
                """
            )
            cur.execute("SELECT mensaje, respuesta FROM dialogos")
            self.dialogos = [(m, r) for m, r in cur.fetchall()]
            conn.close()
        else:
            raise ValueError(f"Backend no soportado: {self.backend}")

    # ------------------------------------------------------------------
    def buscar_similar(self, consulta: str, campo: str = "entrada", n: int = 1) -> List[Experiencia]:
        """Devuelve las experiencias más parecidas a la consulta."""
        if campo not in {"entrada", "decision", "resultado", "juicio_etico"}:
            raise ValueError("Campo inválido para búsqueda")
        corpus = [getattr(e, campo) for e in self.experiencias]
        coincidencias = get_close_matches(consulta, corpus, n=n)
        return [e for e in self.experiencias if getattr(e, campo) in coincidencias]
