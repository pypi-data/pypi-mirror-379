from __future__ import annotations

"""Módulo para almacenar y consultar experiencias narrativas."""

from dataclasses import dataclass, field
from typing import Any, Dict, List
import json
import sqlite3
import string

import numpy as np


@dataclass
class Experience:
    """Representa una experiencia con texto y metadatos asociados."""

    text: str
    metadata: Dict[str, Any]


@dataclass
class SelfModel:
    """Modelo interno que resume rasgos derivados de experiencias."""

    values: Dict[str, int] = field(default_factory=dict)
    goals: Dict[str, int] = field(default_factory=dict)
    affective_states: Dict[str, int] = field(default_factory=dict)
    history: List[Dict[str, Dict[str, int]]] = field(default_factory=list)
    planning_score: float = 0.5
    motivation_score: float = 0.5

    # ------------------------------------------------------------------
    def update_self_model(self, experience: Experience) -> None:
        """Actualiza rasgos y almacena un snapshot del estado."""

        for val in experience.metadata.get("values", []):
            self.values[val] = self.values.get(val, 0) + 1
        for goal in experience.metadata.get("goals", []):
            self.goals[goal] = self.goals.get(goal, 0) + 1
        affects = experience.metadata.get("affective_states") or []
        if isinstance(affects, str):
            affects = [affects]
        for aff in affects:
            self.affective_states[aff] = self.affective_states.get(aff, 0) + 1

        snapshot = {
            "values": self.values.copy(),
            "goals": self.goals.copy(),
            "affective_states": self.affective_states.copy(),
        }
        self.history.append(snapshot)

    # ------------------------------------------------------------------
    def evaluate_action(self, action_description: str) -> Dict[str, float]:
        """Evalúa la compatibilidad de una acción con el ``SelfModel``.

        Analiza el texto de la acción buscando coincidencias con los valores,
        objetivos y estados afectivos predominantes. A partir de esas
        coincidencias ajusta los *scores* de planificación y motivación.

        Parameters
        ----------
        action_description:
            Descripción simbólica de la acción a evaluar.

        Returns
        -------
        dict
            Diccionario con el ``compatibility`` calculado y los nuevos
            ``planning_score`` y ``motivation_score``.
        """

        tokens = set(action_description.lower().split())
        goal_matches = tokens & set(self.goals.keys())
        value_matches = tokens & set(self.values.keys())
        affect_matches = tokens & set(self.affective_states.keys())

        total_matches = (
            len(goal_matches) + len(value_matches) + len(affect_matches)
        )
        compatibility = total_matches / max(len(tokens), 1)

        if goal_matches:
            self.planning_score = min(
                1.0, self.planning_score + 0.1 * len(goal_matches)
            )
        else:
            self.planning_score = max(0.0, self.planning_score - 0.05)

        if affect_matches:
            self.motivation_score = min(
                1.0, self.motivation_score + 0.1 * len(affect_matches)
            )
        else:
            self.motivation_score = max(0.0, self.motivation_score - 0.05)

        return {
            "compatibility": round(compatibility, 3),
            "planning_score": round(self.planning_score, 3),
            "motivation_score": round(self.motivation_score, 3),
        }


class AutonarrativeCore:
    """Gestor ligero de experiencias con soporte de embeddings y consultas."""

    def __init__(self, db_path: str = ":memory:") -> None:
        self.conn = sqlite3.connect(db_path)
        self.self_model = SelfModel()
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS experiences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                metadata TEXT,
                embedding BLOB
            )
            """
        )
        self.conn.commit()

    # ------------------------------------------------------------------
    def _embed(self, text: str) -> np.ndarray:
        """Genera un embedding determinista basado en frecuencias de letras."""
        vec = np.zeros(26, dtype=np.float32)
        for ch in text.lower():
            if ch in string.ascii_lowercase:
                vec[ord(ch) - 97] += 1.0
        norm = np.linalg.norm(vec)
        if norm:
            vec /= norm
        return vec

    # ------------------------------------------------------------------
    def store_experience(self, experience: Experience) -> int:
        """Calcula el embedding y persiste la experiencia."""
        emb = self._embed(experience.text)
        metadata_json = json.dumps(experience.metadata)
        cur = self.conn.execute(
            "INSERT INTO experiences (text, metadata, embedding) VALUES (?, ?, ?)",
            (experience.text, metadata_json, emb.tobytes()),
        )
        self.conn.commit()
        self.self_model.update_self_model(experience)
        return int(cur.lastrowid)

    # ------------------------------------------------------------------
    def query_experiences(
        self, query_text: str, filters: Dict[str, Any] | None = None
    ) -> List[Experience]:
        """Devuelve experiencias relevantes mediante similitud coseno."""
        filters = filters or {}
        q_emb = self._embed(query_text)
        rows = self.conn.execute(
            "SELECT text, metadata, embedding FROM experiences"
        ).fetchall()
        resultados: List[tuple[float, Experience]] = []
        for text, metadata_json, emb_blob in rows:
            metadata = json.loads(metadata_json)
            if filters and not all(metadata.get(k) == v for k, v in filters.items()):
                continue
            emb = np.frombuffer(emb_blob, dtype=np.float32)
            denom = np.linalg.norm(q_emb) * np.linalg.norm(emb)
            sim = float(np.dot(q_emb, emb) / denom) if denom else 0.0
            resultados.append((sim, Experience(text=text, metadata=metadata)))
        resultados.sort(key=lambda x: x[0], reverse=True)
        return [exp for _, exp in resultados]

    # ------------------------------------------------------------------
    def evaluate_action(self, action_description: str) -> Dict[str, float]:
        """Proxy hacia ``SelfModel.evaluate_action``."""
        return self.self_model.evaluate_action(action_description)
