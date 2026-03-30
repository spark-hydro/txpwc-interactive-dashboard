from __future__ import annotations

import numpy as np
import pandas as pd

from core.metrics.mobj_adapter import evaluate_metrics


def compute_streamflow_metrics(joined_df: pd.DataFrame) -> dict[str, float]:
    if joined_df.empty:
        return {}

    required_cols = {"flow_obs", "flow_sim"}
    if not required_cols.issubset(joined_df.columns):
        return {}

    clean = joined_df.dropna(subset=["flow_obs", "flow_sim"])
    if clean.empty:
        return {}

    obs = clean["flow_obs"].to_numpy(dtype=float)
    sim = clean["flow_sim"].to_numpy(dtype=float)
    return evaluate_metrics(obs=obs, sim=sim)


def compute_basic_summary(joined_df: pd.DataFrame) -> pd.DataFrame:
    if joined_df.empty:
        return pd.DataFrame()

    summary = {
        "n_records": [len(joined_df)],
        "obs_mean": [joined_df["flow_obs"].mean() if "flow_obs" in joined_df.columns else np.nan],
        "sim_mean": [joined_df["flow_sim"].mean() if "flow_sim" in joined_df.columns else np.nan],
        "obs_peak": [joined_df["flow_obs"].max() if "flow_obs" in joined_df.columns else np.nan],
        "sim_peak": [joined_df["flow_sim"].max() if "flow_sim" in joined_df.columns else np.nan],
    }
    return pd.DataFrame(summary)
