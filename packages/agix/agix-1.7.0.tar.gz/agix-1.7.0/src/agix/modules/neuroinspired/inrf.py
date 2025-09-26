"""Implementaciones ligeras de componentes INRF inspirados en la corteza visual."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, ClassVar, Dict, Iterable, List, Optional, Tuple

import numpy as np

try:  # pragma: no cover - solo se ejecuta cuando SciPy está disponible
    from scipy.signal import convolve2d as _scipy_convolve2d
except Exception:  # pragma: no cover - el fallback se documenta más adelante
    _scipy_convolve2d = None

Activation = Callable[[np.ndarray], np.ndarray]


def _relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0.0, x)


def _identity(x: np.ndarray) -> np.ndarray:
    return x


def _sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def _tanh(x: np.ndarray) -> np.ndarray:
    return np.tanh(x)


ACTIVATIONS = {
    "relu": _relu,
    "linear": _identity,
    "identity": _identity,
    "sigmoid": _sigmoid,
    "tanh": _tanh,
}


class ActivationNotFoundError(ValueError):
    """Se lanza cuando no se localiza una activación registrada."""


@dataclass
class INRFNeuron:
    """Neurona elemental del modelo INRF.

    Parameters
    ----------
    kernel: Iterable[Iterable[float]]
        Núcleo espacial aplicado en la convolución feed-forward.
    alpha: float
        Intensidad de la retroalimentación (α). Si es cero se opera de forma puramente
        feed-forward.
    activation: str
        Nombre de la no linealidad a emplear. Valores soportados: ``relu``, ``tanh``,
        ``sigmoid`` e ``identity``. Por defecto se usa ``relu``.
    custom_activation: Callable[[np.ndarray], np.ndarray], optional
        Función de activación personalizada que sustituye al nombre por defecto.
    feedback_kernel: Iterable[Iterable[float]], optional
        Núcleo a utilizar para el cálculo de la señal de retroalimentación. Si no se
        proporciona se reutiliza ``kernel``.
    """

    kernel: Iterable[Iterable[float]]
    alpha: float = 0.0
    activation: str = "relu"
    custom_activation: Optional[Activation] = None
    feedback_kernel: Optional[Iterable[Iterable[float]]] = None
    _activation_fn: Activation = field(init=False, repr=False)
    _kernel_array: np.ndarray = field(init=False, repr=False)
    _kernel_flipped: np.ndarray = field(init=False, repr=False)
    _feedback_kernel_array: np.ndarray = field(init=False, repr=False)
    _feedback_kernel_flipped: np.ndarray = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._kernel_array = self._as_kernel(self.kernel)
        self._kernel_flipped = np.flip(self._kernel_array, axis=(0, 1))
        feedback = (
            self._as_kernel(self.feedback_kernel)
            if self.feedback_kernel is not None
            else self._kernel_array
        )
        self._feedback_kernel_array = feedback
        self._feedback_kernel_flipped = np.flip(self._feedback_kernel_array, axis=(0, 1))
        self._activation_fn = self._resolve_activation(self.activation, self.custom_activation)

    @staticmethod
    def _as_kernel(kernel: Iterable[Iterable[float]]) -> np.ndarray:
        array = np.asarray(kernel, dtype=float)
        if array.ndim != 2:
            raise ValueError("El kernel debe ser bidimensional")
        if array.shape[0] % 2 == 0 or array.shape[1] % 2 == 0:
            raise ValueError("El kernel debe tener dimensiones impares para mantener el centro")
        return array

    @staticmethod
    def _resolve_activation(name: str, custom: Optional[Activation]) -> Activation:
        if custom is not None:
            return custom
        try:
            return ACTIVATIONS[name.lower()]
        except KeyError as exc:
            raise ActivationNotFoundError(f"Activación desconocida: {name!r}") from exc

    def forward(
        self,
        stimulus: np.ndarray,
        feedback: Optional[np.ndarray] = None,
        dynamic_alpha: Optional[float] = None,
    ) -> np.ndarray:
        """Calcula la respuesta de la neurona ante un estímulo.

        Parameters
        ----------
        stimulus:
            Mapa de entrada bidimensional.
        feedback:
            Mapa de retroalimentación. Si se omite se reutiliza ``stimulus`` cuando ``alpha``
            sea distinto de cero.
        dynamic_alpha:
            Valor de α calculado dinámicamente para esta evaluación. Si es ``None`` se utiliza
            el ``alpha`` configurado en la instancia.
        """

        stimulus_array = np.asarray(stimulus, dtype=float)
        feedforward = self._convolve2d(
            stimulus_array,
            self._kernel_array,
            self._kernel_flipped,
        )
        alpha = self.alpha if dynamic_alpha is None else dynamic_alpha
        if alpha:
            feedback_source = stimulus_array if feedback is None else np.asarray(feedback, dtype=float)
            feedback_term = self._convolve2d(
                feedback_source,
                self._feedback_kernel_array,
                self._feedback_kernel_flipped,
            )
            feedforward = feedforward + alpha * feedback_term
        return self._activation_fn(feedforward)

    @staticmethod
    def _convolve2d(
        data: np.ndarray,
        kernel: np.ndarray,
        flipped_kernel: np.ndarray,
    ) -> np.ndarray:
        """Convoluciona ``data`` con ``kernel`` usando padding reflectivo.

        Se prioriza el backend vectorizado de SciPy cuando está disponible.
        En entornos donde SciPy no se puede importar, se recurre a un fallback
        puramente basado en NumPy que utiliza ventanas deslizantes y
        ``numpy.einsum`` para minimizar bucles explícitos.
        """

        kh, kw = flipped_kernel.shape
        pad_h = kh // 2
        pad_w = kw // 2
        padded = np.pad(data, ((pad_h, pad_h), (pad_w, pad_w)), mode="reflect")
        if _scipy_convolve2d is not None:
            return _scipy_convolve2d(padded, kernel, mode="valid")
        windows = np.lib.stride_tricks.sliding_window_view(padded, (kh, kw))
        return np.einsum("ij,xyij->xy", flipped_kernel, windows, optimize=True)


class ModeNotSupportedError(ValueError):
    """Se lanza cuando se solicita un modo no soportado por :class:`V1Layer`."""


def build_mode(mode: str) -> str:
    """Normaliza el modo recibido asegurando que sea uno de los soportados."""

    normalized = mode.lower()
    if normalized not in {"classic", "neuroinspired", "hybrid"}:
        raise ModeNotSupportedError(
            f"Modo '{mode}' no soportado. Utiliza 'classic', 'neuroinspired' o 'hybrid'."
        )
    return normalized


@dataclass
class V1Layer:
    """Capa simplificada de la corteza visual primaria que agrupa neuronas INRF."""

    _KERNEL_CACHE: ClassVar[Dict[Tuple[int, int], Tuple[np.ndarray, ...]]] = {}

    num_filters: int = 4
    kernel_size: int = 5
    alpha: float = 0.0
    activation: str = "relu"
    mode: str = "classic"
    custom_activation: Optional[Activation] = None

    def __post_init__(self) -> None:
        self.mode = build_mode(self.mode)
        self._kernels = list(self._get_orientation_kernels(self.num_filters, self.kernel_size))
        self._neurons = self._build_neurons()
        self._last_output: Optional[np.ndarray] = None
        self._dynamic_alpha_cache = np.zeros(self.num_filters, dtype=float)
        self._linspace_indices = np.arange(self.num_filters, dtype=float)

    def _build_neurons(self) -> List[INRFNeuron]:
        neurons: List[INRFNeuron] = []
        for idx in range(self.num_filters):
            kernel = self._kernels[idx]
            neuron_alpha = self._alpha_for_mode(idx)
            neuron = INRFNeuron(
                kernel=kernel,
                alpha=neuron_alpha,
                activation=self.activation,
                custom_activation=self.custom_activation,
            )
            neurons.append(neuron)
        return neurons

    def _alpha_for_mode(self, index: int) -> float:
        if self.mode == "classic":
            return 0.0
        if self.mode == "neuroinspired":
            return self.alpha
        # hybrid: escalamos ligeramente la retroalimentación en función del filtro
        scaling = 0.5 + 0.5 * np.cos(2 * np.pi * index / max(1, self.num_filters))
        return self.alpha * scaling * 0.5

    @staticmethod
    def _create_orientation_kernels(num_filters: int, kernel_size: int) -> List[np.ndarray]:
        if kernel_size % 2 == 0:
            raise ValueError("kernel_size debe ser impar para mantener el centro del filtro")
        radius = kernel_size // 2
        y, x = np.mgrid[-radius : radius + 1, -radius : radius + 1]
        sigma = kernel_size / 3.0
        gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))
        kernels: List[np.ndarray] = []
        for idx in range(num_filters):
            theta = np.pi * idx / max(1, num_filters)
            wave = np.cos((x * np.cos(theta) + y * np.sin(theta)) * np.pi / radius)
            kernel = gaussian * wave
            kernel = kernel - kernel.mean()
            norm = np.linalg.norm(kernel)
            if norm:
                kernel = kernel / norm
            kernels.append(kernel)
        return kernels

    @classmethod
    def _get_orientation_kernels(cls, num_filters: int, kernel_size: int) -> Tuple[np.ndarray, ...]:
        key = (num_filters, kernel_size)
        cached = cls._KERNEL_CACHE.get(key)
        if cached is None:
            cached = tuple(cls._create_orientation_kernels(num_filters, kernel_size))
            cls._KERNEL_CACHE[key] = cached
        return cached

    def forward(self, stimulus: np.ndarray, feedback: Optional[np.ndarray] = None) -> np.ndarray:
        """Ejecuta un paso de inferencia sobre el estímulo recibido."""

        outputs: List[np.ndarray] = []
        dynamic_alpha = self._compute_dynamic_alpha(stimulus)
        for idx, neuron in enumerate(self._neurons):
            neuron_feedback = self._select_feedback(stimulus, feedback, idx)
            response = neuron.forward(stimulus, neuron_feedback, dynamic_alpha=dynamic_alpha[idx])
            outputs.append(response)
        stacked = np.stack(outputs, axis=0)
        self._last_output = stacked
        return stacked

    def _select_feedback(
        self,
        stimulus: np.ndarray,
        external_feedback: Optional[np.ndarray],
        index: int,
    ) -> Optional[np.ndarray]:
        if self.mode == "classic":
            return None
        if external_feedback is not None:
            return external_feedback
        if self.mode == "neuroinspired" and self._last_output is not None:
            return self._last_output[index]
        if self.mode == "hybrid" and self._last_output is not None:
            averaged = self._last_output.mean(axis=0)
            return 0.5 * averaged + 0.5 * stimulus
        return stimulus

    def _compute_dynamic_alpha(self, stimulus: np.ndarray) -> np.ndarray:
        base = self.alpha if self.mode != "classic" else 0.0
        if base == 0.0:
            self._dynamic_alpha_cache.fill(0.0)
            return self._dynamic_alpha_cache
        energy = np.mean(np.square(stimulus))
        modulation = np.clip(energy, 0.0, 1.0)
        if self.mode == "neuroinspired":
            value = base * (0.5 + 0.5 * modulation)
            self._dynamic_alpha_cache.fill(value)
            return self._dynamic_alpha_cache
        # hybrid
        scaling = 0.3 + 0.7 * modulation
        start = base * 0.25
        stop = base * scaling
        if self.num_filters == 1:
            self._dynamic_alpha_cache[0] = stop
            return self._dynamic_alpha_cache
        span = stop - start
        denominator = self.num_filters - 1
        self._dynamic_alpha_cache[:] = start + (span / denominator) * self._linspace_indices
        return self._dynamic_alpha_cache

    @property
    def last_output(self) -> Optional[np.ndarray]:
        """Devuelve el último mapa de activaciones calculado."""

        return self._last_output

    def set_mode(self, mode: str) -> None:
        """Permite alternar el modo de funcionamiento en tiempo de ejecución."""

        self.mode = build_mode(mode)
        for idx, neuron in enumerate(self._neurons):
            neuron.alpha = self._alpha_for_mode(idx)

    def summary(self) -> str:
        """Genera un resumen textual de la configuración actual de la capa."""

        lines = [
            "V1Layer",
            f"  num_filters: {self.num_filters}",
            f"  kernel_size: {self.kernel_size}",
            f"  activation: {self.activation if self.custom_activation is None else 'custom'}",
            f"  mode: {self.mode}",
            f"  alpha: {self.alpha}",
        ]
        return "\n".join(lines)
