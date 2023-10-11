import streamlit as st
from modules.render import render_section

def show_esperienze():
    content = "Inserisci qui le tue esperienze..."
    render_section('Esperienze', content)
