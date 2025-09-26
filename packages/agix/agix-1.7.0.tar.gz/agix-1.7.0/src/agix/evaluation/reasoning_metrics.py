import numpy as np


def computational_cost(ops):
    """Return total computational cost from a list of operation costs."""
    if not ops:
        return 0.0
    return float(np.sum(ops))


