from __future__ import annotations

import math
import streamlit as st

from config.metrics_registry import METRIC_LABELS


def render_metric_cards(metrics: dict[str, float]) -> None:
    if not metrics:
        st.warning("No metrics are available for the selected context.")
        return

    metric_names = list(metrics.keys())
    columns = st.columns(len(metric_names))

    for col, name in zip(columns, metric_names):
        value = metrics[name]
        label = METRIC_LABELS.get(name, name.upper())
        if value is None or (isinstance(value, float) and math.isnan(value)):
            col.metric(label, "NA")
        else:
            col.metric(label, f"{value:.3f}")
