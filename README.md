# TxPWC Dashboard 💧

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-dashboard-red)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

An interactive hydrologic modeling and data visualization platform for the **Texas Produced Water Consortium (TxPWC)**.

---

## 🌊 Overview

The **TxPWC Dashboard** supports integrated analysis of surface water and groundwater systems under produced water management scenarios.

It brings together:

- watershed-scale hydrologic model outputs  
- field monitoring data for streamflow, sediment, and groundwater  
- spatial datasets such as subbasins and stations  
- objective-function-based model performance evaluation  

into a unified interactive platform for exploration, interpretation, and future decision support.

---

## 🎯 Research Vision

This dashboard is part of a broader effort to build a:

> **comprehensive, integrated hydrologic modeling and decision-support system**  
> that combines physics-based models, data-driven methods, and uncertainty analysis.

The long-term vision is to support:
- watershed-scale understanding of hydrologic responses  
- scenario evaluation for produced water management  
- interactive communication of model outputs across space and time  
- future coupling with machine learning and uncertainty workflows  

---

## ✨ Key Features

### 🗺️ Spatial Visualization
- Interactive subbasin polygon rendering using GeoJSON  
- Dynamic map coloring by hydrologic attributes such as elevation, area, and length  
- Basin-specific auto-centering and zooming  

### 📍 Monitoring Data Integration
- Point-based station metadata for streamflow, sediment, and groundwater  
- Station-scale observed and simulated time series  
- Clean separation between subbasin simulation layers and station monitoring layers  

### 📊 Time Series and Evaluation
- Observed vs simulated visualization  
- Support for custom multi-objective functions (`mobjfns`)  
- Extensible architecture for NSE, KGE, RMSE, PBIAS, and related metrics  

### 🔗 Interactive Workflow
- Shared basin/model/scenario context across pages  
- Map-driven analysis workflow  
- Clean path toward linking spatial selection to time-series diagnostics  

---

## 🧱 Architecture

The dashboard follows a modular structure:

- **IO layer** → reads CSV, GeoJSON, and future model outputs  
- **Service layer** → assembles data bundles for app pages  
- **Plotting layer** → reusable maps, hydrographs, and diagnostics  
- **UI layer** → Streamlit-based interactive pages  

```text
txpwc-dashboard/
├── app.py
├── components/
├── config/
├── core/
├── pages/
├── resources/
├── docs/
└── tools/
```

---

## 🖼️ Current Dashboard Design

```text
Subbasin polygons (simulation scale)
        +
Monitoring stations (point scale)
        +
Observed / simulated time series
        +
Objective function metrics
        =
Interactive hydrologic evaluation dashboard
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/txpwc-dashboard.git
cd txpwc-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Data Design

### Subbasin Scale
Used for:
- simulated hydrologic outputs  
- spatial summaries  
- future scenario visualization  

### Station Scale
Used for:
- observed monitoring data  
- matched simulated values  
- point-scale model performance evaluation  

This separation is intentional and reflects the different spatial meanings of polygons and monitoring locations.

---

## 🗺️ Spatial Data Workflow

```text
Shapefile (.shp)
   ↓
GeoJSON conversion (EPSG:4326)
   ↓
resources/txpwc/basins/<basin>/spatial/
   ↓
Interactive dashboard rendering
```

---

## 🔬 Future Development

- full SWAT+ gwflow integration  
- scenario comparison tools  
- uncertainty quantification workflows  
- machine learning integration  
- downloadable analysis products and reporting views  

---

## 🤝 Collaboration

This project is intended to support:
- interdisciplinary water research  
- transparent and reproducible workflows  
- communication of hydrologic insights to collaborators and stakeholders  

---

## 📄 License

MIT License

---

## 👨‍🔬 Author

**Seonggyu Park**  
Assistant Professor  
Civil, Environmental, & Construction Engineering  
Texas Tech University
