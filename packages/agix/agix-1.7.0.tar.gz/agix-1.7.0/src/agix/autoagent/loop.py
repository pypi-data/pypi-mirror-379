from __future__ import annotations

from typing import Any, Callable, Optional

from src.agix.agents.base import AGIAgent
from src.agix.control.controller_core import ControllerCore
from src.agix.evaluation.metrics import EvaluationMetrics


class AutoAgent:
    """Bucle de ejecución autónomo para un :class:`AGIAgent`."""

    def __init__(
        self,
        agent: AGIAgent,
        environment: Any,
        evaluator: Optional[Callable[[Any, Any, Any], dict]] = None,
        controller: Optional[ControllerCore] = None,
        metrics: Optional[type[EvaluationMetrics] | EvaluationMetrics] = None,
    ) -> None:
        self.agent = agent
        self.env = environment
        self.evaluator = evaluator
        self.controller = controller
        self.metrics = metrics or EvaluationMetrics
        self.reward_history: list[float] = []

    # ------------------------------------------------------------------
    def run(self, episodes: int = 1, max_steps: Optional[int] = None) -> dict[str, float]:
        """Ejecuta el bucle percepción-decisión-acción-aprendizaje."""
        for _ in range(episodes):
            observation = self.env.reset()
            done = False
            step = 0
            while not done and (max_steps is None or step < max_steps):
                self.agent.perceive(observation)
                action = self.agent.decide()
                observation, reward, done, _ = self.env.step(action)
                self.agent.learn(reward, done=done)

                success = None
                if self.evaluator:
                    try:
                        result = self.evaluator(observation, action, reward)
                        success = bool(result.get("exito"))
                    except Exception:
                        success = None
                try:
                    self.agent.record_experience(
                        str(observation), str(action), str(reward), success
                    )
                except Exception:
                    pass

                self.reward_history.append(reward)

                if self.controller:
                    try:
                        self.controller.ciclo_control(
                            percepcion=observation,
                            metas={},
                            retroalimentacion={
                                "reward": reward,
                                "states": [],
                                "actions": [],
                                "advantages": [],
                            },
                        )
                    except Exception:
                        pass
                step += 1
        return {
            "average_reward": self.metrics.average_reward(self.reward_history),
            "max_reward": self.metrics.max_reward(self.reward_history),
            "std_reward": self.metrics.std_reward(self.reward_history),
            "success_rate": self.metrics.success_rate(self.reward_history),
        }
