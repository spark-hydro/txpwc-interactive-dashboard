from __future__ import annotations

import numpy as np


def _nse(obs: np.ndarray, sim: np.ndarray) -> float:
    denominator = np.sum((obs - np.mean(obs)) ** 2)
    if denominator == 0:
        return np.nan
    return 1.0 - np.sum((sim - obs) ** 2) / denominator


def _rmse(obs: np.ndarray, sim: np.ndarray) -> float:
    return float(np.sqrt(np.mean((sim - obs) ** 2)))


def _pbias(obs: np.ndarray, sim: np.ndarray) -> float:
    denominator = np.sum(obs)
    if denominator == 0:
        return np.nan
    return float(100.0 * np.sum(sim - obs) / denominator)


def _kge(obs: np.ndarray, sim: np.ndarray) -> float:
    if len(obs) < 2:
        return np.nan

    r = np.corrcoef(obs, sim)[0, 1]
    alpha = np.std(sim, ddof=1) / np.std(obs, ddof=1) if np.std(obs, ddof=1) != 0 else np.nan
    beta = np.mean(sim) / np.mean(obs) if np.mean(obs) != 0 else np.nan
    if np.isnan(r) or np.isnan(alpha) or np.isnan(beta):
        return np.nan
    return float(1.0 - np.sqrt((r - 1.0) ** 2 + (alpha - 1.0) ** 2 + (beta - 1.0) ** 2))


def _r2(obs: np.ndarray, sim: np.ndarray) -> float:
    if len(obs) < 2:
        return np.nan

    r = np.corrcoef(obs, sim)[0, 1]
    if np.isnan(r):
        return np.nan

    return float(r ** 2)


def evaluate_metrics(obs: np.ndarray, sim: np.ndarray) -> dict[str, float]:
    """
    Temporary adapter.

    Replace this function body later with your real `mobjfns` import and metric calls.
    Keeping the same return shape allows the UI layer to stay unchanged.
    """
    return {
        "nse": _nse(obs, sim),
        "rmse": _rmse(obs, sim),
        "pbias": _pbias(obs, sim),
        "kge": _kge(obs, sim),
        "r2": _r2(obs, sim),
    }
