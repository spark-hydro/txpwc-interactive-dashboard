import streamlit as st

from components.sidebar import render_sidebar
from core.services.catalog import load_catalog


st.set_page_config(
    page_title="Model Info", # Default title
    page_icon="💧",
)



context = render_sidebar()
catalog = load_catalog()
basin_info = catalog["basins"][context.basin_id]

st.title("Model Info")
st.json(basin_info)
