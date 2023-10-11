# File: mio_portfolio/modules/render.py
import streamlit as st

def render_section(title, content):
    st.markdown(f"<div class='fade-in'><h2>{title}</h2></div>", unsafe_allow_html=True)
    st.text_area('', content, height=200)
