# src/agix/evaluation/formal/architecture_comparator.py

from agix.evaluation.metrics import EvaluationMetrics
import numpy as np

class ArchitectureComparator:
    """
    Herramienta para comparar dos arquitecturas de agentes en un entorno común.
    Mide: recompensa promedio, robustez, tasa de éxito, explicabilidad, etc.
    """

    def __init__(self, env, perturb_fn=None):
        self.env = env
        self.perturb_fn = perturb_fn

    def run_comparison(self, agent_a, agent_b, episodes=5, threshold=1.0):
        rewards_a = self.run_trials(agent_a, episodes)
        rewards_b = self.run_trials(agent_b, episodes)

        results = {
            "agent_a": self.compute_metrics(agent_a, rewards_a, threshold),
            "agent_b": self.compute_metrics(agent_b, rewards_b, threshold)
        }
        return results

    def run_trials(self, agent, episodes):
        reward_list = []
        for _ in range(episodes):
            obs = self.env.reset()
            total = 0
            done = False
            while not done:
                agent.perceive(obs)
                action = agent.decide()
                obs, reward, done, _ = self.env.step(action)
                agent.learn(reward)
                total += reward
            reward_list.append(total)
        return reward_list

    def compute_metrics(self, agent, rewards, threshold):
        return {
            "avg_reward": EvaluationMetrics.average_reward(rewards),
            "max_reward": EvaluationMetrics.max_reward(rewards),
            "std_reward": EvaluationMetrics.std_reward(rewards),
            "success_rate": EvaluationMetrics.success_rate(rewards, threshold),
            "explainability": EvaluationMetrics.explainability_score(str(agent))
        }
