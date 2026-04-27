import streamlit as st

def render_sidebar():
    st.sidebar.title("Gestão de Ativos")
    st.sidebar.markdown("---")
    
    # Menu de navegação
    menu = st.sidebar.radio(
        "Navegação",
        ["Consulta de Equipamentos", "Cadastro Técnico", "Dados Brutos (Telemetria)"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("Sprint 1: Fundamentos do Ativo")
    
    return menu