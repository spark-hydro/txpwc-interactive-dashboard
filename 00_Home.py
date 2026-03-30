import streamlit as st

from components.sidebar import render_sidebar
from config.settings import CONTENT_DIR
from core.io.filesystem import safe_markdown_read

context = render_sidebar()

st.title("Home")
st.markdown(safe_markdown_read(CONTENT_DIR / "home.md"))

st.subheader("Current selection")
st.write(
    {
        "basin_id": context.basin_id,
        "model_type": context.model_type,
        "scenario_id": context.scenario_id,
    }
)
