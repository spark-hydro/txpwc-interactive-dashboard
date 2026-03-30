from __future__ import annotations

import plotly.graph_objects as go
import pandas as pd


def plot_streamflow_hydrograph(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()

    if "flow_obs" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df["date"],
                y=df["flow_obs"],
                mode="lines",
                name="Observed",
            )
        )
    if "flow_sim" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df["date"],
                y=df["flow_sim"],
                mode="lines",
                name="Simulated",
            )
        )

    fig.update_layout(
        title="Observed vs Simulated Streamflow",
        xaxis_title="Date",
        yaxis_title="Flow",
        template="plotly_white",
        legend_title="Series",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    return fig
