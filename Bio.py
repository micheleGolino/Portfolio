import streamlit as st
import base64

def get_image_as_base64_string(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Ottieni le immagini come stringhe base64
profile_image_str = get_image_as_base64_string("resources/profile.jpg")
github_icon_str = get_image_as_base64_string("resources/github.png")
linkedin_icon_str = get_image_as_base64_string("resources/linkedin.png")
email_icon_str = get_image_as_base64_string("resources/email.png")

def pagina(lingua):

    translations = {
        'Italiano': {
            'arrowTitle': 'Scorri per la sezione contatti',
            'gitHubTitle': 'Visualizza i miei progetti su GitHub',
            'linkedinTitle': 'Consulta il mio profilo LinkedIn',
            'emailTitle': 'Contattami via mail',
            'contentTitle': "### Biografia",
            'contentBox': """
            👋 Ciao, sono Michele! Sono un tech enthusiast con una passione per lo sviluppo software, l'innovazione e le nuove tecnologie.

            💻 Carriera Professionale: Ho messo piede nel settore dello sviluppo software 4 anni fa come sviluppatore Full Stack. Da quel momento, ho lavorato su una gamma diversificata di progetti B2B e B2C, con una predilezione per le soluzioni di backend.

            🛠️ Interessi Tecnologici: Sono particolarmente interessato allo sviluppo di microservizi e dall'automazione dei processi. Mi piace utilizzare tecnologie all'avanguardia ed innovative per rendere tutto più efficiente e scalabile.

            🏢 Ruolo Attuale: Sono attualmente un Software Engineer a tempo pieno, con responsabilità che vanno dalla progettazione alla manutenzione del software attraverso tutto il suo ciclo di vita.

            📖 Formazione in Corso: Sto per completare il mio percorso accademico in Ingegneria Informatica e dell'Automazione. Questa esperienza accademica mi ha fornito una solida base teorica, permettendomi di affinare ulteriormente le mie competenze pratiche e di rimanere aggiornato sulle ultime tendenze del settore.
        """,
            'contentContacts': "### Contatti",
        },
        'English': {
            'arrowTitle': 'Scroll down for the contact section',
            'gitHubTitle': 'See my project on GitHub',
            'linkedinTitle': 'See my LinkedIn profile',
            'emailTitle': 'Send me a mail',
            'contentTitle': "### Biography",
            'contentBox': """
            👋 Hello, I'm Michele! I'm a tech enthusiast with a passion for software development, innovation, and emerging technologies.

            💻 Professional Career: I stepped into the software development industry 4 years ago as a Full Stack Developer. Since then, I've worked on a diverse range of B2B and B2C projects, with a particular fondness for backend solutions.

            🛠️ Technological Interests: I have a keen interest in developing microservices and automating processes. I enjoy using cutting-edge and innovative technologies to make everything more efficient and scalable.

            🏢 Current Role: I'm currently employed as a full-time Software Engineer, with responsibilities ranging from design to maintenance throughout the entire software lifecycle.

            📖 Ongoing Education: I'm about to complete my academic journey in Computer Engineering and Automation. This educational experience has provided me with a solid theoretical foundation, allowing me to further refine my practical skills and stay updated on the latest industry trends.
            """,
            'contentContacts': "### Contacts",
        }
    }

    t = translations[lingua]

    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/jpg;base64,{profile_image_str}" alt="Foto Profilo" style="border-radius: 50%; width: 150px;">
        </div>
    """, unsafe_allow_html=True)

    st.markdown(t['contentTitle'])

    st.markdown(t['contentBox'])

    st.markdown(f"""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />

        <style>
            @keyframes bounce {{
                0%, 20%, 50%, 80%, 100% {{
                    transform: translateY(0);
                }}
                40% {{
                    transform: translateY(-30px);
                }}
                60% {{
                    transform: translateY(-15px);
                }}
            }}
            .arrow {{
                text-align: center;
                animation: bounce 2s infinite;
                margin-top: 20px;
                margin-bottom: 20px;
                opacity: 0.6;
                visibility: visible;
            }}
            @media (max-width: 768px) {{
                .arrow {{
                    display: none;
                }}
            }}
        </style>
        <div class="arrow" title="{t['arrowTitle']}">
            <i class="fas fa-arrow-down"></i>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(t['contentContacts'])
    
    st.write("""
        <style>
            .contact-icons a {
                display: inline-block;
                transition: transform 0.2s;
            }
            .contact-icons a:hover {
                transform: scale(1.5);
            }
        </style>
""", unsafe_allow_html=True)

    st.markdown(f"""
        <div class="contact-icons">
            <a href="https://github.com/micheleGolino" title="{t['gitHubTitle']}"><img src="data:image/png;base64,{github_icon_str}" alt="GitHub" style="width: 40px;"></a>
            <a href="https://www.linkedin.com/in/michelegolino1994" title="{t['linkedinTitle']}"><img src="data:image/png;base64,{linkedin_icon_str}" alt="LinkedIn" style="width: 40px;"></a>
            <a href="mailto:michelegolino94@gmail.com" title="{t['emailTitle']}"><img src="data:image/png;base64,{email_icon_str}" alt="Email" style="width: 40px;"></a>
        </div>
""", unsafe_allow_html=True)
    