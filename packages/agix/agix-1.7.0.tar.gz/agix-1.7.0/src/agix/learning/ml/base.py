from abc import ABC, abstractmethod


class BaseLearner(ABC):
    """Clase base para envoltorios de modelos de aprendizaje."""

    @abstractmethod
    def train(self, X, y):
        """Entrena el modelo con todos los datos."""

    @abstractmethod
    def predict(self, X):
        """Realiza predicciones dada una matriz de características."""

    def train_incremental(self, X, y, **kwargs):
        """Actualiza el modelo de forma incremental, si está soportado."""
        raise NotImplementedError(
            "Este modelo no soporta entrenamiento incremental."
        )
