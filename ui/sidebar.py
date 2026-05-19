import streamlit as st
from providers.db_mock import LocalizacaoRepository # Importando o novo repositório

def render_sidebar():
    st.sidebar.title("Gestão de Ativos")
    st.sidebar.markdown("---")
    
    # --- NOVO BLOCO: Filtros de Localização ---
    st.sidebar.header("Filtro de Localização")
    
    # Busca os dados mockados
    estrutura_locais = LocalizacaoRepository.obter_plantas_e_areas()
    lista_plantas = list(estrutura_locais.keys())
    
    # Seletor de Planta
    planta = st.sidebar.selectbox("Selecione a Planta", lista_plantas)
    st.session_state['planta_selecionada'] = planta
    
    # Seletor de Área (Dinâmico conforme a planta)
    areas_disponiveis = estrutura_locais[planta]
    area = st.sidebar.selectbox("Selecione a Área", areas_disponiveis)
    st.session_state['area_selecionada'] = area
    
    st.sidebar.markdown("---")
    # ------------------------------------------

    # Menu de navegação (Seu código original)
    menu = st.sidebar.radio(
        "Navegação",
        ["Consulta de Equipamentos", "Cadastro Técnico", "Dados Brutos (Telemetria)"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("Sprint 2: Visualização Operacional") # Atualizado para a Sprint 2
    
    return menu