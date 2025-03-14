import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import logging
from datetime import datetime
from tabulate import tabulate

# ------------------------------------------------------
# Configuração do log e do Streamlit
# ------------------------------------------------------
log_file_path = r"C:\logs\system_log.log"
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

    # Exibir registros existentes
    try:
        query = """
            SELECT 
                cnp, situacao, cnpj, razao_social, cc, telefone, telefone_proprietario,
                email, endereco, bairro, cidade, uf, cep, latitude, longitude, observacao
            FROM cnp_data
            ORDER BY cnp;
        """
        df_cnp = pd.read_sql(query, engine)
        st.subheader("Lista de CNPs")
        st.dataframe(df_cnp)
    except Exception as e:
        st.error(f"Erro ao consultar os CNPs: {e}")
        logging.error(f"Erro ao consultar os CNPs: {e}")

    st.subheader("Adicionar Novo CNP")

    with st.form("form_add_cnp", clear_on_submit=False):
        # 1ª linha: CNP, Telefone
        row1_col1, row1_col2 = st.columns(2)
        new_cnp = row1_col1.text_input("CNP", value="")
        new_telefone = row1_col2.text_input("Telefone", value="")

        # 2ª linha: Situação, CNPJ
        row2_col1, row2_col2 = st.columns(2)
        new_situacao = row2_col1.selectbox("Situação", [1, 0], index=0)
        new_cnpj = row2_col2.text_input("CNPJ", value="")

        # 3ª linha: Razão Social, CC
        row3_col1, row3_col2 = st.columns(2)
        new_razao = row3_col1.text_input("Razão Social", value="")
        new_cc = row3_col2.text_input("CC", value="")

        # 4ª linha: Telefone do Proprietário, Email
        row4_col1, row4_col2 = st.columns(2)
        new_telefone_proprietario = row4_col1.text_input("Telefone do Proprietário", value="")
        new_email = row4_col2.text_input("Email", value="")

        # 5ª linha: Endereço, Bairro
        row5_col1, row5_col2 = st.columns(2)
        new_endereco = row5_col1.text_input("Endereço", value="")
        new_bairro = row5_col2.text_input("Bairro", value="")

        # 6ª linha: Cidade, UF
        row6_col1, row6_col2 = st.columns(2)
        new_cidade = row6_col1.text_input("Cidade", value="")
        new_uf = row6_col2.text_input("UF", value="")

        # 7ª linha: CEP, Latitude
        row7_col1, row7_col2 = st.columns(2)
        new_cep = row7_col1.text_input("CEP", value="")
        new_latitude = row7_col2.text_input("Latitude", value="")

        # 8ª linha: Longitude, Observação
        row8_col1, row8_col2 = st.columns(2)
        new_longitude = row8_col1.text_input("Longitude", value="")
        new_observacao = row8_col2.text_input("Observação", value="")

        # 9ª linha: Botão à direita
        empty_col, button_col = st.columns([4,1])
        submitted = button_col.form_submit_button("Adicionar CNP")

    if submitted:
        # Verificação de campos obrigatórios
        if new_cnp.strip() == "" or new_cnpj.strip() == "" or new_razao.strip() == "":
            st.error("Preencha os campos obrigatórios: CNP, CNPJ e Razão Social.")
        else:
            try:
                query_insert = text("""
                    INSERT INTO cnp_data (
                        cnp, situacao, cnpj, razao_social, cc, telefone, telefone_proprietario,
                        email, endereco, bairro, cidade, uf, cep, latitude, longitude, observacao
                    )
                    VALUES (
                        :cnp, :situacao, :cnpj, :razao_social, :cc, :telefone, :telefone_proprietario,
                        :email, :endereco, :bairro, :cidade, :uf, :cep, :latitude, :longitude, :observacao
                    )
                """)
                with engine.begin() as conn:
                    conn.execute(query_insert, {
                        "cnp": int(new_cnp),
                        "situacao": int(new_situacao),
                        "cnpj": new_cnpj.strip(),
                        "razao_social": new_razao.strip(),
                        "cc": new_cc.strip(),
                        "telefone": new_telefone.strip(),
                        "telefone_proprietario": new_telefone_proprietario.strip(),
                        "email": new_email.strip(),
                        "endereco": new_endereco.strip(),
                        "bairro": new_bairro.strip(),
                        "cidade": new_cidade.strip(),
                        "uf": new_uf.strip(),
                        "cep": new_cep.strip(),
                        "latitude": float(new_latitude) if new_latitude.strip() != "" else None,
                        "longitude": float(new_longitude) if new_longitude.strip() != "" else None,
                        "observacao": new_observacao.strip()
                    })
                st.success("CNP adicionado com sucesso!")
                logging.info(f"CNP {new_cnp} adicionado com sucesso.")
                # Reinicializar a página para limpar os campos
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Erro ao adicionar CNP: {e}")
                logging.error(f"Erro ao adicionar CNP {new_cnp}: {e}")


elif menu == "Seguro":
    st.header("Informações de Seguros")
    st.write("Em breve, detalhes dos seguros...")

elif menu == "Relatório":
    st.header("Relatórios")
    st.write("Em breve, relatórios interativos...")

elif menu == "Executar ETL":
    st.header("Executar ETL")
    # File uploader para selecionar a planilha do ETL
    uploaded_file = st.file_uploader("Selecione a planilha para executar o ETL", type=["xlsx"])
    if uploaded_file is not None:
        st.write("Arquivo selecionado.")
        if st.button("Rodar ETL"):
            from etl.etl import rodar_etl  # Ajuste no script ETL para receber o arquivo
            try:
                resultado = rodar_etl(uploaded_file)
                st.success(resultado)
            except Exception as e:
                st.error(f"Erro na execução do ETL: {e}")
    else:
        st.info("Selecione uma planilha para executar o ETL.")
