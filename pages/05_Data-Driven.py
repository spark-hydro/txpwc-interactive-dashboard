import streamlit as st

from components.sidebar import render_sidebar

context = render_sidebar()

st.title("Scenarios")
st.markdown(
    """
    This page is reserved for future scenario analysis workflows such as:

    - baseline vs treated produced-water release
    - alternative discharge timing or rates
    - climate or drought sensitivity
    - uncertainty envelopes
    """
)

st.write(
    {
        "active_basin": context.basin_id,
        "active_model": context.model_type,
        "active_scenario": context.scenario_id,
    }
)
