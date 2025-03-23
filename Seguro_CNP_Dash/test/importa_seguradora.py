import pandas as pd
from sqlalchemy import create_engine, text
import logging
import os

# Configuração do log
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, "seguradora_import.log")
logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Caminho do arquivo Excel
excel_file = r"F:\Users\Administrador\OneDrive\Documentos\FOLLOW UP CNP 2025.xlsx"
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

# Lista para armazenar os dados das parcelas a serem inseridos em pag_seguradora
parcelas_to_insert = []

# Processar colunas de débito (1º débito a 5º débito)
for idx, row in df.iterrows():
    # Garantir que todas as 5 parcelas sejam criadas
    for debito_idx in range(1, 6):  # De 1 a 5
        col = f"debito{debito_idx}"
        value = str(row.get(col, '')).strip()

        if value.lower() == "nan" or not value or value == '-':
            # Se o valor for vazio, 'nan' ou '-', criar uma parcela com data_vencimento NULL
            parcelas_to_insert.append({
                "cnp": row["cnp"],
                "numero_parcela": debito_idx,
                "data_vencimento": None,
                "status": "PENDENTE"
            })
            continue

        # Converter "AGUARDANDO EMISSÃO DOS BOLETOS" para "EMITIR"
        if value.upper() == "AGUARDANDO EMISSÃO DOS BOLETOS":
            parcelas_to_insert.append({
                "cnp": row["cnp"],
                "numero_parcela": debito_idx,
                "data_vencimento": None,
                "status": "EMITIR"
            })
            continue

        # Tratar "16/01/2024 BAIXADO" ou "16/01/2024 BAIXADA"
        if "BAIXADO" in value.upper() or "BAIXADA" in value.upper():
            date_part = value.split()[0]  # Pegar a data (ex.: "16/01/2024")
            try:
                data_vencimento = pd.to_datetime(date_part, format="%d/%m/%Y").date()
                parcelas_to_insert.append({
                    "cnp": row["cnp"],
                    "numero_parcela": debito_idx,
                    "data_vencimento": data_vencimento,
                    "status": "PAGO"
                })
            except ValueError as e:
                logging.warning(f"Erro ao processar data BAIXADO/BAIXADA '{value}' para CNP {row['cnp']}: {e}")
            continue

        # Tratar "15/10/2024 PENDENTE"
        if "PENDENTE" in value.upper():
            date_part = value.split()[0]  # Pegar a data (ex.: "15/10/2024")
            try:
                data_vencimento = pd.to_datetime(date_part, format="%d/%m/%Y").date()
                parcelas_to_insert.append({
                    "cnp": row["cnp"],
                    "numero_parcela": debito_idx,
                    "data_vencimento": data_vencimento,
                    "status": "PENDENTE"
                })
            except ValueError as e:
                logging.warning(f"Erro ao processar data PENDENTE '{value}' para CNP {row['cnp']}: {e}")
            continue

        # Tratar datas avulsas (ex.: "15/03/2024" ou "3/15/2024")
        try:
            # Tentar parsing flexível de data
            data_vencimento = pd.to_datetime(value, dayfirst=True, errors='coerce')
            if pd.notnull(data_vencimento):
                parcelas_to_insert.append({
                    "cnp": row["cnp"],
                    "numero_parcela": debito_idx,
                    "data_vencimento": data_vencimento.date(),
                    "status": "PENDENTE"
                })
            else:
                logging.warning(f"Data inválida '{value}' para CNP {row['cnp']} na coluna {col}")
                # Se a data for inválida, criar uma parcela com data_vencimento NULL
                parcelas_to_insert.append({
                    "cnp": row["cnp"],
                    "numero_parcela": debito_idx,
                    "data_vencimento": None,
                    "status": "PENDENTE"
                })
        except Exception as e:
            logging.warning(f"Erro ao processar data avulsa '{value}' para CNP {row['cnp']}: {e}")
            # Se houver erro, criar uma parcela com data_vencimento NULL
            parcelas_to_insert.append({
                "cnp": row["cnp"],
                "numero_parcela": debito_idx,
                "data_vencimento": None,
                "status": "PENDENTE"
            })

# Converter "B" para "boleto" na coluna "forma_de_pgt"
df["forma_de_pgt"] = df["forma_de_pgt"].apply(lambda x: "boleto" if str(x).strip().upper() == "B" else x)

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
    logging.warning(f"CNPs não encontrados na tabela cnp_data e não inseridos na tabela seguradora: {', '.join(map(str, missing_cnps))}")

# Filtrar registros apenas para CNPs válidos
df = df[df["cnp"].isin(valid_cnps)]

# Inserir os dados na tabela "seguradora" (sem as colunas debito1 a debito5)
with engine.begin() as conn:
    for _, row in df.iterrows():
        query_insert = text("""
            INSERT INTO seguradora (
                cnp, inicio_vigencia_seguro, vencimento, valor_cobertura, valor_parcela,
                forma_de_pgt, situacao_proposta, obs, apolice, multiseguros
            ) VALUES (
                :cnp, :inicio_vigencia_seguro, :vencimento, :valor_cobertura, :valor_parcela,
                :forma_de_pgt, :situacao_proposta, :obs, :apolice, :multiseguros
            ) ON DUPLICATE KEY UPDATE 
                inicio_vigencia_seguro=VALUES(inicio_vigencia_seguro),
                vencimento=VALUES(vencimento),
                valor_cobertura=VALUES(valor_cobertura),
                valor_parcela=VALUES(valor_parcela),
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
            "forma_de_pgt": row["forma_de_pgt"],
            "situacao_proposta": row["situacao_proposta"],
            "obs": row["obs"],
            "apolice": row["apolice"],
            "multiseguros": row["multiseguros"]
        })

        # Obter o seguro_id (id da tabela seguradora) para o CNP
        seguro_id_query = text("SELECT id FROM seguradora WHERE cnp = :cnp")
        seguro_id = conn.execute(seguro_id_query, {"cnp": row["cnp"]}).scalar()
        logging.info(f"Seguro ID {seguro_id} obtido para CNP {row['cnp']}")

        # Inserir as parcelas na tabela pag_seguradora
        for parcela in parcelas_to_insert:
            if parcela["cnp"] != row["cnp"]:
                continue
            query_parcela = text("""
                INSERT INTO pag_seguradora (
                    seguro_id, numero_parcela, data_vencimento, status
                ) VALUES (
                    :seguro_id, :numero_parcela, :data_vencimento, :status
                ) ON DUPLICATE KEY UPDATE
                    data_vencimento=VALUES(data_vencimento),
                    status=VALUES(status);
            """)
            conn.execute(query_parcela, {
                "seguro_id": seguro_id,
                "numero_parcela": parcela["numero_parcela"],
                "data_vencimento": parcela["data_vencimento"],
                "status": parcela["status"]
            })
            logging.info(f"Parcela {parcela['numero_parcela']} inserida para seguro_id {seguro_id} (CNP {row['cnp']})")

logging.info("Importação concluída com sucesso!")
print("✅ Importação finalizada com sucesso!")