import streamlit as st

def page(language):
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

    translations = {
        'Italiano': {
            'contentTitle': "# Esperienze",
            'contentTitleAgm': "## AGM Solutions",
            'contentSubtitleAgm1': "### Software Engineer",
            'contentDateAgm1': "Febbraio 2022 - Presente, Torino, Piemonte, Italia",
            'contentBoxAgm1': """
                Software Engineer, Consulente presso Intesa Kyndryl:
                - Sviluppo Full-Stack: Progettazione e implementazione di soluzioni software B2C e strumenti interni, garantendo un'esperienza utente fluida e funzionalità back-end robuste.
                - Microservizi Java: Sviluppo di microservizi utilizzando Java e il framework Quarkus, ottimizzati per la scalabilità e le prestazioni.
                - Containerizzazione e Automazione: Utilizzo di Docker per la containerizzazione di applicazioni e Jenkins per l'automazione delle pipeline CI/CD.
                - Schedulazione di Task: Gestione e schedulazione di flussi di dati (DAG) attraverso Apache Airflow.
                - Sviluppo Python: Creazione di applicazioni web interattive utilizzando Python e il framework Streamlit.
            """,
            'contentSubtitleAgm2': "### Application Developer",
            'contentDateAgm2': "Ottobre 2020 - Febbraio 2022, Torino, Piemonte, Italia",
            'contentBoxAgm2': """
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
            """,
            'contentSubtitleAgm2': "### Application Developer",
            'contentDateAgm2': "Ottobre 2020 - Febbraio 2022, Torino, Piemonte, Italia",
            'contentBoxAgm2' : """
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
            """,

            'contentTitleDedagroup' : "## Dedagroup",
            'contentSubtitleDedagroup': "### Junior Java Developer",
            'contentDateDedagroup': "Febbraio 2020 - Ottobre 2020 · 9 mesi, Torino, Italia",
            'contentBoxDedagroup': """
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
            """,

            'contentTitleRandstad': "## Randstad Technologies Italia",
            'contentSubtitleRandstad': "### Software Developer",
            'contentDateRandstad': "Settembre 2019 - Febbraio 2020 · 6 mesi, Torino, Piemonte, Italia",
            'contentBoxRandstad': """
                Attività di Junior Java Consultant presso Dedagroup Spa fino ad assunzione interna.
                **Competenze**:
                - Sviluppo di software
            """,
        },
        'English': {
            'contentTitle': "# Experiences",
            'contentTitleAgm': "## AGM Solutions",
            'contentSubtitleAgm1': "### Software Engineer",
            'contentDateAgm1': "February 2022 - Present, Turin, Piedmont, Italy",
            'contentBoxAgm1': """
                Software Engineer, Consultant at Intesa Kyndryl:
                - Full-Stack Development: Design and implementation of B2C software solutions and internal tools, ensuring a smooth user experience and robust back-end functionality.
                - Java Microservices: Development of microservices using Java and the Quarkus framework, optimized for scalability and performance.
                - Containerization and Automation: Use of Docker for application containerization and Jenkins for CI/CD pipeline automation.
                - Task Scheduling: Management and scheduling of data flows (DAG) through Apache Airflow.
                - Python Development: Creation of interactive web applications using Python and the Streamlit framework.
            """,
            'contentSubtitleAgm2': "### Application Developer",
            'contentDateAgm2': "October 2020 - February 2022, Turin, Piedmont, Italy",
            'contentBoxAgm2': """
                Application Developer, Consultant at Intesa IBM:
                **Areas of Expertise**:
                - Development and Maintenance of B2B and B2C Applications: Specialized in the electronic invoicing sector, with a focus on robust and scalable solutions.
                - Bug Resolution: Experience in diagnosing and correcting errors to improve software quality.
                **Technologies and Tools**:
                - Programming Languages: Java, AngularJS
                - Database: Oracle SQL
                - Styling: CSS
                - Development Environment: Eclipse, WebSphere
                - Code Quality Tools: Sonarlint, Sonar
                - Versioning Systems: Git, SVN
                - Web Servers: Tomcat, JBoss
                - Frameworks and Libraries: JavaEE, SoapUI, Maven
                - APIs and Web Services: RESTful Services
                - Management Methodologies and Tools: Agile, Jira
            """,
            'contentTitleDedagroup': "## Dedagroup",
            'contentSubtitleDedagroup': "### Junior Java Developer",
            'contentDateDedagroup': "February 2020 - October 2020 · 9 months, Turin, Italy",
            'contentBoxDedagroup': """
                Software Consultant at RGI Group:
                **Areas of Expertise**:
                - Development and Maintenance of B2B Applications: Specialized in the insurance sector, with a focus on robust and scalable solutions.
                **Technologies and Tools**:
                - Programming Languages: Java, AngularJS
                - Versioning Systems: Git, SVN
                - Development Environment: Eclipse
                - Web Servers: Tomcat, JBoss
                - Frameworks and Libraries: JavaEE, SoapUI, Maven
                - APIs and Web Services: RESTful Services
                - Management Methodologies and Tools: Agile, Jira, Sonar
                **Skills**:
                - Java
                - Software development
            """,

            'contentTitleRandstad': "## Randstad Technologies Italia",
            'contentSubtitleRandstad': "### Software Developer",
            'contentDateRandstad': "September 2019 - February 2020 · 6 months, Turin, Piedmont, Italy",
            'contentBoxRandstad': """
                Activities as Junior Java Consultant at Dedagroup Spa until internal hiring.
                **Skills**:
                - Software development
            """,
        }
    }

    t = translations[language]

    st.markdown(t['contentTitle'])

    st.markdown(t['contentTitleAgm'])
    st.markdown(t['contentSubtitleAgm1'])
    st.markdown(t['contentDateAgm1'])
    st.markdown(t['contentBoxAgm1'])
    st.markdown(t['contentSubtitleAgm2'])
    st.markdown(t['contentDateAgm2'])
    st.markdown(t['contentBoxAgm2'])
    st.markdown("---")

    st.markdown(t['contentTitleDedagroup'])
    st.markdown(t['contentSubtitleDedagroup'])
    st.markdown(t['contentDateDedagroup'])
    st.markdown(t['contentBoxDedagroup'])
    st.markdown("---")

    st.markdown(t['contentTitleRandstad'])
    st.markdown(t['contentSubtitleRandstad'])
    st.markdown(t['contentDateRandstad'])
    st.markdown(t['contentBoxRandstad'])
