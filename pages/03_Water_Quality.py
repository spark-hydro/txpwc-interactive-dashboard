import streamlit as st

from components.sidebar import render_sidebar

context = render_sidebar()

st.title("Water Quality")
st.markdown(
    """
    Planned content for this page:

    - salinity and constituent transport
    - produced-water quality indicators
    - concentration / load comparisons
    - spatial summaries by subbasin or receiving stream segment
    """
)

st.info(
    f"Water quality modules are not yet wired in for basin `{context.basin_id}` "
    f"and scenario `{context.scenario_id}`."
)
