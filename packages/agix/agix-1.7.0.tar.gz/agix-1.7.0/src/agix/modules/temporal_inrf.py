"""Componentes temporales para integradores y módulos INRF con memoria."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import torch
from torch import Tensor, nn


def _clamp_decay(decay: Tensor, minimum: float, maximum: float) -> Tensor:
    """Restringe dinámicamente los valores de decaimiento."""

    return decay.clamp(min=minimum, max=maximum)


class TemporalIntegrator(nn.Module):
    """Acumulador temporal con decaimiento exponencial.

    Parameters
    ----------
    decay : float
        Factor de decaimiento exponencial :math:`\lambda \in (0, 1)` aplicado a la
        memoria interna. Valores cercanos a uno priorizan la historia, mientras que
        valores bajos favorecen la nueva entrada.
    learnable_decay : bool, default ``False``
        Permite que ``decay`` se optimice mediante gradiente.
    minimum_decay : float, default ``0.05``
        Límite inferior seguro para evitar una pérdida total de memoria.
    maximum_decay : float, default ``0.995``
        Límite superior que evita inestabilidades numéricas por acumulación.
    persistent_state : bool, default ``True``
        Si es ``True`` la memoria se mantiene entre invocaciones consecutivas hasta
        llamar a :meth:`reset_state`.
    """

    def __init__(
        self,
        decay: float = 0.8,
        *,
        learnable_decay: bool = False,
        minimum_decay: float = 0.05,
        maximum_decay: float = 0.995,
        persistent_state: bool = True,
    ) -> None:
        super().__init__()
        if not 0.0 < decay < 1.0:
            raise ValueError("decay debe pertenecer al rango (0, 1)")
        if minimum_decay <= 0.0 or maximum_decay >= 1.0:
            raise ValueError("Los límites de decaimiento deben permanecer dentro de (0, 1)")
        if minimum_decay >= maximum_decay:
            raise ValueError("minimum_decay debe ser estrictamente menor que maximum_decay")
        self.persistent_state = persistent_state
        self.minimum_decay = float(minimum_decay)
        self.maximum_decay = float(maximum_decay)
        if learnable_decay:
            self.decay = nn.Parameter(torch.tensor(decay, dtype=torch.float32))
        else:
            self.register_buffer("decay", torch.tensor(decay, dtype=torch.float32))
        self._state: Optional[Tensor] = None

    def reset_state(self) -> None:
        """Elimina la memoria acumulada."""

        self._state = None

    def _current_decay(self) -> Tensor:
        decay = _clamp_decay(self.decay, self.minimum_decay, self.maximum_decay)
        return decay

    def forward(self, stimulus: Tensor) -> Tensor:
        """Integra un estímulo actualizando la memoria interna."""

        if self._state is None or not self.persistent_state or self._state.shape != stimulus.shape:
            self._state = torch.zeros_like(stimulus)
        decay = self._current_decay()
        memory = decay * self._state + (1.0 - decay) * stimulus
        self._state = memory
        return memory


class ActivationBuffer(nn.Module):
    """Buffer FIFO para suavizar activaciones mediante agregación."""

    def __init__(self, length: int, reduction: str = "mean") -> None:
        super().__init__()
        if length <= 0:
            raise ValueError("length debe ser positivo")
        if reduction not in {"mean", "sum", "last"}:
            raise ValueError("reduction debe ser 'mean', 'sum' o 'last'")
        self.length = int(length)
        self.reduction = reduction
        self._buffer: List[Tensor] = []

    def reset(self) -> None:
        """Limpia el historial almacenado."""

        self._buffer.clear()

    def forward(self, activation: Tensor) -> Tensor:
        """Actualiza el buffer y devuelve la agregación configurada."""

        self._buffer.append(activation)
        if len(self._buffer) > self.length:
            self._buffer.pop(0)
        if self.reduction == "last":
            return self._buffer[-1]
        stacked = torch.stack(self._buffer, dim=0)
        if self.reduction == "sum":
            return stacked.sum(dim=0)
        return stacked.mean(dim=0)


class ConvLSTMCell(nn.Module):
    """Celda ConvLSTM ligera para mapas espaciales."""

    def __init__(
        self,
        input_channels: int,
        hidden_channels: int,
        kernel_size: int = 3,
        bias: bool = True,
    ) -> None:
        super().__init__()
        if kernel_size % 2 == 0:
            raise ValueError("kernel_size debe ser impar para mantener el centrado")
        padding = kernel_size // 2
        self.hidden_channels = hidden_channels
        self.conv = nn.Conv2d(
            input_channels + hidden_channels,
            4 * hidden_channels,
            kernel_size,
            padding=padding,
            bias=bias,
        )

    def init_state(self, input_tensor: Tensor) -> Tuple[Tensor, Tensor]:
        batch, _, height, width = input_tensor.shape
        device, dtype = input_tensor.device, input_tensor.dtype
        h = torch.zeros(batch, self.hidden_channels, height, width, device=device, dtype=dtype)
        c = torch.zeros(batch, self.hidden_channels, height, width, device=device, dtype=dtype)
        return h, c

    def forward(self, x: Tensor, state: Optional[Tuple[Tensor, Tensor]]) -> Tuple[Tensor, Tuple[Tensor, Tensor]]:
        if state is None:
            state = self.init_state(x)
        h_prev, c_prev = state
        combined = torch.cat([x, h_prev], dim=1)
        gates = self.conv(combined)
        i, f, o, g = torch.chunk(gates, chunks=4, dim=1)
        i = torch.sigmoid(i)
        f = torch.sigmoid(f)
        o = torch.sigmoid(o)
        g = torch.tanh(g)
        c = f * c_prev + i * g
        h = o * torch.tanh(c)
        return h, (h, c)


@dataclass
class TemporalINRFConfig:
    """Configuración de alto nivel para :class:`TemporalINRF`."""

    input_channels: int
    hidden_channels: Optional[int] = None
    integrator_decay: float = 0.8
    learnable_decay: bool = False
    recurrent_type: Optional[str] = None
    buffer_length: int = 0
    buffer_reduction: str = "mean"
    convlstm_kernel: int = 3


class TemporalINRF(nn.Module):
    """Bloque temporal inspirado en INRF que combina integración y recurrencia."""

    def __init__(self, config: TemporalINRFConfig) -> None:
        super().__init__()
        self.config = config
        hidden = config.hidden_channels or config.input_channels
        self.integrator = TemporalIntegrator(
            decay=config.integrator_decay,
            learnable_decay=config.learnable_decay,
        )
        self.recurrent_type = config.recurrent_type
        if self.recurrent_type is None:
            self.recurrent: Optional[nn.Module] = None
        elif self.recurrent_type.lower() == "conv_lstm":
            self.recurrent = ConvLSTMCell(
                config.input_channels,
                hidden,
                kernel_size=config.convlstm_kernel,
            )
        elif self.recurrent_type.lower() == "gru":
            self.recurrent = nn.GRUCell(config.input_channels, hidden)
            self._gru_pool = nn.AdaptiveAvgPool2d(1)
        else:
            raise ValueError("recurrent_type debe ser None, 'conv_lstm' o 'gru'")
        self.hidden_channels = hidden
        self.buffer = (
            ActivationBuffer(config.buffer_length, reduction=config.buffer_reduction)
            if config.buffer_length > 0
            else None
        )
        self._recurrent_state: Optional[Tuple[Tensor, Tensor]] = None
        self._gru_hidden: Optional[Tensor] = None

    def reset_state(self) -> None:
        """Restablece tanto la memoria integradora como la recurrente."""

        self.integrator.reset_state()
        self._recurrent_state = None
        self._gru_hidden = None
        if self.buffer is not None:
            self.buffer.reset()

    def _apply_recurrence(self, activation: Tensor) -> Tensor:
        if self.recurrent is None:
            return activation
        if isinstance(self.recurrent, ConvLSTMCell):
            output, state = self.recurrent(activation, self._recurrent_state)
            self._recurrent_state = state
            return output
        assert isinstance(self.recurrent, nn.GRUCell)
        pooled = self._gru_pool(activation).view(activation.size(0), -1)
        if self._gru_hidden is None or self._gru_hidden.shape[0] != activation.shape[0]:
            self._gru_hidden = torch.zeros(
                activation.size(0),
                self.hidden_channels,
                device=activation.device,
                dtype=activation.dtype,
            )
        self._gru_hidden = self.recurrent(pooled, self._gru_hidden)
        expanded = self._gru_hidden.unsqueeze(-1).unsqueeze(-1)
        return expanded.expand(-1, -1, activation.size(2), activation.size(3))

    def forward(self, sequence: Tensor, *, reset_state: bool = False) -> Tensor:
        """Procesa una secuencia temporal de estímulos."""

        if sequence.dim() == 4:
            sequence = sequence.unsqueeze(0)
        if sequence.dim() != 5:
            raise ValueError("La secuencia debe tener forma (T, B, C, H, W) o (B, C, H, W)")
        if reset_state:
            self.reset_state()
        outputs: List[Tensor] = []
        for frame in sequence:
            integrated = self.integrator(frame)
            recurrent = self._apply_recurrence(integrated)
            if self.buffer is not None:
                recurrent = self.buffer(recurrent)
            outputs.append(recurrent)
        return torch.stack(outputs, dim=0)


@torch.no_grad()
def evaluate_temporal_stability(
    module: TemporalINRF,
    sequence: Tensor,
    *,
    noise_std: float = 0.05,
) -> Dict[str, float]:
    """Evalúa estabilidad ante secuencias con ruido aditivo."""

    if noise_std < 0.0:
        raise ValueError("noise_std debe ser no negativo")
    clean_outputs = module(sequence, reset_state=True)
    diffs = clean_outputs[1:] - clean_outputs[:-1]
    temporal_consistency = float(diffs.pow(2).mean().sqrt().item()) if diffs.numel() else 0.0
    if noise_std == 0.0:
        noise_robustness = 0.0
    else:
        noisy_sequence = sequence + noise_std * torch.randn_like(sequence)
        noisy_outputs = module(noisy_sequence, reset_state=True)
        noise_robustness = float((clean_outputs - noisy_outputs).pow(2).mean().sqrt().item())
    module.reset_state()
    return {
        "temporal_consistency": temporal_consistency,
        "noise_robustness": noise_robustness,
    }

