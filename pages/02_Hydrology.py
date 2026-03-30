import streamlit as st

from components.sidebar import render_sidebar
from core.services.performance_service import load_performance_bundle

context = render_sidebar()
bundle = load_performance_bundle(context)

st.title("Hydrology")
st.markdown(
    """
    This page is a placeholder for future hydrology-specific views such as:

    - baseflow indicators
    - low-flow diagnostics
    - seasonal hydrograph comparisons
    - event windows
    - water budget summaries
    """
)

st.subheader("Available streamflow columns")
st.write(list(bundle.streamflow_joined.columns))
