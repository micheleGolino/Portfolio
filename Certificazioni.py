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

    st.markdown("# Licenze e Certificazioni")

    st.markdown("#### Academy Java")
    st.markdown("Forma Temp")
    st.markdown("Data di rilascio: Agosto 2019")
    st.markdown("ID credenziale: P037190970PTHS")
    st.markdown("- Competenze: Java · Java Enterprise Edition")
    st.markdown("---")

    st.markdown("#### Cisco Networking Academy")

    st.markdown("##### CCNA2 Routing and Switching: Routing and Switching Essentials")
    st.markdown("Data di rilascio: Giugno 2018")
    st.markdown("- Competenze: Tecnologie Cisco · Certificazione Cisco")
    st.markdown("---")

    st.markdown("#### Cisco Networking Academy")
    
    st.markdown("##### CCNA Routing and Switching: Introduction to Networks")
    st.markdown("Data di rilascio: Maggio 2018")
    st.markdown("- Competenze: Tecnologie Cisco · Certificazione Cisco")

# Chiamare la funzione pagina per visualizzare il contenuto
pagina()
