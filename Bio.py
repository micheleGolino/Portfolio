import streamlit as st
import base64

def get_image_as_base64_string(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Obtain the image as a base64 string
profile_image_str = get_image_as_base64_string("resources/profile.jpg")
github_icon_str = get_image_as_base64_string("resources/github.png")
linkedin_icon_str = get_image_as_base64_string("resources/linkedin.png")
email_icon_str = get_image_as_base64_string("resources/email.png")

def page(language):
    translations = {
        'Italiano': {
            'arrowTitle': 'Scorri per la sezione contatti',
            'gitHubTitle': 'Visualizza i miei progetti su GitHub',
            'linkedinTitle': 'Consulta il mio profilo LinkedIn',
            'emailTitle': 'Contattami via mail',
            'contentTitle': "### Biografia",
            'contentBox': '''
👋 Ciao, sono Michele!

Sono un Software Engineer con 6 anni di esperienza nello sviluppo full-stack, con una particolare attenzione al backend. Mi dedico alla creazione di sistemi Java ad alte prestazioni e applicazioni web interattive in Python. La mia passione per l’innovazione e l’adozione delle migliori pratiche, come il Clean Code.

💻 Specializzazione in soluzioni Backend

Dopo aver iniziato come sviluppatore full-stack, ho scelto di focalizzarmi sulla progettazione di microservizi. Utilizzo principalmente Java con il framework Quarkus per costruire sistemi robusti, leggeri e facilmente aggiornabili. Per le interfacce web, mi affido a Python e Streamlit, trasformando dati complessi in dashboard intuitive e reattive.

🛠️ Tecnologie e Automazione

Credo nell’automazione intelligente e nella semplificazione dei processi lavorativi. Progetto soluzioni end-to-end integrando strumenti moderni, riducendo i tempi di sviluppo e migliorando l’esperienza utente. La mia esperienza include l’integrazione di sistemi di autenticazione sicuri utilizzando Keycloak e l’implementazione di applicazioni web interattive con Streamlit.

🏢 Esperienza Professionale

Ho gestito progetti B2B e B2C dall’ideazione alla manutenzione, collaborando con team multidisciplinari per garantire che ogni componente software sia allineato con gli obiettivi aziendali e facilmente gestibile nel tempo.

🎓 Formazione e Aggiornamento

Ho conseguito una laurea in Ingegneria Informatica e dell’Automazione, che mi ha fornito una solida base pratica. Inoltre, ho frequentato la Apple Developer Academy, collaborando con ingegneri esperti nello sviluppo di applicazioni iOS. Sono impegnato in un continuo aggiornamento professionale, esplorando nuove tecnologie e metodologie per migliorare le mie competenze e offrire soluzioni all’avanguardia.
''',
            'contentContacts': "### Contatti",
        },
        'English': {
            'arrowTitle': 'Scroll down for the contact section',
            'gitHubTitle': 'See my project on GitHub',
            'linkedinTitle': 'See my LinkedIn profile',
            'emailTitle': 'Send me a mail',
            'contentTitle': "### Biography",
            'contentBox': '''
👋 Hello, I’m Michele!

I am a Software Engineer with 6 years of experience in full-stack development, with a particular focus on backend solutions. I specialize in creating high-performance Java systems and interactive web applications using Python. My passion for innovation and adopting best practices, such as Clean Code, guides me in developing efficient and maintainable solutions. 

💻 Specialization in Backend Solutions

After starting as a full-stack developer, I chose to focus on microservices design. I primarily use Java with the Quarkus framework to build robust, lightweight, and easily upgradable systems. For web interfaces, I rely on Python and Streamlit, transforming complex data into intuitive and responsive dashboards.

🛠️ Technologies and Automation

I believe in intelligent automation and simplifying work processes. I design end-to-end solutions by integrating modern tools, reducing development time, and enhancing user experience. My experience includes integrating secure authentication systems using Keycloak and implementing interactive web applications with Streamlit.

🏢 Professional Experience

I have managed B2B and B2C projects from conception to maintenance, collaborating with multidisciplinary teams to ensure each software component aligns with business objectives and remains easily manageable over time.

🎓 Education and Training

I hold a degree in Computer Engineering and Automation, which has provided me with a solid practical foundation. Additionally, I attended the Apple Developer Academy, collaborating with experienced engineers in developing iOS applications. I am committed to continuous professional development, exploring new technologies and methodologies to enhance my skills and deliver cutting-edge solutions.
''',
            'contentContacts': "### Contacts",
        }
    }

    t = translations[language]

    short_description = t['contentBox'].split("\n")[1].strip()

    st.markdown(f'''
        <div style="max-width: 500px; margin: 0 auto 30px auto; background: var(--secondary-background-color); border-radius: 18px; box-shadow: 0 4px 24px rgba(0,0,0,0.10); padding: 32px 24px 24px 24px; text-align: center; position: relative; color: var(--text-color);">
            <img src="data:image/jpg;base64,{profile_image_str}" alt="Foto Profilo" style="border-radius: 50%; width: 120px; border: 4px solid #0a66c2; margin-bottom: 12px;">
            <h2 style="margin-bottom: 0; color: #0a66c2; font-size: 2rem;">Michele Golino</h2>
            <h4 style="margin-top: 4px; color: var(--text-color); opacity: 0.7; font-weight: 400;">Software Engineer | Full Stack Developer</h4>
            <p style="margin-top: 16px; font-size: 1.1rem; line-height: 1.5;">{short_description}</p>
            <div style="margin-top: 18px;">
                <a href="https://github.com/micheleGolino" title="{t['gitHubTitle']}" style="margin: 0 10px;"><img src="data:image/png;base64,{github_icon_str}" alt="GitHub" style="width: 32px;"></a>
                <a href="https://www.linkedin.com/in/michelegolino1994" title="{t['linkedinTitle']}" style="margin: 0 10px;"><img src="data:image/png;base64,{linkedin_icon_str}" alt="LinkedIn" style="width: 32px;"></a>
                <a href="mailto:michelegolino94@gmail.com" title="{t['emailTitle']}" style="margin: 0 10px;"><img src="data:image/png;base64,{email_icon_str}" alt="Email" style="width: 32px;"></a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown(t['contentTitle'])
    st.markdown(t['contentBox'])
