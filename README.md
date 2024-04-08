# Exemplo-de-extracao-com-PYTHON-e-SQL

Este script em Python foi feito para se conectar a um banco de dados SQL Server, executar consultas SQL especificadas e salvar os resultados como arquivos CSV. 
Isso Pode ajudar você a criar BACKUPS, ou até mesmo levar as informações para ferramentas de visualizações (em casos Específicos) .

Aqui está uma explicação passo a passo:

Importações de bibliotecas:

pyodbc: É utilizada para conectar-se ao banco de dados SQL Server.
pandas as pd: É uma biblioteca de análise de dados que fornece estruturas de dados e ferramentas de análise.
re: É uma biblioteca para expressões regulares, utilizada para manipular texto.
html: É usada para manipular HTML.
BeautifulSoup do módulo bs4: É uma biblioteca Python para analisar dados HTML e XML.
Função remove_html_tags: É definida para remover tags HTML de uma string usando expressões regulares.

Parâmetros de conexão ao banco de dados:

server, database, username e password: São as informações necessárias para se conectar ao banco de dados. Elas devem ser fornecidas pelo usuário.
connection_string: É uma string de conexão que contém as informações necessárias para estabelecer a conexão com o banco de dados.
Conexão ao banco de dados:

pyodbc.connect: Estabelece uma conexão com o banco de dados usando a connection_string definida anteriormente.
conn.cursor(): Cria um objeto cursor para executar consultas SQL.
Definição das consultas SQL:

queries: É uma lista de strings, onde cada string contém uma consulta SQL. O usuário pode adicionar suas próprias consultas aqui. 
Execução das consultas SQL:

Um loop é usado para iterar sobre cada consulta na lista queries.
Cada consulta é executada usando pd.read_sql_query, que executa a consulta SQL no banco de dados e retorna um DataFrame do Pandas contendo os resultados.
Em seguida, a função remove_html_tags é aplicada a cada valor do DataFrame para remover tags HTML e caracteres especiais.
Linhas totalmente em branco são removidas e valores None são substituídos por strings vazias.
Fechamento do cursor e da conexão: Após a execução das consultas, o cursor e a conexão são fechados para liberar recursos.

Especificação dos caminhos dos arquivos CSV:

caminhos_arquivos: É uma lista de strings, onde cada string contém o caminho para salvar um arquivo CSV. O usuário deve fornecer o caminho desejado para salvar cada arquivo.
Salvamento dos DataFrames como arquivos CSV:

Um loop é usado para iterar sobre cada DataFrame.
Cada DataFrame é salvo como um arquivo CSV usando df.to_csv, onde o separador é definido como ;.
Impressão da mensagem de conclusão: Uma mensagem é exibida indicando que as consultas foram realizadas com sucesso.

Lembre-se de substituir os valores das variáveis server, database, username, password, queries e caminhos_arquivos com as informações relevantes para o seu ambiente antes de executar o script.
