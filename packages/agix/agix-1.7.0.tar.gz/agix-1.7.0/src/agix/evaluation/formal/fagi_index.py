# src/agix/evaluation/formal/fagi_index.py

import numpy as np


def compute_fagi_index(task_scores, adaptability_scores, transfer_scores, weights=None):
    """
    Calcula el índice F_AGI(π): medida de generalidad y adaptabilidad cognitiva.

    task_scores: lista de floats en [0, 1] (desempeño en tareas concretas)
    adaptability_scores: lista de floats en [0, 1] (resiliencia ante cambios)
    transfer_scores: lista de floats en [0, 1] (reutilización de conocimiento)
    weights: dict opcional con claves 'task', 'adaptability', 'transfer'
    """
    if weights is None:
        weights = {"task": 0.33, "adaptability": 0.33, "transfer": 0.34}

    task_avg = np.mean(task_scores) if task_scores else 0.0
    adaptability_avg = np.mean(adaptability_scores) if adaptability_scores else 0.0
    transfer_avg = np.mean(transfer_scores) if transfer_scores else 0.0

    fagi = (
            weights["task"] * task_avg +
            weights["adaptability"] * adaptability_avg +
            weights["transfer"] * transfer_avg
    )
    return round(fagi, 4)
