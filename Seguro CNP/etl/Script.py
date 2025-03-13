import pandas as pd
import logging
from datetime import datetime
from tabulate import tabulate  # Importa a biblioteca tabulate

# Configuração do log
log_file_path = r"C:\Users\u512228\Documents\etl_log.log"
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Iniciando o processo de ETL...")

# Caminho do arquivo Excel
excel_file = r"C:\Users\u512228\Documents\Base\Relatório EIS.xlsx"

# Caminho do arquivo CSV temporário para validação
csv_temp_file = r"C:\Users\u512228\Documents\temp_movimentacao.csv"

def exibir_dados_em_tabela(df: pd.DataFrame, log_output=False):
    """
    Exibe o DataFrame em formato de tabela utilizando a biblioteca tabulate.
    Se log_output for True, registra a tabela no arquivo de log, caso contrário imprime no console.
    """
    df_formatado = df.copy()
    for col in ["Recolhimento", "Malote", "Media_Mes"]:
        if col in df_formatado.columns:
            df_formatado[col] = df_formatado[col].apply(lambda x: f"{x:,.2f}")
    
    tabela_str = tabulate(df_formatado, headers='keys', tablefmt='psql', showindex=False)
    
    if log_output:
        logging.info("\n" + tabela_str)
    else:
        print(tabela_str)

# Leitura da planilha
try:
    df_005 = pd.read_excel(excel_file, sheet_name="005")
    df_107 = pd.read_excel(excel_file, sheet_name="107")
    logging.info("Planilha carregada com sucesso.")
except Exception as e:
    logging.error(f"Erro ao carregar planilha: {e}")
    raise

# Remover espaços extras dos nomes das colunas
df_005.columns = df_005.columns.str.strip()
df_107.columns = df_107.columns.str.strip()

# Verifica se as colunas necessárias existem na planilha
colunas_necessarias_005 = {"ptaCod", "ctrCod", "logTrnSta", "logValLan014"}
colunas_necessarias_107 = {"logCnaNum004", "logValTot014", "ptaCod", "logTrnSta"}

if not colunas_necessarias_005.issubset(set(df_005.columns)) or not colunas_necessarias_107.issubset(set(df_107.columns)):
    logging.error("Colunas esperadas não encontradas na planilha. Verifique os nomes das colunas.")
    raise ValueError("Colunas esperadas não encontradas na planilha.")

# **Cálculo do Recolhimento (005)**
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

# **Cálculo do Malote (107)**
df_malote = df_107.groupby("logCnaNum004", as_index=False).apply(
    lambda g: pd.Series({
        "Malote": (
            g["logValTot014"].sum()
            - g.loc[(g["ptaCod"] == 245), "logValTot014"].sum()  # Remove valores do ptaCod 245
            - g.loc[(g["logTrnSta"] == "E"), "logValTot014"].sum()  # Remove valores onde logTrnSta == "E"
        )
    })
).reset_index()

df_malote.rename(columns={"logCnaNum004": "ptaCod"}, inplace=True)

# Criando DataFrame final
df_movimentacao = df_recolhimento.merge(df_malote, on="ptaCod", how="left")
df_movimentacao.fillna(0, inplace=True)

# **Aplicando a fórmula da Média Mês**
df_movimentacao["Media_Mes"] = (df_movimentacao["Recolhimento"] - df_movimentacao["Malote"]) / 22

# **Gerar arquivo CSV para validação**
df_movimentacao.to_csv(csv_temp_file, index=False, encoding="utf-8-sig")
logging.info(f"Arquivo temporário gerado com sucesso: {csv_temp_file}")
logging.info("Valide os dados no CSV antes de continuar para a inserção no banco.")

# **Exibir os dados corrigidos em formato tabular**
exibir_dados_em_tabela(df_movimentacao)
