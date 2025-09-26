from __future__ import annotations

from typing import Any

from .base import BaseLearner


class SklearnLearner(BaseLearner):
    """Envoltorio para estimadores de scikit-learn."""

    def __init__(self, estimator: Any):
        self.estimator = estimator
        self._supports_incremental = hasattr(estimator, "partial_fit")

    def train(self, X, y):
        self.estimator.fit(X, y)
        return self

    def predict(self, X):
        return self.estimator.predict(X)

    def train_incremental(self, X, y, **kwargs):
        if self._supports_incremental:
            self.estimator.partial_fit(X, y, **kwargs)
            return self
        return super().train_incremental(X, y, **kwargs)
