import pandas as pd
from sqlalchemy import create_engine, text
import logging
from datetime import datetime, timedelta
from tabulate import tabulate

def rodar_etl(uploaded_file):
    """
    Executa o processo de ETL usando o arquivo Excel enviado.
    Retorna uma mensagem de sucesso ao final.
    """
    # Configuração do log
    log_file_path = r"C:\logs\etl_log.log"
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Iniciando o processo de ETL...")

    # Conexão com o banco de dados
    DATABASE_URI = "mariadb+mariadbconnector://root:@localhost:3306/gecaf"
    engine = create_engine(DATABASE_URI)

    # Leitura da planilha usando o arquivo enviado
    try:
        df_005 = pd.read_excel(uploaded_file, sheet_name="005")
        df_107 = pd.read_excel(uploaded_file, sheet_name="107")
        logging.info("Planilha carregada com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao carregar planilha: {e}")
        raise

    # Remover espaços extras dos nomes das colunas
    df_005.columns = df_005.columns.str.strip()
    df_107.columns = df_107.columns.str.strip()

    # Determinar a coluna do banco de dados com base na data do primeiro registro da aba 005
    try:
        primeira_data = pd.to_datetime(df_005["logDatMov"].dropna().iloc[0], dayfirst=True)  # Define que o primeiro valor é o dia
        mes_map = {
            "01": "jan", "02": "fev", "03": "mar", "04": "abr",
            "05": "mai", "06": "jun", "07": "jul", "08": "ago",
            "09": "set", "10": "out", "11": "nov", "12": "dez"
        }
        
        mes_abbr = primeira_data.strftime("%m")  # Obtém o mês como número (ex: "01" para janeiro)
        ano_abbr = primeira_data.strftime("%y")    # Obtém o ano abreviado (ex: "25" para 2025)
        
        coluna_mes_atual = f"{mes_map[mes_abbr]}_{ano_abbr}"
        logging.info(f"Coluna do mês determinada a partir da planilha: {coluna_mes_atual}")
    except Exception as e:
        logging.error(f"Erro ao determinar a coluna do mês: {e}")
        raise ValueError("Não foi possível determinar a coluna do mês.")

    # Cálculo do Recolhimento (005)
    df_recolhimento = df_005.groupby("ptaCod", as_index=False).apply(
        lambda g: pd.Series({
            "Recolhimento": (
                g.loc[(g["ctrCod"] == 25400) & (g["logTrnSta"] != "E"), "logValLan014"].sum()
                - g.loc[(g["ctrCod"] == 25400) & (g["logTrnSta"] == "E"), "logValLan014"].sum()
                - g.loc[(g["ctrCod"] == 25300) & (g["logTrnSta"] != "E"), "logValLan014"].sum()
                + g.loc[(g["ctrCod"] == 25300) & (g["logTrnSta"] == "E"), "logValLan014"].sum()
            )
        })
    ).reset_index()

    # Cálculo do Malote (107)
    df_malote = df_107.groupby("logCnaNum004", as_index=False).apply(
        lambda g: pd.Series({
            "Malote": (
                g["logValTot014"].sum()
                - g.loc[(g["ptaCod"] == 245), "logValTot014"].sum()
                - g.loc[(g["logTrnSta"] == "E"), "logValTot014"].sum()
            )
        })
    ).reset_index()

    df_malote.rename(columns={"logCnaNum004": "ptaCod"}, inplace=True)

    # Criando DataFrame final
    df_movimentacao = df_recolhimento.merge(df_malote, on="ptaCod", how="left")
    df_movimentacao.fillna(0, inplace=True)

    # Aplicando a fórmula da Média Mês
    df_movimentacao["Media_Mes"] = (df_movimentacao["Recolhimento"] - df_movimentacao["Malote"]) / 22

    # Exibir os dados antes de inserir no banco (apenas para debug)
    print(tabulate(df_movimentacao, headers='keys', tablefmt='psql', showindex=False))

    # Verificar se a coluna do mês atual existe na tabela cnp_historico
    with engine.connect() as conn:
        resultado = conn.execute(text("SHOW COLUMNS FROM cnp_historico;"))
        colunas_existentes = {row[0] for row in resultado}
        
        if coluna_mes_atual not in colunas_existentes:
            logging.error(f"A coluna '{coluna_mes_atual}' não existe na tabela cnp_historico!")
            raise ValueError(f"A coluna '{coluna_mes_atual}' não existe na tabela cnp_historico!")

    # Filtrar CNPs válidos cadastrados na tabela cnp_data
    df_cnp_data = pd.read_sql("SELECT cnp FROM cnp_data", engine)
    cnps_validos = set(df_cnp_data["cnp"])
    df_movimentacao = df_movimentacao[df_movimentacao["ptaCod"].isin(cnps_validos)]

    # Criar CNPs novos na tabela cnp_historico antes de atualizar
    with engine.connect() as conn:
        for cnp in df_movimentacao["ptaCod"]:
            query_insert = text("""
                INSERT IGNORE INTO cnp_historico (cnp) VALUES (:cnp);
            """)
            conn.execute(query_insert, {"cnp": int(cnp)})

    # Exibir os SQLs de atualização (apenas para log)
    with engine.connect() as conn:
        for _, row in df_movimentacao.iterrows():
            sql_query = f"""
                UPDATE cnp_historico
                SET `{coluna_mes_atual}` = {row['Media_Mes']}
                WHERE cnp = {row['ptaCod']};
            """
            # logging.info(f"Executando SQL: {sql_query}")

    # Atualizar a coluna do mês atual na tabela cnp_historico
    with engine.begin() as conn:
        for _, row in df_movimentacao.iterrows():
            query_update = text(f"""
                UPDATE cnp_historico
                SET `{coluna_mes_atual}` = :media_mes
                WHERE cnp = :cnp;
            """)
            conn.execute(query_update, {
                "media_mes": round(float(row["Media_Mes"]), 2),
                "cnp": int(row["ptaCod"])
            })

    logging.info(f"Tabela cnp_historico atualizada com sucesso para a coluna {coluna_mes_atual}.")
    logging.info("ETL concluído com sucesso!")

    # --- IMPLEMENTAÇÃO ADICIONAL: ATUALIZAR valor_cobertura na tabela seguradora ---

    # Obter as colunas da tabela cnp_historico novamente (para garantir que a variável esteja definida)
    with engine.connect() as conn:
        resultado = conn.execute(text("SHOW COLUMNS FROM cnp_historico;"))
        colunas_existentes = {row[0] for row in resultado}

    # Obter os últimos 12 meses para cálculo da média
    ultimos_12_meses = []
    for i in range(12):
        data_retroativa = primeira_data - timedelta(days=i * 30)
        mes_retroativo = data_retroativa.strftime("%m")
        ano_retroativo = data_retroativa.strftime("%y")
        coluna_mes = f"{mes_map[mes_retroativo]}_{ano_retroativo}"
        ultimos_12_meses.append(coluna_mes)

    # Construir a expressão para somar os valores dos últimos 12 meses
    expressao_soma = "+".join(ultimos_12_meses)

    # Gerar a query SQL para obter a média dos últimos 12 meses
    query_media = f"""
        SELECT cnp, COALESCE(ROUND(SUM({expressao_soma}) / 12, 2), 0) AS media_mensal
        FROM cnp_historico
        GROUP BY cnp;
    """
    df_media = pd.read_sql(query_media, engine)

    # Aplicar a regra da apólice para definir o valor da cobertura
    def definir_cobertura(media_mensal):
        if media_mensal <= 70000:
            return 70000
        elif media_mensal <= 90000:
            return 90000
        elif media_mensal <= 100000:
            return 100000
        elif media_mensal <= 120000:
            return 120000
        elif media_mensal <= 150000:
            return 150000
        elif media_mensal <= 180000:
            return 180000
        else:
            return 200000

    df_media["valor_cobertura"] = df_media["media_mensal"].apply(definir_cobertura)

    # Atualizar a tabela seguradora com o valor da cobertura calculado
    with engine.begin() as conn:
        for _, row in df_media.iterrows():
            query_update = text("""
                UPDATE seguradora
                SET valor_cobertura = :valor_cobertura
                WHERE cnp = :cnp;
            """)
            conn.execute(query_update, {
                "valor_cobertura": row["valor_cobertura"],
                "cnp": int(row["cnp"])
            })

    logging.info("Tabela seguradora atualizada com sucesso.")
    logging.info("ETL concluído com sucesso!")
    
    return "ETL executado com sucesso!"
