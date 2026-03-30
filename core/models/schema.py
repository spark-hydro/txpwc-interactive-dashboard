from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd


@dataclass(frozen=True)
class AppContext:
    basin_id: str
    model_type: str
    scenario_id: str


@dataclass
class PerformanceBundle:
    context: AppContext
    basin_dir: Path
    observed_streamflow: pd.DataFrame
    simulated_streamflow: pd.DataFrame
    streamflow_joined: pd.DataFrame
    groundwater: pd.DataFrame
    stations: pd.DataFrame
    metrics: dict[str, float]
    subbasins_geojson: dict | None
    station_timeseries: pd.DataFrame
    stations_geojson: dict | None
    observed_data_filename: str | None
    channel_daily: pd.DataFrame
