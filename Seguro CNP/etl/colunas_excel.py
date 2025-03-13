import pandas as pd

# Definir caminho do Excel e nome da aba
excel_file = r"C:\Users\u512228\Documents\FOLLOW UP CNP 2025.xlsx"
sheet_name = "FOLLOW UP"

# Ler o arquivo Excel
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Imprimir os nomes das colunas
print("Colunas do DataFrame:", df.columns.tolist())
