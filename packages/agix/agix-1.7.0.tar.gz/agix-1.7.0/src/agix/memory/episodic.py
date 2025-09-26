from __future__ import annotations

"""Memoria episódica combinando registro experiencial y narrativa."""

import json
from datetime import datetime
from typing import List, Optional

from .experiential import GestorDeMemoria, Experiencia
from .narrative import NarrativeMemoryTree
try:  # pragma: no cover
    from src.agix.emotion.emotion_simulator import PADState
except Exception:  # pragma: no cover
    class PADState:  # type: ignore
        pass


class EpisodicMemory:
    """Gestiona recuerdos episódicos con soporte narrativo y cronológico."""

    def __init__(
        self,
        k: int = 2,
        depth: int = 3,
        backend: str = "json",
        ruta: Optional[str] = None,
        auto_expand_threshold: float = 0.8,
    ) -> None:
        self.manager = GestorDeMemoria(backend=backend, ruta=ruta)
        self.tree = NarrativeMemoryTree(k=k, depth=depth)
        self.auto_expand_threshold = auto_expand_threshold

    # ------------------------------------------------------------------
    # Compatibilidad con GestorDeMemoria
    @property
    def experiencias(self) -> List[Experiencia]:
        return self.manager.experiencias

    def registrar(
        self,
        entrada: str,
        decision: str,
        resultado: str,
        exito: bool,
        juicio_etico: Optional[str] = None,
        timestamp: Optional[str] = None,
    ) -> Experiencia:
        return self.manager.registrar(
            entrada, decision, resultado, exito, juicio_etico, timestamp
        )

    def guardar(self, ruta: Optional[str] = None) -> None:
        self.manager.guardar(ruta)

    def cargar(self, ruta: Optional[str] = None) -> None:
        self.manager.cargar(ruta)

    def buscar_similar(self, consulta: str, campo: str = "entrada", n: int = 1) -> List[Experiencia]:
        return self.manager.buscar_similar(consulta, campo, n)

    # ------------------------------------------------------------------
    # Compatibilidad con NarrativeMemoryTree
    def _auto_expand(self) -> None:
        """Expande el árbol si supera el umbral de ocupación."""
        if self.tree.load_factor() > self.auto_expand_threshold:
            self.tree.expand()

    def insert(self, content: str) -> None:
        self.tree.insert(content)
        self._auto_expand()

    def retrieve(self) -> str:
        return self.tree.retrieve()

    @property
    def root(self):
        return self.tree.root

    # ------------------------------------------------------------------
    def store_episode(
        self,
        entrada: str,
        decision: str,
        resultado: str,
        exito: bool,
        juicio_etico: Optional[str] = None,
        timestamp: Optional[str] = None,
        emocion: PADState | dict | None = None,
    ) -> Experiencia:
        """Registra un episodio e inserta un fragmento narrativo."""
        emocion_serializada = None
        if emocion is not None:
            emocion_serializada = json.loads(
                json.dumps(
                    emocion.__dict__ if isinstance(emocion, PADState) else emocion
                )
            )
        exp = self.manager.registrar(
            entrada,
            decision,
            resultado,
            exito,
            juicio_etico,
            timestamp,
            emocion=emocion_serializada,
        )
        fragment = f"{exp.timestamp}: {entrada} -> {resultado}"
        self.tree.insert(fragment)
        self._auto_expand()
        return exp

    def retrieve_context(self, inicio: str, fin: Optional[str] = None) -> List[str]:
        """Devuelve eventos entre ``inicio`` y ``fin`` en orden temporal."""
        start_dt = datetime.fromisoformat(inicio)
        end_dt = datetime.fromisoformat(fin) if fin else datetime.max
        eventos = []
        for exp in self.manager.experiencias:
            if exp.timestamp is None:
                continue
            try:
                ts = datetime.fromisoformat(exp.timestamp)
            except ValueError:
                continue
            if start_dt <= ts <= end_dt:
                eventos.append((ts, exp))
        eventos.sort(key=lambda t: t[0])
        return [f"{e.timestamp}: {e.entrada} -> {e.resultado}" for _, e in eventos]
