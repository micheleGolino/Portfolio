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

def pagina():

    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/jpg;base64,{profile_image_str}" alt="Foto Profilo" style="border-radius: 50%; width: 150px;">
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Biografia")

    st.markdown("""
        👋 Ciao, sono Michele! Sono un tech enthusiast con una passione per lo sviluppo software, l'innovazione e le nuove tecnologie.

        💻 Carriera Professionale: Ho messo piede nel settore dello sviluppo software 4 anni fa come sviluppatore Full Stack. Da quel momento, ho lavorato su una gamma diversificata di progetti B2B e B2C, con una predilezione per le soluzioni di backend.

        🛠️ Interessi Tecnologici: Sono particolarmente interessato allo sviluppo di microservizi e dall'automazione dei processi. Mi piace utilizzare tecnologie all'avanguardia ed innovative per rendere tutto più efficiente e scalabile.

        🏢 Ruolo Attuale: Sono attualmente un Software Engineer a tempo pieno, con responsabilità che vanno dalla progettazione alla manutenzione del software attraverso tutto il suo ciclo di vita.

        📖 Formazione in Corso: Sto per completare il mio percorso accademico in Ingegneria Informatica e dell'Automazione. Questa esperienza accademica mi ha fornito una solida base teorica, permettendomi di affinare ulteriormente le mie competenze pratiche e di rimanere aggiornato sulle ultime tendenze del settore.
    """)

    st.markdown("""
        <style>
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% {
                    transform: translateY(0);
                }
                40% {
                    transform: translateY(-30px);
                }
                60% {
                    transform: translateY(-15px);
                }
            }
            .arrow {
                text-align: center;
                animation: bounce 2s infinite;
                margin-top: 20px;
                margin-bottom: 20px;
                opacity: 0.6;
                visibility: visible;
            }
            @media (max-width: 768px) {
                .arrow {
                    display: none;
                }
            }
        </style>
        <div class="arrow" title="Scorri per la sezione Contatti">
            <i class="fas fa-arrow-down"></i>
        </div>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Contatti")
    
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
            <a href="https://github.com/micheleGolino" title="Visualizza i miei progetti su GitHub"><img src="data:image/png;base64,{github_icon_str}" alt="GitHub" style="width: 40px;"></a>
            <a href="https://www.linkedin.com/in/michelegolino1994" title="Consulta il mio profilo LinkedIn"><img src="data:image/png;base64,{linkedin_icon_str}" alt="LinkedIn" style="width: 40px;"></a>
            <a href="mailto:michelegolino94@gmail.com" title="Contattami via mail"><img src="data:image/png;base64,{email_icon_str}" alt="Email" style="width: 40px;"></a>
        </div>
""", unsafe_allow_html=True)


    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """, unsafe_allow_html=True)