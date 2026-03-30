from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.graph_objects as go


def _fdc_values(series: pd.Series) -> tuple[np.ndarray, np.ndarray]:
    clean = series.dropna().sort_values(ascending=False).to_numpy(dtype=float)
    if len(clean) == 0:
        return np.array([]), np.array([])
    exceedance = np.arange(1, len(clean) + 1) / (len(clean) + 1) * 100.0
    return exceedance, clean


def plot_fdc(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()

    if "flow_obs" in df.columns:
        x, y = _fdc_values(df["flow_obs"])
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Observed"))
    if "flow_sim" in df.columns:
        x, y = _fdc_values(df["flow_sim"])
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Simulated"))

    fig.update_layout(
        title="Flow Duration Curve",
        xaxis_title="Exceedance Probability (%)",
        yaxis_title="Flow",
        template="plotly_white",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    fig.update_yaxes(type="log")
    return fig
