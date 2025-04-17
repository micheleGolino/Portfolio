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
                
            h4:hover {
                color: #0078d4;
                transition: color 0.3s;
            }
                
        </style>
    """, unsafe_allow_html=True)

    translations = {
        'Italiano': {
            'contentTitle': "# Licenze e Certificazioni",
        
            'contentTitleJava': "#### Academy Java",
            'contentSubtitleJava': "Forma Temp",
            'contentDateJava': "Data di rilascio: Agosto 2019",
            'contentIdJava': "ID credenziale: P037190970PTHS",

            'contentTitleCisco1': "#### Cisco Networking Academy",
            'contentSubtitleCisco1': "##### CCNA2 Routing and Switching: Routing and Switching Essentials",
            'contentDateCisco1': "Data di rilascio: Giugno 2018",
            
            'contentTitleCisco2': "#### Cisco Networking Academy",
            'contentSubtitleCisco2': "##### CCNA Routing and Switching: Introduction to Networks",
            'contentDateCisco2': "Data di rilascio: Maggio 2018",
        },
        'English': {
            'contentTitle': "# Licenses and Certifications",
        
            'contentTitleJava': "#### Academy Java",
            'contentSubtitleJava': "Forma Temp",
            'contentDateJava': "Issued: August 2019",
            'contentIdJava': "Credential ID: P037190970PTHS",

            'contentTitleCisco1': "#### Cisco Networking Academy",
            'contentSubtitleCisco1': "##### CCNA2 Routing and Switching: Routing and Switching Essentials",
            'contentDateCisco1': "Issued: June 2018",
            
            'contentTitleCisco2': "#### Cisco Networking Academy",
            'contentSubtitleCisco2': "##### CCNA Routing and Switching: Introduction to Networks",
            'contentDateCisco2': "Issued: May 2018",
        },
    }
    
    t = translations[language]

    st.markdown(t['contentTitle'])

    st.markdown(t['contentTitleJava'])
    st.markdown(t['contentSubtitleJava'])
    st.markdown(t['contentDateJava'])
    st.markdown(t['contentIdJava'])

    st.markdown("---")

    st.markdown(t['contentTitleCisco1'])
    st.markdown(t['contentSubtitleCisco1'])
    st.markdown(t['contentDateCisco1'])

    st.markdown("---")

    st.markdown(t['contentTitleCisco2'])
    st.markdown(t['contentSubtitleCisco2'])
    st.markdown(t['contentDateCisco2'])
