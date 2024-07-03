import streamlit as st


st.set_page_config(
    page_title="DataSphere",
    page_icon="✨",
    layout="wide",
)

st.markdown("""
    <style>
    .header {
        font-size: 2em;
        font-weight: bold;
        color: #a87b05; /* Dourado */
        text-align: left;
        padding: 1em;
        background-color: #0000;
        margin: 0;
    }
    nav {
        background-color: #0000;
        color: white;
        padding: 1em;
        text-align: center;
    }
    nav ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }
    nav ul li {
        display: inline;
        margin-right: 1em;
    }
    nav ul li a {
        color: white;
        text-decoration: none;
        cursor: pointer;
    }
    .tab-content {
        padding: 2em 0;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<div class="header">DataSphere</div>', unsafe_allow_html=True)


tabs = ["Home", "Serviços", "Feedback", "Sobre Nós"]
selected_tab = st.radio("Navegação", tabs)


if selected_tab == "Home":
    st.write("# Bem-vindo ao DataSphere!")
    st.write("Este é um exemplo de site usando Streamlit com um cabeçalho dourado e navegação lateral.")
elif selected_tab == "Serviços":
    st.write("# Serviços")
    st.write("Detalhes sobre os serviços que oferecemos.")
elif selected_tab == "Feedback":
    st.write("# Feedback")
    st.write("Deixe seu feedback aqui.")
elif selected_tab == "Sobre Nós":
    st.write("# Sobre Nós")
    st.write("Informações sobre nossa empresa.")