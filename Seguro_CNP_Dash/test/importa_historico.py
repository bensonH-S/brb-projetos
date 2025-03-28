import pandas as pd
from sqlalchemy import create_engine

# Configuração da conexão com o banco de dados
DATABASE_URI = 'mariadb+mariadbconnector://root:@localhost:3306/gecaf'
engine = create_engine(DATABASE_URI)

# Caminho do arquivo Excel e nome da aba
# excel_file = r"C:\Users\u512228\Documents\Base\Dados_Historico.xlsx"
excel_file = r"F:\Users\Administrador\OneDrive\Documentos\Base\MEDIA_MENSAL_ATUALIZAÇÃO.xlsx"
sheet_name = "Total 2024"  # Aba da planilha

# Ler o Excel sem interpretar automaticamente os valores
df = pd.read_excel(excel_file, sheet_name=sheet_name, header=0, parse_dates=False, dtype=str)

# Remover a coluna "Unnamed: 0" se ela existir
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# Forçar os nomes das colunas a serem strings
df.columns = df.columns.astype(str)
print("Columns antes do renomeamento:", df.columns.tolist())

# Renomear as colunas para o padrão da tabela cnp_historico
rename_dict = {
    "CNP": "cnp",
    "dez/23": "dez_23",
    "jan/24": "jan_24",
    "fev/24": "fev_24",
    "mar/24": "mar_24",
    "abr/24": "abr_24",
    "mai/24": "mai_24",
    "jun/24": "jun_24",
    "jul/24": "jul_24",
    "ago/24": "ago_24",
    "set/24": "set_24",
    "out/24": "out_24",
    "nov/24": "nov_24",
    "dez/24": "dez_24",
    "jan/25": "jan_25"
}

df.rename(columns=rename_dict, inplace=True)

# Garantir que a coluna "cnp" seja numérica e sem valores None
if "cnp" in df.columns:
    df["cnp"] = pd.to_numeric(df["cnp"], errors="coerce").fillna(0).astype(int)

# 🔹 **Correção da conversão dos valores monetários**
def convert_to_float(value):
    """Função para remover separadores incorretos e converter para float"""
    if isinstance(value, str):
        value = value.replace(',', '.')  # Substitui decimal correto
        try:
            return round(float(value), 2)  # Arredonda para 2 casas decimais
        except ValueError:
            return 0.0
    return 0.0

for col in df.columns:
    if col != "cnp":
        print(f"🔹 Convertendo coluna: {col}")  # Debugging
        print("Antes da conversão:", df[col].head(10).tolist())  # Mostra os primeiros valores antes da conversão
        df[col] = df[col].apply(lambda x: convert_to_float(str(x)))  # Aplica a conversão
        print("Depois da conversão:", df[col].head(10).tolist())  # Mostra os primeiros valores após a conversão

# 🔹 **Teste de Conversão**
# print("\nPrévia dos valores corrigidos antes da inserção:")
# print(df.head(10))  # Mostra os primeiros 10 registros para checagem

# 🔹 **Filtrar apenas os CNPs que existem na tabela `cnp_data`**
valid_cnp = pd.read_sql("SELECT cnp FROM cnp_data", engine)
valid_cnp_set = set(valid_cnp["cnp"])
df = df[df["cnp"].isin(valid_cnp_set)]

if df.empty:
    print("Nenhuma linha válida para inserir. Todos os CNPs estão ausentes na tabela `cnp_data`.")
else:
    # 🔹 **Remover CNPs que já existem na tabela `cnp_historico`**
    existing_cnp = pd.read_sql("SELECT DISTINCT cnp FROM cnp_historico", engine)
    existing_cnp_set = set(existing_cnp["cnp"])
    
    df = df[~df["cnp"].isin(existing_cnp_set)]  # Remove duplicatas já existentes no banco
    
    if df.empty:
        print("Nenhuma nova linha para inserir. Todos os CNPs já estão na tabela `cnp_historico`.")
    else:
        batch_size = 50
        for i in range(0, len(df), batch_size):
            df.iloc[i:i + batch_size].to_sql('cnp_historico', engine, if_exists='append', index=False)
            print(f"Inserido batch {i} até {i + batch_size}")

        print("Dados importados com sucesso!")
