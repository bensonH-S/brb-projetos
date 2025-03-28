import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Configuração do banco de dados
DATABASE_URI = 'mariadb+mariadbconnector://root:@localhost:3306/gecaf'
engine = create_engine(DATABASE_URI)

# Caminho do arquivo Excel
# file_path = r"C:\Users\u512228\Documents\Cadastro_CNP.xlsx"
file_path = r"F:\Users\Administrador\OneDrive\Documentos\Base\Cadastro_CNP.xlsx"
sheet_name = "CNPS"

# Ler o Excel (a primeira linha é o cabeçalho e os dados começam na segunda linha)
df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)

# Renomear as colunas para corresponder à tabela do banco de dados
rename_mapping = {
    "CNP": "cnp",
    "Situação": "situacao",
    "CNPJ": "cnpj",
    "Razão Social": "razao_social",
    "CC": "cc",
    "Telefone": "telefone",
    "Telefone do Proprietário": "telefone_proprietario",
    "Email": "email",
    "Endereço": "endereco",
    "Bairro": "bairro",
    "Cidade": "cidade",
    "UF": "uf",
    "CEP": "cep",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Observações": "observacao"
}
df = df.rename(columns=rename_mapping)

# Filtrar apenas as linhas onde a coluna "cnp" possui um valor efetivo
df = df[df["cnp"].apply(lambda x: pd.notna(x) and str(x).strip() != "" and str(x).strip().upper() != "NAN")]

# Converter "cnp" para inteiro (garantindo o tipo correto para a chave primária)
df["cnp"] = df["cnp"].astype(int)

# Garantir que o DataFrame contenha somente as colunas esperadas (ordem e nomes conforme a tabela)
expected_cols = ["cnp", "situacao", "cnpj", "razao_social", "cc", "telefone",
                 "telefone_proprietario", "email", "endereco", "bairro", "cidade",
                 "uf", "cep", "latitude", "longitude", "observacao"]
df = df[expected_cols]

def normalize_text(text):
    """
    Remove espaços extras (início, fim e entre palavras) e converte para maiúsculas.
    """
    return " ".join(str(text).strip().split()).upper()

# Debug: exibe os valores únicos normalizados da coluna "situacao"
print("Valores únicos normalizados da coluna 'situacao':")
print(df["situacao"].apply(normalize_text).unique())

def convert_situacao(x):
    """
    Se o valor normalizado for "ATIVA" ou "1", retorna 1; 
    caso contrário, retorna 0.
    """
    normalized = normalize_text(x)
    if normalized in ["ATIVA", "1"]:
        return 1
    else:
        return 0

# Converter a coluna "situacao" conforme o esperado
df["situacao"] = df["situacao"].apply(convert_situacao)

# Converter as colunas de texto para string (para campos VARCHAR no banco)
varchar_cols = ['cnpj', 'razao_social', 'cc', 'telefone', 'telefone_proprietario',
                'email', 'endereco', 'bairro', 'cidade', 'uf', 'cep', 'observacao']
for col in varchar_cols:
    if col in df.columns:
        df[col] = df[col].fillna("").astype(str)

def convert_coord(val):
    """
    Remove os pontos e divide por 1e6 para converter a coordenada para decimal.
    """
    try:
        s = str(val)
        s_clean = s.replace('.', '')
        return float(s_clean) / 1e6
    except Exception:
        return np.nan

# Converter as colunas de latitude e longitude
df['latitude'] = df['latitude'].apply(convert_coord)
df['longitude'] = df['longitude'].apply(convert_coord)

# Inserir os dados na tabela 'cnp_data'
df.to_sql('cnp_data', engine, if_exists='append', index=False)

print("Dados importados com sucesso!")
