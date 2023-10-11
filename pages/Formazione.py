import streamlit as st
from modules.render import render_section

def show_formazione():
    content = "Inserisci qui la tua formazione..."
    render_section('Formazione', content)
