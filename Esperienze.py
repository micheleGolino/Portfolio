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
                
            h2:hover {
                color: #0078d4;
                transition: color 0.3s;
            }
        </style>
""", unsafe_allow_html=True)

    st.markdown("# Esperienze")

    st.markdown("## AGM Solutions")
    st.markdown("### Software Engineer")
    st.markdown("Febbraio 2022 - Presente, Torino, Piemonte, Italia")

    st.markdown("""
        Software Engineer, Consulente presso Intesa Kyndryl:
        - Sviluppo Full-Stack: Progettazione e implementazione di soluzioni software B2C e strumenti interni, garantendo un'esperienza utente fluida e funzionalità back-end robuste.
        - Microservizi Java: Sviluppo di microservizi utilizzando Java e il framework Quarkus, ottimizzati per la scalabilità e le prestazioni.
        - Containerizzazione e Automazione: Utilizzo di Docker per la containerizzazione di applicazioni e Jenkins per l'automazione delle pipeline CI/CD.
        - Schedulazione di Task: Gestione e schedulazione di flussi di dati (DAG) attraverso Apache Airflow.
        - Sviluppo Python: Creazione di applicazioni web interattive utilizzando Python e il framework Streamlit.
    """)

    st.markdown("### Application Developer")
    st.markdown("Ottobre 2020 - Febbraio 2022, Torino, Piemonte, Italia")

    st.markdown("""
        Application Developer, Consulente presso Intesa IBM:

        **Aree di competenza**:
        - Sviluppo e Manutenzione di Applicativi B2B e B2C: Specializzato nel settore della fatturazione elettronica, con un focus su soluzioni robuste e scalabili.
        - Risoluzione di Bug: Esperienza nella diagnosi e correzione di errori per migliorare la qualità del software.

        **Tecnologie e Strumenti**:
        - Linguaggi di Programmazione: Java, AngularJS
        - Database: Oracle SQL
        - Styling: CSS
        - Ambiente di Sviluppo: Eclipse, WebSphere
        - Strumenti di Qualità del Codice: Sonarlint, Sonar
        - Sistemi di Versioning: Git, SVN
        - Server Web: Tomcat, JBoss
        - Framework e Librerie: JavaEE, SoapUI, Maven
        - API e Servizi Web: RESTful Services
        - Metodologie e Strumenti di Gestione: Agile, Jira
    """)
    st.markdown("---")

    st.markdown("## Dedagroup")
    st.markdown("### Junior Java Developer")
    st.markdown("Febbraio 2020 - Ottobre 2020 · 9 mesi, Torino, Italia")

    st.markdown("""
        Consulente Software presso RGI Group:

        **Aree di competenza**:
        - Sviluppo e Manutenzione di Applicativi B2B: Specializzato nel settore assicurativo, con un focus su soluzioni robuste e scalabili.

        **Tecnologie e Strumenti**:
        - Linguaggi di Programmazione: Java, AngularJS
        - Sistemi di Versioning: Git, SVN
        - Ambiente di Sviluppo: Eclipse
        - Server Web: Tomcat, JBoss
        - Framework e Librerie: JavaEE, SoapUI, Maven
        - API e Servizi Web: RESTful Services
        - Metodologie e Strumenti di Gestione: Agile, Jira, Sonar

        **Competenze**:
        - Java
        - Sviluppo di software
    """)
    st.markdown("---")
    
    st.markdown("## Randstad Technologies Italia")
    st.markdown("### Software Developer")
    st.markdown("Settembre 2019 - Febbraio 2020 · 6 mesi, Torino, Piemonte, Italia")

    st.markdown("""
        Attività di Junior Java Consultant presso Dedagroup Spa fino ad assunzione interna.

        **Competenze**:
        - Sviluppo di software
    """)

# Chiamare la funzione pagina per visualizzare il contenuto
pagina()
