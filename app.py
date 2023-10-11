# File: mio_portfolio/app.py
import streamlit as st
from modules.content import get_content
from modules.render import render_section

SECTIONS = get_content()

def main():
    st.title('Il mio Portfolio')

    st.markdown("""
        <style>
            @keyframes fadeIn {
                0% {opacity: 0;}
                100% {opacity: 1;}
            }
            .fade-in {
                animation: fadeIn 2s;
            }
            body {
                color: white;
                background-color: #0d1117;
            }
        </style>
    """, unsafe_allow_html=True)

    for section, content in SECTIONS.items():
        render_section(section, content)

if __name__ == "__main__":
    main()
