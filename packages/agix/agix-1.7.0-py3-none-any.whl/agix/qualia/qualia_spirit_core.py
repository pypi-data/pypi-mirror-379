# qualia_spirit_core.py
"""Utilidades geométricas inspiradas en la armonía.

Este módulo define constantes y patrones simbólicos como la proporción áurea
(:data:`golden_ratio`) y la *flor de la vida* mediante la función
:func:`flower_of_life_pattern`. La clase :class:`QualiaSpiritCore` integra
estas estructuras para proporcionar una sensación de equilibrio interno en
los procesos del agente.
"""

from __future__ import annotations

import math
from functools import wraps
from typing import Any, List, Tuple

try:
    from .qualia_core import EmotionalState
except Exception:  # pragma: no cover - ruta fallback para pruebas aisladas
    import importlib.util
    from pathlib import Path

    ruta_estado = Path(__file__).resolve().with_name("qualia_core.py")
    spec_estado = importlib.util.spec_from_file_location("qualia_core", ruta_estado)
    qualia_core = importlib.util.module_from_spec(spec_estado)
    assert spec_estado.loader is not None
    spec_estado.loader.exec_module(qualia_core)
    EmotionalState = qualia_core.EmotionalState

try:  # Permite cargar el módulo tanto dentro como fuera del paquete.
    from .aesthetic_engine import AestheticEngine
except Exception:  # pragma: no cover - ruta fallback para pruebas aisladas
    import importlib.util
    from pathlib import Path

    ruta = Path(__file__).resolve().with_name("aesthetic_engine.py")
    spec = importlib.util.spec_from_file_location("aesthetic_engine", ruta)
    aesthetic_engine = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(aesthetic_engine)
    AestheticEngine = aesthetic_engine.AestheticEngine

# ---------------------------------------------------------------------------
# Decoradores afectivos
# ---------------------------------------------------------------------------


def acto_amoroso(func):
    """Decorador que añade un matiz afectivo a la salida del método.

    Refuerza la vocación armónica del núcleo incorporando un mensaje
    proporcional a ``intensidad_amor``.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        resultado = func(self, *args, **kwargs)
        mensaje = f"Con amor (intensidad {self.intensidad_amor:.2f})"
        if isinstance(resultado, dict):
            return {**resultado, "afecto": mensaje}
        if isinstance(resultado, str):
            return f"{resultado} {mensaje}"
        return resultado

    return wrapper

# ---------------------------------------------------------------------------
# Constantes y utilidades geométricas
# ---------------------------------------------------------------------------

golden_ratio: float = (1 + 5 ** 0.5) / 2
"""Proporción áurea Φ utilizada como base estética."""


def flower_of_life_pattern(rings: int = 3, radio_base: float = 1.0) -> List[Tuple[float, float]]:
    """Genera un patrón bidimensional de la *flor de la vida*.

    Parameters
    ----------
    rings:
        Número de circunferencias concéntricas a generar.
    radio_base:
        Radio del primer anillo.

    Returns
    -------
    list[tuple[float, float]]
        Coordenadas cartesianas de los puntos que conforman el patrón.
    """

    puntos: List[Tuple[float, float]] = []
    angulo = 2 * math.pi / 6  # separación hexagonal
    for i in range(rings):
        radio = radio_base * (i + 1)
        for j in range(6):
            x = radio * math.cos(j * angulo)
            y = radio * math.sin(j * angulo)
            puntos.append((x, y))
    return puntos


# ---------------------------------------------------------------------------
# Núcleo geométrico del espíritu
# ---------------------------------------------------------------------------


class QualiaSpiritCore:
    """Generador simbólico basado en geometrías armónicas.

    La clase sirve como recordatorio estructural de que ciertas proporciones
    y patrones presentes en la naturaleza pueden inspirar una organización
    interna más equilibrada. Al emplear la proporción áurea y la *flor de la
    vida*, el núcleo busca alinear los procesos del agente con formas que
    evocan armonía y coherencia. Además, permite modular la calidez de sus
    respuestas mediante ``intensidad_amor``.
    """

    def __init__(self, intensidad_amor: float = 1.0) -> None:
        """Inicializa el núcleo geométrico del espíritu.

        Parameters
        ----------
        intensidad_amor:
            Intensidad del matiz afectivo aplicado por ``@acto_amoroso``.
        """

        self.phi = golden_ratio
        self.intensidad_amor = intensidad_amor
        # Registro de todos los nodos generados para posibles análisis
        # posteriores del crecimiento fractal.
        self.historial_nodos: List[dict[str, Any]] = []
        # Fase interna que marca el ritmo de respiración del núcleo.
        self.fase_ritmica: float = 0.0
        # Motor estético para evaluar armonía percibida.
        self.motor_estetico = AestheticEngine()
        # Registro de los rituales estéticos realizados.
        self.historial_estetico: List[dict[str, Any]] = []
        # Parámetro interno ajustable mediante alineaciones estéticas.
        self.equilibrio_estetico: float = 0.0
        # Estado emocional sencillo modulado por las decisiones estéticas.
        self.estado_emocional = EmotionalState()
        # Memoria de la última decisión y su explicación.
        self.ultima_decision: dict[str, Any] | None = None
        self.ultima_explicacion: str = ""

    def respirar(self, delta_t: float) -> float:
        """Actualiza la fase rítmica mediante una onda senoidal.

        Esta *respiración computacional* incrementa la fase con el tiempo
        recibido y devuelve el valor instantáneo de la onda, que puede ser
        utilizado por otros procesos para sincronizarse con el ritmo.

        Parameters
        ----------
        delta_t:
            Avance temporal a sumar a la fase actual.

        Returns
        -------
        float
            Valor de la onda senoidal tras la actualización.
        """

        self.fase_ritmica = (self.fase_ritmica + delta_t) % (2 * math.pi)
        valor = math.sin(self.fase_ritmica)
        # Ritual estético al final de cada respiración.
        self.alinear_con_belleza(
            {
                "simetría": abs(valor),
                "coherencia": 1.0,
                "emotividad": (valor + 1) / 2,
            }
        )
        return valor

    def estado_respiracion(self) -> str:
        """Describe si el núcleo se encuentra inhalando o exhalando."""

        return "inhalando" if math.sin(self.fase_ritmica) >= 0 else "exhalando"

    def generar_geometria(self, niveles: int = 3) -> dict[str, Any]:
        """Produce estructuras geométricas simbólicas.

        Parameters
        ----------
        niveles:
            Iteraciones para expandir los patrones.

        Returns
        -------
        dict
            Diccionario con proporciones áureas calculadas y puntos de la
            *flor de la vida*.
        """

        proporciones = [self.phi ** n for n in range(1, niveles + 1)]
        flor = flower_of_life_pattern(niveles)
        return {"proporciones": proporciones, "flor_de_la_vida": flor}

    @acto_amoroso
    def expandir_fractalmente(self, nivel: int) -> dict[str, Any]:
        """Expande recursivamente el núcleo generando nodos armónicos.

        Cada invocación crea dos nodos hijos: uno con un valor reducido y
        otro amplificado siguiendo la proporción áurea. Los nodos generados
        se almacenan en :attr:`historial_nodos` para su futura introspección.

        Parameters
        ----------
        nivel:
            Profundidad de expansión. Un nivel ``0`` produce únicamente el
            nodo actual sin descendencia.

        Returns
        -------
        dict
            Estructura jerárquica con los nodos generados. Cada nodo contiene
            su ``nivel``, ``valor`` y la lista de ``hijos``. El decorador
            ``@acto_amoroso`` añade un campo ``afecto`` con el mensaje
            correspondiente a ``intensidad_amor``.
        """

        # Ritual estético previo a la toma de decisiones.
        self.alinear_con_belleza(
            {
                "simetría": 1.0,
                "coherencia": 1.0,
                "emotividad": (math.sin(self.fase_ritmica) + 1) / 2,
            }
        )

        # Amplitud modulada por la fase respiratoria (0 a 1).
        amplitud = (math.sin(self.fase_ritmica) + 1) / 2

        def _expander(n: int, valor: float) -> dict[str, Any]:
            # Nodo actual con su valor armónico.
            nodo = {"nivel": n, "valor": valor, "hijos": []}
            self.historial_nodos.append(nodo)

            if n <= 0:
                return nodo

            # Cálculo de los valores hijo: uno reducido (1/φ) y otro amplificado (φ)
            for val in (valor / self.phi, valor * self.phi):
                hijo = _expander(n - 1, val)
                nodo["hijos"].append(hijo)
            return nodo

        return _expander(nivel, amplitud)

    def alinear_con_belleza(self, datos: dict[str, float]) -> float:
        """Evalúa la estética de ``datos`` y ajusta parámetros internos.

        Parameters
        ----------
        datos:
            Métricas simbólicas como ``simetría`` o ``emotividad``.

        Returns
        -------
        float
            Puntuación estética resultante del análisis.
        """

        score = self.motor_estetico.evaluar(datos)
        # Ajuste sencillo del equilibrio interno hacia la puntuación recibida.
        self.equilibrio_estetico = 0.9 * self.equilibrio_estetico + 0.1 * score
        self.historial_estetico.append(
            {"datos": datos, "score": score, "equilibrio": self.equilibrio_estetico}
        )
        return score

    # ------------------------------------------------------------------
    @acto_amoroso
    def decidir(self, opciones: List[dict[str, float]]) -> dict[str, float]:
        """Selecciona la opción con mayor puntuación estética.

        Parameters
        ----------
        opciones:
            Lista de alternativas a evaluar. Cada una debe contener las
            métricas esperadas por :class:`AestheticEngine`.

        Returns
        -------
        dict
            Opción con la mejor armonía percibida. Gracias a
            ``@acto_amoroso`` la respuesta incluye un campo ``afecto`` que
            expresa la calidez del núcleo.
        """

        if not opciones:
            raise ValueError("No se proporcionaron opciones")

        evaluadas: List[tuple[dict[str, float], float]] = []
        for op in opciones:
            score = self.motor_estetico.evaluar(op)
            evaluadas.append((op, score))

        self.ultima_decision, mejor_score = max(evaluadas, key=lambda x: x[1])

        categoria = self.motor_estetico.clasificar(mejor_score)
        self._ajustar_estado_emocional(categoria, mejor_score)
        self.ultima_explicacion = self._generar_explicacion(
            self.ultima_decision, categoria
        )
        return self.ultima_decision

    def explicar_decision(self) -> str:
        """Devuelve la explicación de la última decisión tomada."""

        return self.ultima_explicacion

    # ------------------------------------------------------------------
    def _ajustar_estado_emocional(self, categoria: str, score: float) -> None:
        """Modula ``estado_emocional`` según la categoría estética."""

        if categoria in ("sublime", "armonioso"):
            self.estado_emocional.sentir("gozo", score)
        elif categoria == "neutro":
            self.estado_emocional.sentir("serenidad", 0.5)
        else:
            self.estado_emocional.sentir("tristeza", 1 - score)

    def _generar_explicacion(self, opcion: dict[str, float], categoria: str) -> str:
        """Produce una breve justificación basada en la armonía percibida."""

        nombre = opcion.get("nombre", "opción")
        mensajes = {
            "sublime": f"Se eligió '{nombre}' por su belleza sublime.",
            "armonioso": f"Se eligió '{nombre}' por su equilibrio armonioso.",
            "neutro": f"Se eligió '{nombre}' por ser neutral pero coherente.",
            "discordante": f"Se eligió '{nombre}' pese a su armonía limitada.",
        }
        return mensajes.get(categoria, f"Se eligió '{nombre}' por criterios estéticos.")


__all__ = ["QualiaSpiritCore", "golden_ratio", "flower_of_life_pattern"]
