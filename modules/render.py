# File: mio_portfolio/modules/render.py
import streamlit as st

def render_section(section, content):
    if st.button(f"Mostra {section}"):
        st.markdown(f"<div class='fade-in'>{section}</div>", unsafe_allow_html=True)
        st.text_area('', content, height=200)