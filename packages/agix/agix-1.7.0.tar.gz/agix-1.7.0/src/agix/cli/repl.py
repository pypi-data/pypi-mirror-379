import argparse
from typing import Optional
import cmd
import logging

from src.agix.security.blocker import verificar

from agix.agents.genetic import GeneticAgent
from agix.agents.narrative import NarrativeAgent
from agix.agents.affective_npc import AffectiveNPC
from agix.environments.env_base import SimpleEnvironment


AGENTS = {
    "genetic": GeneticAgent,
    "geneticagent": GeneticAgent,
    "narrative": NarrativeAgent,
    "narrativeagent": NarrativeAgent,
    "affective": AffectiveNPC,
    "affectivenpc": AffectiveNPC,
}


class AGIXRepl(cmd.Cmd):
    """REPL interactivo para agentes AGIX."""

    intro = "\n🤖 Bienvenido al AGIX REPL. Escribe 'help' para ver comandos.\n"
    prompt = "agix> "

    def __init__(self) -> None:
        super().__init__()
        self.agent = None
        self.env = None
        self.steps = 0
        self.total_reward = 0.0
        self.observation = None

    # ------------------------------------------------------------------
    def precmd(self, line: str) -> str:
        """Verifica el comando antes de procesarlo."""
        if not verificar(line):
            if self.agent and hasattr(self.agent, "memory"):
                self.agent.memory.registrar("bloqueo", line, "", False)
            print("Comando bloqueado.")
            return ""
        return line

    def do_load_agent(self, arg: str) -> None:
        """Carga un agente disponible."""
        name = arg.strip().lower()
        cls = AGENTS.get(name)
        if not cls:
            print(f"Agente '{name}' no disponible. Opciones: {list(AGENTS.keys())}")
            return

        self.env = SimpleEnvironment()
        try:
            self.agent = cls(action_space_size=self.env.action_space_size)
        except TypeError:
            self.agent = cls()
        self.observation = self.env.reset()
        self.steps = 0
        self.total_reward = 0.0
        print(f"Agente {name} cargado.")

    def do_step(self, arg: str) -> None:
        """Ejecuta un paso del agente en el entorno."""
        if not self.agent or not self.env:
            print("Primero carga un agente con load-agent")
            return

        self.agent.perceive(self.observation)
        try:
            action = self.agent.decide()
        except RuntimeError as exc:
            logging.error("Error en decide: %s", exc)
            action = 0
        except Exception as exc:
            logging.exception("Error inesperado en decide: %s", exc)
            action = 0
        self.observation, reward, done, _ = self.env.step(action)
        try:
            self.agent.learn(reward, done=done)
        except RuntimeError as exc:
            logging.error("Error en learn: %s", exc)
        except Exception as exc:
            logging.exception("Error inesperado en learn: %s", exc)
        self.steps += 1
        self.total_reward += reward
        print(f"Paso {self.steps} | Acción: {action} | Recompensa: {reward:.2f}")
        if done:
            print("Episodio terminado.")
            self.observation = self.env.reset()

    def do_status(self, arg: str) -> None:
        """Muestra métricas acumuladas."""
        print(f"Pasos ejecutados: {self.steps} | Recompensa acumulada: {self.total_reward:.2f}")

    def do_exit(self, arg: str) -> bool:
        """Sale del REPL."""
        print("Hasta pronto.")
        return True

    def do_quit(self, arg: str) -> bool:  # alias
        return self.do_exit(arg)

    def do_EOF(self, arg: str) -> bool:  # Ctrl+D
        print()
        return self.do_exit(arg)

    def emptyline(self) -> None:
        pass


def run_repl(args: argparse.Namespace) -> None:
    """Inicia el bucle interactivo."""
    AGIXRepl().cmdloop()


def build_parser(parser: Optional[argparse.ArgumentParser] = None) -> argparse.ArgumentParser:
    """Construye el parser para ``repl``."""
    if parser is None:
        parser = argparse.ArgumentParser(description="REPL interactivo para AGIX")
    return parser


__all__ = ["run_repl", "build_parser", "AGIXRepl"]
