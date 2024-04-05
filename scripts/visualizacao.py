import mysql.connector
import pandas as pd
import os

# Define o caminho para o arquivo credenciais.env que contém as credenciais
caminho_cred = r'C:\Users\Karol\OneDrive\Documentos\FIAP\projeto-contabilzei-fiap\config\credenciais.env'

# Abre o arquivo em modo de leitura ('r') e atribui-o ao identificador 'f'
with open(caminho_cred, 'r') as f:
    # Lê todo o conteúdo do arquivo e o armazena na variável 'arquivo'
    arquivo = f.read()

# Itera sobre cada linha do arquivo
for linha in arquivo.split('\n'):
    # Divide cada linha em duas partes com base no sinal de igual ('=')
    valores = linha.split('=')
    # Remove espaços em branco em excesso ao redor da chave (primeira parte da linha)
    chave = valores[0].strip()
    # Remove espaços em branco em excesso ao redor do valor (segunda parte da linha)
    valor = valores[1].strip()
    # Define uma variável de ambiente com a chave e o valor extraídos do arquivo
    os.environ[chave] = valor

# Obtém as credenciais do ambiente
db_username = os.getenv("USER-MYSQL")
db_password = os.getenv("PASSWORD-MYSQL")
# Define o nome do banco de dados
db_name = 'contabilizei'
# Obtém o endereço do host do banco de dados do ambiente
db_host = os.getenv("HOST-MYSQL")

# Crie a conexão
conn = mysql.connector.connect(
    user=db_username,
    password=db_password,
    database=db_name,
    host=db_host
)

# Crie o cursor
cursor = conn.cursor()

# Execute uma consulta SQL
consulta_sql = "SELECT * FROM contabilizei.estabelecimentos"
cursor.execute(consulta_sql)

# Recupere os resultados e armazene-os em um DataFrame do Pandas
result = cursor.fetchall()
df = pd.DataFrame(result, columns=cursor.column_names)

# Visualize os dados
print(df.head())

# Feche a conexão
cursor.close()
conn.close()
