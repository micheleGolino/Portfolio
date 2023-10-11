import streamlit as st
from modules.render import render_section

def show_certificazioni():
    content = "Inserisci qui le tue certificazioni..."
    render_section('Certificazioni', content)
