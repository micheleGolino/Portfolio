import streamlit as st

def pagina():
    st.markdown("""
        <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            .stMarkdown {
                animation: fadeIn 2s;
            }
                
            h4:hover {
                color: #0078d4;
                transition: color 0.3s;
            }
                
        </style>
""", unsafe_allow_html=True)

    st.markdown("# Formazione")

    st.markdown("#### Università degli Studi eCampus")
    st.markdown("Laurea triennale, Ingegneria informatica e dell'automazione")
    st.markdown("Settembre 2022 - Gennaio 2024")
    st.markdown("""
        Ripresa degli Studi Interrotti:
        - Università: Università degli Studi eCampus
        - Percorso Accademico: Ho ripreso gli studi precedentemente interrotti, iniziati presso la Prima Università Degli Studi di Napoli - Federico II.
        - Cambio di Indirizzo: Ho effettuato una transizione dal corso di laurea in Informatica al corso di laurea in Ingegneria Informatica e dell'Automazione.
        - Competenze: Informatica · Ingegneria informatica
    """)

    st.markdown("---")

    st.markdown("#### Apple Developer Academy @Unina Federico II")
    st.markdown("Student at Apple Developer Academy @Unina Federico II")
    st.markdown("Ottobre 2017 - Giugno 2018")
    st.markdown("""
        L'Apple Developer Academy è una collaborazione tra l'Università di Napoli Federico II e Apple.
        La formazione presso l'Accademia è volta allo sviluppo di applicazioni per l'ecosistema di app più innovativo e vivace al mondo.
        Il programma si concentra sullo sviluppo software, sulla creazione di startup e sul design di app, con un particolare enfasi su creatività e collaborazione.
        - Competenze: Sviluppo iOS · Informatica · Scrum · iOS
    """)

    st.markdown("---")

    st.markdown("#### Università degli Studi di Napoli Federico II")
    st.markdown("Laurea breve in Scienze e Tecnologie Informatiche, Informatica")
    st.markdown("Settembre 2014 - Dicembre 2017")
    st.markdown("""
        Inizio del Percorso di Laurea Triennale in Informatica, Scienze MFN:
        - Università: Prima Università Degli Studi di Napoli - Federico II
        - Progresso: Completato il 75% degli esami previsti dal corso di laurea.
        - Note: Ho sospeso temporaneamente gli studi per partecipare all'Apple Developer Academy e intraprendere attività lavorative nel settore.
        - Competenze: SQL · Informatica · Unified Modeling Language · Sviluppo di software
    """)

    st.markdown("---")
    
    st.markdown("#### I.T.S.T. Galileo Ferraris Marcianise | I.S.I.S Istituto D'arte")
    st.markdown("Diploma di Perito Industriale Capotecnico: Informatica, Informatica")
    st.markdown("2008 - 2014")
    st.markdown("""
        - Votazione: 74/100
        - Diploma: Perito Industriale Capotecnico
        - Specializzazione: Informatica Abacus
        - Competenze: Informatica
    """)
