import streamlit as st
import Bio, Educations, Experiences, Certifications, Skills

PAGES = {
    'Biografia': Bio.page,
    'Formazione': Educations.page,
    'Esperienze': Experiences.page,
    'Certificazioni': Certifications.page,
    # 'Skill': Skills.page
}

PAGES_ITALIANO = ['Biografia', 'Formazione', 'Esperienze', 'Certificazioni']
PAGES_ENGLISH = ['Biography', 'Educations', 'Experiences', 'Certifications']

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

def show_selected_page(selection, language):
    selection_translated = translate_selection(selection, language)

    page = PAGES.get(selection_translated)
    if page:
        page(language)

def translate_selection(selection: str, language: str) -> str:
    if language != 'Italiano':
        if selection == 'Biography':
            return 'Biografia'
        elif selection == 'Educations':
            return 'Formazione'
        elif selection == 'Experiences':
            return 'Esperienze'
        elif selection == 'Certifications':
            return 'Certificazioni'
    else:
        return selection

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

language = st.selectbox("Lingua", LANGUAGES.keys(), label_visibility='hidden')

t = translations[language]
opt_page_selections = PAGES_ITALIANO if language == 'Italiano' else PAGES_ENGLISH
selection = st.selectbox(t['selectBoxPage'], opt_page_selections, 0)
if selection:
    show_selected_page(selection, language)