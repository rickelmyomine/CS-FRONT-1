import streamlit as st
from pipelines.conversor_sinais import obter_dados_telemetria

def render_dados():
    st.markdown("### 📊 Monitoramento de Sensores e Telemetria")

    # Verifica se existe algum equipamento cadastrado
    if not st.session_state.get('equipamentos'):
        st.info("Nenhum equipamento cadastrado. Vá até 'Cadastro Técnico' para adicionar um ativo primeiro.")
        return

    # Extrai as TAGs dos equipamentos para o selectbox
    tags_disponiveis = [eq['TAG'] for eq in st.session_state['equipamentos']]
    
    col_header1, col_header2 = st.columns([2, 1])
    with col_header1:
        ativo_selecionado = st.selectbox("Selecione o Ativo para Monitoramento", tags_disponiveis)
    with col_header2:
        st.markdown("<br>", unsafe_allow_html=True) # Espaçamento
        st.status("Conexão com Sensor: OK", state="complete")

    st.markdown("---")

    col_lateral, col_principal = st.columns([1, 3])

    # Área de Controle (Human-in-the-loop)
    with col_lateral:
        st.markdown("#### Parâmetros de Leitura")
        qtd_amostras = st.slider("Janela de Tempo (segundos)", min_value=10, max_value=100, value=30)
        
        if st.button("🔄 Iniciar Nova Coleta", use_container_width=True):
            with st.spinner("Lendo barramento de sensores..."):
                st.session_state['df_telemetria'] = obter_dados_telemetria(qtd_amostras)

    # Inicializa os dados na primeira vez que abre a tela
    if 'df_telemetria' not in st.session_state:
        st.session_state['df_telemetria'] = obter_dados_telemetria(30)

    df_atual = st.session_state['df_telemetria']

    # Área de Exibição
    with col_principal:
        tab_grafico, tab_tabela = st.tabs(["📈 Gráfico em Tempo Real", "🗄️ Tabela de Conversão (Bruto vs Real)"])
        
        with tab_grafico:
            st.markdown(f"**Comportamento do Motor: {ativo_selecionado}**")
            # Exibe um gráfico simples de linha do RPM
            st.line_chart(df_atual, x='Tempo (s)', y='RPM_Convertido', height=300)

        with tab_tabela:
            st.markdown("**Comparativo de Sinais**")
            # Mostra o DataFrame completo, destacando as colunas
            st.dataframe(
                df_atual, 
                use_container_width=True,
                hide_index=True
            )