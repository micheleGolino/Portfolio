# File: mio_portfolio/app.py
import streamlit as st
from pages import Esperienze as esperienze, Formazione as formazione, Skill as skill, Certificazioni as certificazioni
import base64

def get_image_as_base64_string(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Ottieni le immagini come stringhe base64
profile_image_str = get_image_as_base64_string("resources/profile.jpg")
github_icon_str = get_image_as_base64_string("resources/github.png")
linkedin_icon_str = get_image_as_base64_string("resources/linkedin.png")
email_icon_str = get_image_as_base64_string("resources/email.png")

PAGES = {
    "Esperienze": esperienze.show_esperienze,
    "Formazione": formazione.show_formazione,
    "Skill": skill.show_skill,
    "Certificazioni": certificazioni.show_certificazioni
}

def main():
    st.markdown("""
    <style>
        .title {
            display: flex;
            justify-content: center;
            height: 100px;
            padding-left: 2.3rem;
        }
    </style>
    <div class="title">
        <h1>Michele Golino</h1>
    </div>
""", unsafe_allow_html=True)

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

            📖 Formazione in Corso: Sto per completare il mio percorso accademico in Ingegneria Informatica e dell'Automazione. Questa esperienza accademica mi ha fornito una solida base teorica, permettendomi di affinare ulteriormente le mie competenze pratiche e di rimanere aggiornato sulle ultime tendenze del settore.""")
    
    st.markdown("---")

    st.markdown("### Contatti")

    st.markdown(f"""
    [![GitHub](data:image/png;base64,{github_icon_str})](https://github.com/micheleGolino)
    [![LinkedIn](data:image/png;base64,{linkedin_icon_str})](https://www.linkedin.com/in/michelegolino1994)
    [![Email](data:image/png;base64,{email_icon_str})](mailto:michelegolino94@gmail.com)
""", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
