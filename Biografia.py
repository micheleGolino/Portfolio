import streamlit as st
import Formazione, Certificazioni, Esperienze, Skill, Bio

PAGES = {
    'Biografia': Bio.pagina,
    'Formazione': Formazione.pagina,
    'Esperienze': Esperienze.pagina,
    'Certificazioni': Certificazioni.pagina,
    # 'Skill': Skill.pagina
}

LANGUAGES = {
    "Italiano": "resources/flags/italy_flag.png",
    "English": "resources/flags/uk_flag.png",
}

translations = {
    'Italiano': {
        'selectBoxLingua': 'Seleziona la lingua',
        'selectBoxPage': 'Vai a',
    },
    'English': {
        'selectBoxLingua': 'Select language',
        'selectBoxPage': 'Go to',
    },
}

def mostra_pagina_selezionata(selezione, lingua):
    pagina = PAGES.get(selezione)
    if pagina:
        pagina(lingua)

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

t = translations['Italiano']

lingua = st.selectbox("Lingua", LANGUAGES.keys(), label_visibility='hidden')

t = translations[lingua]

selezione = st.selectbox(t['selectBoxPage'], PAGES.keys(), 0)
if selezione:
    mostra_pagina_selezionata(selezione, lingua)