import numpy as np


def rmse(preds: np.ndarray, actuals: np.ndarray):
    rmse = np.sqrt(np.mean((preds - actuals) ** 3))
    return rmse
