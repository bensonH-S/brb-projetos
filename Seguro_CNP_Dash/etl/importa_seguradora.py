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

def importar_seguradora(df):
    try:
        # Remover espaços extras nos nomes das colunas
        df.columns = df.columns.str.strip()

        # Renomear colunas
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

        # Converter valores monetários
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

        # Lista para parcelas
        parcelas_to_insert = []

        # Processar débitos
        for idx, row in df.iterrows():
            for debito_idx in range(1, 6):
                col = f"debito{debito_idx}"
                value = str(row.get(col, '')).strip()

                if value.lower() == "nan" or not value or value == '-':
                    parcelas_to_insert.append({
                        "cnp": row["cnp"],
                        "numero_parcela": debito_idx,
                        "data_vencimento": None,
                        "status": "PENDENTE"
                    })
                    continue

                if value.upper() == "AGUARDANDO EMISSÃO DOS BOLETOS":
                    parcelas_to_insert.append({
                        "cnp": row["cnp"],
                        "numero_parcela": debito_idx,
                        "data_vencimento": None,
                        "status": "EMITIR"
                    })
                    continue

                if "BAIXADO" in value.upper() or "BAIXADA" in value.upper():
                    date_part = value.split()[0]
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

                if "PENDENTE" in value.upper():
                    date_part = value.split()[0]
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

                try:
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
                        parcelas_to_insert.append({
                            "cnp": row["cnp"],
                            "numero_parcela": debito_idx,
                            "data_vencimento": None,
                            "status": "PENDENTE"
                        })
                except Exception as e:
                    logging.warning(f"Erro ao processar data avulsa '{value}' para CNP {row['cnp']}: {e}")
                    parcelas_to_insert.append({
                        "cnp": row["cnp"],
                        "numero_parcela": debito_idx,
                        "data_vencimento": None,
                        "status": "PENDENTE"
                    })

        # Converter "B" para "boleto"
        df["forma_de_pgt"] = df["forma_de_pgt"].apply(lambda x: "boleto" if str(x).strip().upper() == "B" else x)

        # Converter apolice e multiseguros para string
        df["apolice"] = df["apolice"].astype(str).str.strip().replace("nan", None)
        df["multiseguros"] = df["multiseguros"].astype(str).str.strip().replace("nan", None)

        # Remover registros sem CNP
        df = df.dropna(subset=["cnp"])
        df["cnp"] = df["cnp"].astype(int)

        # Conectar ao banco
        DATABASE_URI = "mariadb+mariadbconnector://root:@localhost:3306/gecaf"
        engine = create_engine(DATABASE_URI)

        # Verificar CNPs válidos
        df_valid = pd.read_sql("SELECT cnp FROM cnp_data", engine)
        valid_cnps = set(df_valid["cnp"].unique())

        # Logar CNPs ausentes
        cnps_in_seg = set(df["cnp"].unique())
        missing_cnps = cnps_in_seg - valid_cnps
        if missing_cnps:
            logging.warning(f"CNPs não encontrados na tabela cnp_data: {', '.join(map(str, missing_cnps))}")

        # Filtrar CNPs válidos
        df = df[df["cnp"].isin(valid_cnps)]

        # Inserir na tabela seguradora (sem colunas debito1 a debito5)
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

                # Inserir parcelas
                for parcela in parcelas_to_insert:
                    if parcela["cnp"] != row["cnp"]:
                        continue
                    query_parcela = text("""
                        INSERT INTO pag_seguradora (
                            cnp, numero_parcela, data_vencimento, status
                        ) VALUES (
                            :cnp, :numero_parcela, :data_vencimento, :status
                        ) ON DUPLICATE KEY UPDATE
                            data_vencimento=VALUES(data_vencimento),
                            status=VALUES(status);
                    """)
                    conn.execute(query_parcela, {
                        "cnp": parcela["cnp"],
                        "numero_parcela": parcela["numero_parcela"],
                        "data_vencimento": parcela["data_vencimento"],
                        "status": parcela["status"]
                    })
                    logging.info(f"Parcela {parcela['numero_parcela']} inserida para CNP {row['cnp']}")

        logging.info("Importação concluída com sucesso!")
        return True, "✅ Importação finalizada com sucesso!"

    except Exception as e:
        logging.error(f"Erro na importação: {str(e)}")
        return False, f"Erro na importação: {str(e)}"