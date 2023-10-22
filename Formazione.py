import streamlit as st

def pagina(lingua):
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
    
    translations = {
        'Italiano': {
            'contentTitle': "# Formazione",

            'contentEcampus': "#### Università degli Studi eCampus",
            'contentSubtitleEcampus': "Laurea triennale, Ingegneria Informatica e dell'Automazione",
            'contentDataEcampus': "Settembre 2022 - Gennaio 2024",
            'contentBoxEcampus': """
            Ripresa degli Studi Interrotti:
            - Università: Università degli Studi eCampus
            - Percorso Accademico: Ho ripreso gli studi precedentemente interrotti, iniziati presso la Prima Università Degli Studi di Napoli - Federico II.
            - Cambio di Indirizzo: Ho effettuato una transizione dal corso di laurea in Informatica al corso di laurea in Ingegneria Informatica e dell'Automazione.
            - Competenze: Informatica · Ingegneria informatica
        """,

            'contentApple': "#### Apple Developer Academy @Unina Federico II",
            'contentSubtitleApple': "Studente a Apple Developer Academy @Unina Federico II",
            'contentDataApple': "Ottobre 2017 - Giugno 2018",
            'contentBoxApple': """
            L'Apple Developer Academy è una collaborazione tra l'Università di Napoli Federico II e Apple.
            La formazione presso l'Accademia è volta allo sviluppo di applicazioni per l'ecosistema di app più innovativo e vivace al mondo.
            Il programma si concentra sullo sviluppo software, sulla creazione di startup e sul design di app, con un particolare enfasi su creatività e collaborazione.
            - Competenze: Sviluppo iOS · Informatica · Scrum · iOS
        """,

            'contentFederico': "#### Prima Università degli Studi di Napoli Federico II",
            'contentSubtitleFederico': "Laurea breve in Scienze e Tecnologie Informatiche, Informatica",
            'contentDataFederico': "Settembre 2014 - Dicembre 2017",
            'contentBoxFederico': """
                Inizio del Percorso di Laurea Triennale in Informatica, Scienze MFN:
                - Università: Prima Università Degli Studi di Napoli - Federico II
                - Progresso: Completato il 75% degli esami previsti dal corso di laurea.
                - Note: Ho sospeso temporaneamente gli studi per partecipare all'Apple Developer Academy e intraprendere attività lavorative nel settore.
                - Competenze: SQL · Informatica · Unified Modeling Language · Sviluppo di software
            """,

            'contentFerraris': "#### I.T.S.T. Galileo Ferraris Marcianise | I.S.I.S Istituto D'arte",
            'contentSubtitleFerraris': "Diploma di Perito Industriale Capotecnico: Informatica, Informatica",
            'contentDataFerraris': "2008 - 2014",
            'contentBoxFerraris': """
                - Votazione: 74/100
                - Diploma: Perito Industriale Capotecnico
                - Specializzazione: Informatica Abacus
                - Competenze: Informatica
            """,
        },
        'English': {
            'contentTitle': "# Formazione",

            'contentEcampus': "#### Università degli Studi eCampus",
            'contentSubtitleEcampus': "Bachelor's degree, Computer and automation Engineering",
            'contentDataEcampus': "September 2022 - January 2024",
            'contentBoxEcampus': """Resumption of Interrupted Academic Studies:
                University: eCampus University
                Academic Path: Resumed previously interrupted studies, initially started at the First University of Naples - Federico II.
                Change of Major: Transitioned from a degree program in Computer Science to a degree program in Computer Engineering and Automation.""",

            'contentApple': "#### Apple Developer Academy @Unina Federico II",
            'contentSubtitleApple': "Student at Apple Developer Academy @Unina Federico II",
            'contentDataApple': "October 2017 - June 2018",
            'contentBoxApple': """ The Apple Developer
                Academy is a partnership between the University of Napoli Federico II and Apple.
                Training at the Academy is aimed at developing apps for the world’s most
                innovative and vibrant app ecosystem. The program focuses on software
                development, startup creation and app design with an emphasis on creativity and
                collaboration.
            """,

            'contentFederico': "#### Prima Università degli Studi di Napoli Federico II",
            'contentSubtitleFederico': "Bachelor's Degree in computer science, Computer Science",
            'contentDataFederico': "September 2014 - December 2017",
            'contentBoxFederico': """
                University: First University of Naples - Federico II
                Progress: Completed 75% of the required exams for the degree program.
                Note: Temporarily suspended studies to participate in the Apple Developer Academy and to engage in professional activities in the field.
            """,

            'contentFerraris': "#### I.T.S.T. Galileo Ferraris Marcianise | I.S.I.S Istituto D'arte",
            'contentSubtitleFerraris': "Industrial Technical Expert: Computer Science, Computer Science",
            'contentDataFerraris': "2008 - 2014",
            'contentBoxFerraris': """
                Vote: 74/100
                Degree: Industrial Technical Expert
                Specialization: Computer Science Abacus
            """,
        },
    }

    t = translations[lingua]

    st.markdown(t['contentTitle'])

    st.markdown(t['contentEcampus'])
    st.markdown(t['contentSubtitleEcampus'])
    st.markdown(t['contentDataEcampus'])
    st.markdown(t['contentBoxEcampus'])

    st.markdown("---")

    st.markdown(t['contentApple'])
    st.markdown(t['contentSubtitleApple'])
    st.markdown(t['contentDataApple'])
    st.markdown(t['contentBoxApple'])

    st.markdown("---")

    st.markdown(t['contentFederico'])
    st.markdown(t['contentSubtitleFederico'])
    st.markdown(t['contentDataFederico'])
    st.markdown(t['contentBoxFederico'])

    st.markdown("---")
    
    st.markdown(t['contentFerraris'])
    st.markdown(t['contentSubtitleFerraris'])
    st.markdown(t['contentDataFerraris'])
    st.markdown(t['contentBoxFerraris'])
