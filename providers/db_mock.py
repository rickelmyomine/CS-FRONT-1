import streamlit as st

class EquipamentoRepository:
    """
    Classe responsável por simular a persistência de dados.
    No futuro, você só precisará alterar esta classe para conectar a um PostgreSQL, DynamoDB, etc.
    """
    
    @staticmethod
    def _iniciar_db():
        if 'equipamentos' not in st.session_state:
            st.session_state['equipamentos'] = []

    @classmethod
    def salvar(cls, equipamento_dict):
        cls._iniciar_db()
        st.session_state['equipamentos'].append(equipamento_dict)

    @classmethod
    def buscar_todos(cls):
        cls._iniciar_db()
        return st.session_state['equipamentos']

    @classmethod
    def tag_existe(cls, tag):
        cls._iniciar_db()
        return any(eq['TAG'] == tag for eq in st.session_state['equipamentos'])