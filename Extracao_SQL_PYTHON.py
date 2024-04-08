import pyodbc
import pandas as pd 
import re
import html
from bs4 import BeautifulSoup

# Função para remover tags HTML de uma string
def remove_html_tags(text):
    if text is None:
        return ''
    clean = re.compile('<.*?>')
    return re.sub(clean, '', str(text))

# EXTRAÇÃO DA BASE INTEIRA DA SELEME CONSULTING
server = '000.00.00.000'
database = 'xxx'
username = 'xxx'
password = 'xxx'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Defina sua consulta SELECT (Query 1)

queries = [
"""
  --Sua query aqui
""",

"""
 --Pode adcionar mais querys
"""
]

# Executar as consultas e armazenar os resultados em um dicionário de DataFrames
dfs = {}
for i, query in enumerate(queries, start=1):
    df = pd.read_sql_query(query, conn)
    for col in df.columns:
        df[col] = df[col].apply(lambda x: remove_html_tags(html.unescape(str(x))).strip())
    # Remover linhas totalmente em branco
    df.dropna(how='all', inplace=True)
    # Substituir valores None por uma string vazia em todo o DataFrame
    df.fillna('', inplace=True)
    dfs[f'df_{i}'] = df

# Feche o cursor e a conexão
cursor.close()
conn.close()





# Especificar o caminho do arquivo CSV
caminhos_arquivos = [

   #SEU/CAMINHO/AQUI,
   #SEU/CAMINHO/AQUI,
   


]

# Salvar os DataFrames como arquivos CSV com o separador ;
for i, (key, df) in enumerate(dfs.items()):
    # Substituir valores None por strings vazias em todo o DataFrame
    df.fillna('', inplace=True)  # Primeiro substituímos os valores None por string vazia
    df.to_csv(caminhos_arquivos[i], index=False, sep=';')




print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Querys Realizadas com Sucesso!")
