import pandas as pd
from sqlalchemy import create_engine, text
import logging

# Configuração do log
log_file = r"C:\Users\u512228\Documents\seguradora_import.log"
logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    filemode="w",  # Sobrescreve a cada execução
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Caminho do arquivo Excel
excel_file = r"C:\Users\u512228\Documents\FOLLOW UP CNP 2025.xlsx"
sheet_name = "FOLLOW UP"

# Leitura do arquivo Excel
try:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    logging.info("Planilha carregada com sucesso.")
except Exception as e:
    logging.error(f"Erro ao carregar planilha: {e}")
    raise

# Remover espaços extras nos nomes das colunas
df.columns = df.columns.str.strip()

# Renomear colunas para corresponder à estrutura da tabela seguradora
rename_mapping = {
    "CNP": "cnp",
    "Início Vigência Seguro": "inicio_vigencia_seguro",
    "Vencimento": "vencimento",
    "Valor Cobertura": "valor_cobertura",
    "Valor Parcela": "valor_parcela",
    "1º débito": "debito1",
    "2º débito": "debito2",
    "3º débito": "debito3",
    "4º débito": "debito4",
    "5º débito": "debito5",
    "Forma de Pgt": "forma_de_pgt",
    "Situação Proposta": "situacao_proposta",
    "Obs": "obs",
    "APÓLICE": "apolice",
    "MULTISEGUROS": "multiseguros"
}
df = df.rename(columns=rename_mapping)

# Converter colunas de data
df["inicio_vigencia_seguro"] = pd.to_datetime(df["inicio_vigencia_seguro"], format="%d/%m/%Y", errors="coerce").dt.date
df["vencimento"] = pd.to_datetime(df["vencimento"], format="%d/%m/%Y", errors="coerce").dt.date

# Converter valores monetários corretamente
def convert_money(value):
    if isinstance(value, (int, float)):
        return float(value)
    if pd.isnull(value) or str(value).strip() == "":
        return None
    value = str(value).replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
    try:
        return float(value)
    except ValueError:
        return None

df["valor_cobertura"] = df["valor_cobertura"].apply(convert_money)
df["valor_parcela"] = df["valor_parcela"].apply(convert_money)

# Garantir que colunas de débito sejam strings
for col in ['debito1', 'debito2', 'debito3', 'debito4', 'debito5']:
    df[col] = df[col].astype(str).str.strip().replace("nan", None)

# Converter explicitamente "apolice" e "multiseguros" para string
df["apolice"] = df["apolice"].astype(str).str.strip().replace("nan", None)
df["multiseguros"] = df["multiseguros"].astype(str).str.strip().replace("nan", None)

# Remover registros sem CNP
df = df.dropna(subset=["cnp"])
df["cnp"] = df["cnp"].astype(int)

# Conectar ao banco de dados
DATABASE_URI = "mariadb+mariadbconnector://root:@localhost:3306/gecaf"
engine = create_engine(DATABASE_URI)

# Obter a lista de CNPs válidos na tabela cnp_data
df_valid = pd.read_sql("SELECT cnp FROM cnp_data", engine)
valid_cnps = set(df_valid["cnp"].unique())

# Identificar e logar CNPs que não existem na tabela cnp_data
cnps_in_seg = set(df["cnp"].unique())
missing_cnps = cnps_in_seg - valid_cnps
if missing_cnps:
    logging.warning(f"CNPs não cadastrados e não inseridos: {', '.join(map(str, missing_cnps))}")

# Filtrar registros apenas para CNPs válidos
df = df[df["cnp"].isin(valid_cnps)]

# Inserir os dados na tabela "seguradora"
with engine.begin() as conn:
    for _, row in df.iterrows():
        query_insert = text("""
            INSERT INTO seguradora (
                cnp, inicio_vigencia_seguro, vencimento, valor_cobertura, valor_parcela,
                debito1, debito2, debito3, debito4, debito5, forma_de_pgt,
                situacao_proposta, obs, apolice, multiseguros
            ) VALUES (
                :cnp, :inicio_vigencia_seguro, :vencimento, :valor_cobertura, :valor_parcela,
                :debito1, :debito2, :debito3, :debito4, :debito5, :forma_de_pgt,
                :situacao_proposta, :obs, :apolice, :multiseguros
            ) ON DUPLICATE KEY UPDATE 
                inicio_vigencia_seguro=VALUES(inicio_vigencia_seguro),
                vencimento=VALUES(vencimento),
                valor_cobertura=VALUES(valor_cobertura),
                valor_parcela=VALUES(valor_parcela),
                debito1=VALUES(debito1),
                debito2=VALUES(debito2),
                debito3=VALUES(debito3),
                debito4=VALUES(debito4),
                debito5=VALUES(debito5),
                forma_de_pgt=VALUES(forma_de_pgt),
                situacao_proposta=VALUES(situacao_proposta),
                obs=VALUES(obs),
                apolice=VALUES(apolice),
                multiseguros=VALUES(multiseguros);
        """)
        conn.execute(query_insert, {
            "cnp": row["cnp"],
            "inicio_vigencia_seguro": row["inicio_vigencia_seguro"],
            "vencimento": row["vencimento"],
            "valor_cobertura": row["valor_cobertura"],
            "valor_parcela": row["valor_parcela"],
            "debito1": row["debito1"],
            "debito2": row["debito2"],
            "debito3": row["debito3"],
            "debito4": row["debito4"],
            "debito5": row["debito5"],
            "forma_de_pgt": row["forma_de_pgt"],
            "situacao_proposta": row["situacao_proposta"],
            "obs": row["obs"],
            "apolice": row["apolice"],
            "multiseguros": row["multiseguros"]
        })

logging.info("Importação concluída com sucesso!")
print("✅ Importação finalizada com sucesso!")