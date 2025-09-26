# agi_lab/learning/plasticity.py

import numpy as np

class HebbianPlasticity:
    """
    Implementación básica de regla de aprendizaje hebbiana.
    Δw_ij = η * pre_j * post_i
    """

    def __init__(self, input_size, output_size, learning_rate=0.01):
        self.weights = np.random.uniform(-1, 1, (output_size, input_size))
        self.learning_rate = learning_rate

    def forward(self, x):
        return np.dot(self.weights, x)

    def update(self, pre, post):
        delta_w = self.learning_rate * np.outer(post, pre)
        self.weights += delta_w


class STDPPlasticity:
    """
    Implementación simplificada de Spike-Timing Dependent Plasticity (STDP).
    Se asume codificación temporal abstracta.
    """

    def __init__(self, input_size, output_size, a_plus=0.01, a_minus=0.012):
        self.weights = np.random.uniform(-0.5, 0.5, (output_size, input_size))
        self.a_plus = a_plus
        self.a_minus = a_minus
        self.pre_trace = np.zeros(input_size)
        self.post_trace = np.zeros(output_size)

    def forward(self, x):
        return np.dot(self.weights, x)

    def update(self, x, y):
        self.pre_trace = 0.9 * self.pre_trace + x
        self.post_trace = 0.9 * self.post_trace + y

        for i in range(len(y)):
            for j in range(len(x)):
                if self.pre_trace[j] > 0 and self.post_trace[i] > 0:
                    self.weights[i, j] += self.a_plus * self.pre_trace[j] * self.post_trace[i]
                elif self.pre_trace[j] > 0 and self.post_trace[i] == 0:
                    self.weights[i, j] -= self.a_minus * self.pre_trace[j]


class BCMPlasticity:
    """
    Regla BCM (Bienenstock–Cooper–Munro): plasticidad dependiente del umbral de actividad.
    """

    def __init__(self, input_size, output_size, eta=0.01, theta=0.1):
        self.weights = np.random.normal(0, 0.1, (output_size, input_size))
        self.eta = eta
        self.theta = theta  # Umbral de plasticidad

    def forward(self, x):
        return np.dot(self.weights, x)

    def update(self, x, y):
        for i in range(len(y)):
            for j in range(len(x)):
                delta = y[i] * (y[i] - self.theta) * x[j]
                self.weights[i, j] += self.eta * delta