#conector com banco de dados
import mysql.connector
import pandas as pd
import os

#visualizacao
import pandas as pd
import geopandas
import streamlit as st
import folium
import plotly.express as px

# Define o caminho para o arquivo credenciais.env que contém as credenciais
caminho_cred = r'C:/Users/Karol/OneDrive\Documentos/FIAP/projeto-contabilzei-fiap/config/credenciais.env'

#r'/tmp/arquivos-fiap/config/credenciais.env'

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
consulta_sql = """
    SELECT 
        estab.*, 
        empresas.natureza_juridica,
        empresas.capital_social_da_empresa,
        empresas.porte_da_empresa,
        cnaes.descricao
    FROM 
        contabilizei.estabelecimentos estab
    JOIN 
        contabilizei.empresas ON estab.cnpj_basico = empresas.cnpj_basico
    JOIN 
        contabilizei.cnaes ON cnaes.codigo = estab.cnae_fiscal_principal
"""
cursor.execute(consulta_sql)

# Recupere os resultados e armazene-os em um DataFrame do Pandas
result = cursor.fetchall()
df = pd.DataFrame(result, columns=cursor.column_names)

# Visualize os dados
print(df.head())

# Feche a conexão
cursor.close()
conn.close()

#INICIANDO DASHBOARD

# título dashboard
st.title('Dashboard Contabilizei')

# Adicionando uma seção para visualizar os dados
st.subheader('Visualização de Dados')

# criando filtro de data
df["data_situacao_cadastral"] = pd.to_datetime(df["data_situacao_cadastral"])
df=df.sort_values("data_situacao_cadastral")

df["month"] = df["data_situacao_cadastral"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["month"].unique())

df.filtered = df[df['month'] == month]
df.filtered

# Divida a tela em duas colunas
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Adicionando grafico
# Extrair o mês e o ano da coluna de data
df['mes_ano'] = df['data_situacao_cadastral'].dt.strftime('%Y-%m')

# Contar a quantidade de CNPJs por mês
df_agrupado = df.groupby('mes_ano')['cnpj'].nunique().reset_index(name='quantidade')

# Plotar o gráfico de barras
fig = px.bar(df_agrupado, x='mes_ano', y='quantidade', labels={'mes_ano': 'Mês e Ano', 'quantidade': 'Quantidade de CNPJs'},
             title='Quantidade de CNPJs por Mês e Ano')
fig.update_xaxes(type='category')  # Define o eixo x como uma categoria
col1.plotly_chart(fig)






