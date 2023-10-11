import streamlit as st
from modules.render import render_section

def show_skill():
    content = "Inserisci qui le tue skill..."
    render_section('Skill', content)
