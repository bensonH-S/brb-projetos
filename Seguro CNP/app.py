import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import logging
from datetime import datetime
from tabulate import tabulate

# Importar a função do seu ETL
from etl.extraction import rodar_etl

# ------------------------------------------------------
# Configuração do log e do Streamlit
# ------------------------------------------------------
log_file_path = r"C:\Users\u512228\Documents\etl_log.log"
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

st.set_page_config(page_title="Sistema Seguro CNP", layout="wide")
st.title("Sistema Seguro CNP")

# ------------------------------------------------------
# Configuração do Banco de Dados (SQLAlchemy)
# ------------------------------------------------------
DATABASE_URI = "mariadb+mariadbconnector://root:@localhost:3306/gecaf"

# Criar engine (opcional criar função get_engine())
engine = create_engine(DATABASE_URI)

def exibir_dados_em_tabela(df: pd.DataFrame):
    """ Exibe o DataFrame em formato de tabela """
    df_formatado = df.copy()
    for col in ["Recolhimento", "Malote", "Media_Mes"]:
        if col in df_formatado.columns:
            df_formatado[col] = df_formatado[col].apply(lambda x: f"{x:,.2f}")
    st.write(df_formatado)  # ou st.dataframe(df_formatado)

# ------------------------------------------------------
# Menu Lateral
# ------------------------------------------------------
menu = st.sidebar.radio("Menu", ["Dashboard", "CNPs", "Seguro", "Relatório", "Executar ETL"])

if menu == "Dashboard":
    st.header("Dashboard - Visão Geral")
    st.write("Em breve, gráficos e indicadores...")

elif menu == "CNPs":
    st.header("Cadastro de CNPs")
    st.write("Em breve, listagem e edição de CNPs...")

elif menu == "Seguro":
    st.header("Informações de Seguros")
    st.write("Em breve, detalhes dos seguros...")

elif menu == "Relatório":
    st.header("Relatórios")
    st.write("Em breve, relatórios interativos...")

elif menu == "Executar ETL":
    st.header("Executar ETL")
    st.write("Clique no botão para rodar o ETL.")
    if st.button("Rodar ETL"):
        resultado = rodar_etl()  # Chama a função do ETL
        st.success(resultado)     # Exibe o retorno na tela
