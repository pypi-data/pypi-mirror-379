# agi_lab/evaluation/metrics.py

import numpy as np
import hashlib
from dataclasses import dataclass

from src.agix.evaluation import NarrativeCompressionEvaluator


@dataclass
class IntentionMetrics:
    """Resultados obtenidos del ``IntentionEvaluator``."""

    intention_moral_score: float
    goal_conflict_score: float
    consequence_simulation: dict


class EvaluationMetrics:
    """
    Clase utilitaria para calcular métricas de evaluación de AGI:
    - Generalidad de tarea
    - Transferencia
    - Autonomía
    - Robustez
    - Explicabilidad
    - Recompensa promedio, máxima, desviación estándar, tasa de éxito
    """

    @staticmethod
    def generality_score(agent, tasks, threshold=0.8):
        """
        Mide en cuántas tareas el agente supera cierto umbral de desempeño.
        """
        success_count = 0
        for env in tasks:
            obs = env.reset()
            total_reward = 0
            done = False
            while not done:
                agent.perceive(obs)
                action = agent.decide()
                obs, reward, done, _ = env.step(action)
                agent.learn(reward, done)
                total_reward += reward
            if total_reward >= threshold:
                success_count += 1
        return success_count / len(tasks)

    @staticmethod
    def intention_metrics(moral_score: float, conflict_score: float, consequence: dict) -> IntentionMetrics:
        """Empaqueta los resultados del ``IntentionEvaluator`` en un dataclass."""
        return IntentionMetrics(moral_score, conflict_score, consequence)

    @staticmethod
    def transfer_score(agent, task_seq):
        """
        Evalúa cuánto conocimiento se transfiere entre tareas.
        """
        deltas = []
        for i in range(1, len(task_seq)):
            env = task_seq[i]
            obs = env.reset()
            reward_pre = 0
            for _ in range(10):  # sin entrenamiento
                agent.perceive(obs)
                action = agent.decide()
                obs, reward, done, _ = env.step(action)
                reward_pre += reward
                if done: break

            agent.reset()
            obs = env.reset()
            reward_post = 0
            for _ in range(10):  # con entrenamiento mínimo
                agent.perceive(obs)
                action = agent.decide()
                obs, reward, done, _ = env.step(action)
                agent.learn(reward)
                reward_post += reward
                if done: break

            delta = (reward_post - reward_pre) / max(reward_post, 1e-6)
            deltas.append(delta)
        return np.mean(deltas)

    @staticmethod
    def robustness_score(agent, env, perturb_fn, runs=5):
        """
        Mide estabilidad bajo perturbaciones del entorno.
        """
        drops = []
        for _ in range(runs):
            obs = env.reset()
            total_normal = 0
            done = False
            while not done:
                agent.perceive(obs)
                action = agent.decide()
                obs, reward, done, _ = env.step(action)
                agent.learn(reward)
                total_normal += reward

            obs = env.reset()
            env = perturb_fn(env)
            total_perturbed = 0
            done = False
            while not done:
                agent.perceive(obs)
                action = agent.decide()
                obs, reward, done, _ = env.step(action)
                total_perturbed += reward

            drop = (total_normal - total_perturbed) / max(total_normal, 1e-6)
            drops.append(drop)
        return 1 - np.mean(drops)

    @staticmethod
    def explainability_score(symbolic_model):
        """
        Mide explicabilidad por compresibilidad lógica.
        Asume que el modelo simbólico es un string o estructura parseable.
        """
        length = len(str(symbolic_model))
        compressed = len(hashlib.sha256(str(symbolic_model).encode()).hexdigest())
        return compressed / max(length, 1)

    @staticmethod
    def average_reward(reward_list):
        if not reward_list:
            return 0.0
        return float(np.mean(reward_list))

    @staticmethod
    def max_reward(reward_list):
        if not reward_list:
            return 0.0
        return float(np.max(reward_list))

    @staticmethod
    def std_reward(reward_list):
        if not reward_list:
            return 0.0
        return float(np.std(reward_list))

    @staticmethod
    def success_rate(reward_list, threshold=1.0):
        if not reward_list:
            return 0.0
        successes = [1 for r in reward_list if r >= threshold]
        return len(successes) / len(reward_list)
    @staticmethod
    def fagi_index(task_scores, adaptability_scores, transfer_scores, weights=None):
        """
        Índice F_AGI(π): mide generalidad y adaptabilidad combinada.
        - task_scores: lista de desempeños en tareas específicas [0-1]
        - adaptability_scores: lista de robustez/adaptación a entornos cambiantes [0-1]
        - transfer_scores: lista de capacidad de transferencia entre tareas [0-1]
        - weights: dict opcional con {'task', 'adaptability', 'transfer'} (suman 1)

        Devuelve un valor entre 0 y 1.
        """
        if weights is None:
            weights = {"task": 0.33, "adaptability": 0.33, "transfer": 0.34}

        task_score = np.mean(task_scores) if task_scores else 0.0
        adaptability_score = np.mean(adaptability_scores) if adaptability_scores else 0.0
        transfer_score = np.mean(transfer_scores) if transfer_scores else 0.0

        fagi = (
            weights["task"] * task_score +
            weights["adaptability"] * adaptability_score +
            weights["transfer"] * transfer_score
        )
        return round(fagi, 4)

    @staticmethod
    def narrative_alpha(original_lengths, recall_lengths):
        """Calcula \u03b1 usando regresi\u00f3n logar\u00edtmica."""
        return NarrativeCompressionEvaluator.estimate_alpha(original_lengths, recall_lengths)

    @staticmethod
    def narrative_semantic_precision(original, recalled):
        """Similitud sem\u00e1ntica entre texto original y recordado."""
        return NarrativeCompressionEvaluator.semantic_precision(original, recalled)

