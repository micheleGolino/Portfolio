import streamlit as st
import Formazione, Certificazioni, Esperienze, Skill, Bio

PAGES = {
    'Biografia': Bio.pagina,
    'Formazione': Formazione.pagina,
    'Esperienze': Esperienze.pagina,
    'Certificazioni': Certificazioni.pagina,
    # 'Skill': Skill.pagina
}

def mostra_pagina_selezionata(selezione):
    pagina = PAGES.get(selezione)
    if pagina:
        pagina()

st.markdown("""
    <style>
        .title {
            display: flex;
            justify-content: center;
            height: 100px;
            padding-left: 2.3rem;
        }
        .contact-icons {
            display: flex;
            justify-content: space-evenly;
            margin-top: 1rem;
        }
        @media (max-width: 768px) {
            .title {
                padding-left: 0;
                justify-content: center;
            }
            .contact-icons {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
    <div class="title">
        <h1>Michele Golino</h1>
    </div>
    """, unsafe_allow_html=True)

selezione = st.selectbox("Vai a:", PAGES.keys(), 0)
if selezione:
    mostra_pagina_selezionata(selezione)