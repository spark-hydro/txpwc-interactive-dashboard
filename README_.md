# TxPWC Dashboard 💧

An interactive hydrologic modeling and data visualization platform for the Texas Produced Water Consortium (TxPWC).

## Overview

The TxPWC Dashboard supports integrated analysis of surface water and groundwater systems under produced water management scenarios.

It connects:
- watershed-scale hydrologic model outputs (e.g., SWAT+ gwflow)
- field monitoring data (streamflow, sediment, groundwater)
- spatial data (subbasins, stations)
- performance metrics (NSE, KGE, etc.)

## Research Vision

A comprehensive, integrated hydrologic modeling and decision-support system combining:
- physics-based models
- data-driven methods
- uncertainty analysis

## Key Features

- Subbasin-scale spatial visualization
- Station-based monitoring integration
- Observed vs simulated time series
- Multi-objective performance metrics
- Interactive map-to-data workflow

## Getting Started

```bash
git clone https://github.com/<your-username>/txpwc-dashboard.git
cd txpwc-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## Structure

- core/ → data & logic
- pages/ → Streamlit UI
- resources/ → demo data
- docs/ → documentation
- tools/ → preprocessing scripts

## Author

Seonggyu Park  
Texas Tech University
