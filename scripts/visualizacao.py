#conector com banco de dados
import mysql.connector
import pandas as pd
import os
import boto3
import io


#visualizacao
import pandas as pd
import geopandas
import streamlit as st
import folium
import plotly.express as px

# ========================================================================================================================
# Pegando dados do banco

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
df_sql = pd.DataFrame(result, columns=cursor.column_names)

# ========================================================================================================================
# Pegando dados do S3

# Inicialize o cliente S3
s3 = boto3.client('s3')

# Especifique o bucket e o caminho do arquivo no S3
bucket_name = 'contabilizei-fiap'
file_key = 'dados/denominacao.xlsx'

# Use o método `get_object` do cliente S3 para obter o objeto
obj = s3.get_object(Bucket=bucket_name, Key=file_key)

# Leia o conteúdo do objeto usando o pandas
df_denominacao = pd.read_excel(io.BytesIO(obj['Body'].read()))


divisoes = df_denominacao['Divisões'].to_list()

denominacoes = df_denominacao['Denominação'].to_list()

novas_denominacoes = []
for x in range(len(divisoes)):
    linha = divisoes[x]
    inicio = int(linha.split(' .. ')[0])
    fim = int(linha.split(' .. ')[-1])

    for y in range(inicio, fim+1):
        novas_denominacoes.append({'divisoes': y ,'denominacoes': denominacoes[x]})

df_s3 = pd.DataFrame(novas_denominacoes)
# ========================================================================================================================
# Juntando df_sql com df_s3

# Copie a coluna 'cnae_fiscal_principal' de df_sql para um novo dataframe
df_sql_join = df_sql[['cnae_fiscal_principal']].copy()

# Extraia os dois primeiros dígitos da coluna 'cnae_fiscal_principal' e transforme em inteiros
df_sql_join['cnae_fiscal_principal'] = df_sql_join['cnae_fiscal_principal'].astype(str).str[:2].astype(int)

# Renomeie a coluna para 'divisoes' para corresponder ao nome da coluna em df_s3
df_sql_join.rename(columns={'cnae_fiscal_principal': 'divisoes'}, inplace=True)

# Realize o join entre df_sql_join e df_s3 usando a coluna 'divisoes'
df_final = pd.merge(df_sql_join, df_s3, on='divisoes', how='inner')

# Adicione todas as colunas do df_sql ao df_final
df_final = pd.concat([df_sql, df_final.drop(columns=['divisoes'])], axis=1)

df = df_final 

# ========================================================================================================================
# Converte a coluna 'data_situacao_cadastral' para datetime
df['data_situacao_cadastral'] = pd.to_datetime(df['data_situacao_cadastral'])

# Remover caracteres não numéricos da coluna 'capital_social_da_empresa'
df['capital_social_da_empresa'] = df['capital_social_da_empresa'].str.replace(',', '')

# Converter para tipo inteiro
df['capital_social_da_empresa'] = df['capital_social_da_empresa'].astype(float)

# Feche a conexão
cursor.close()
conn.close()

# ========================================================================================================================
#INICIANDO DASHBOARD

# Definindo o tamanho da tela
st.set_page_config(layout="wide")

# Carregando e exibindo a logo
st.image("https://theme.zdassets.com/theme_assets/527873/d7addb22e6b934c69a805b22680038893c822101.png", width=200)

# título dashboard
st.title('Dashboard Contabilizei')  

# criando filtro de data
# df["data_situacao_cadastral"] = pd.to_datetime(df["data_situacao_cadastral"])
# df=df.sort_values("data_situacao_cadastral")

# df["month"] = df["data_situacao_cadastral"].apply(lambda x: str(x.year) + "-" + str(x.month))
# month = st.sidebar.selectbox("Mês", df["month"].unique())

# Criando filtro de ramo de atividade
filtro_ramo_atividade = df_final['denominacoes'].unique()

# Adicionando o filtro na interface Streamlit
opcao_selecionada = st.selectbox('Selecione um ramo de atividade:', filtro_ramo_atividade)

# Filtrando o dataframe com base na opção selecionada
df_filtrado = df[df['denominacoes'] == opcao_selecionada]

# # Exibindo o dataframe filtrado
# st.write('Dataframe filtrado:', df_filtrado)

# Dividindo a tela em duas colunas
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# ========================================================================================================================
# Filtrando o dataframe com base na opção selecionada
df_filtrado = df[df['denominacoes'] == opcao_selecionada]

# Adicionando grafico 1 - Evolução Abertura CNPJ por Periodo
# Extraindo o mês e o ano da coluna de data
df_filtrado['mes_ano'] = df_filtrado['data_situacao_cadastral'].dt.strftime('%Y-%m')

# Contando a quantidade de CNPJs por mês
df_agrupado = df_filtrado.groupby('mes_ano')['cnpj'].nunique().reset_index(name='quantidade')

# Plotando o gráfico de barras
fig = px.line(df_agrupado, x='mes_ano', y='quantidade', labels={'mes_ano': 'Data', 'quantidade': 'Quantidade de CNPJs'},
             title='Evolução Abertura CNPJ por Periodo')
fig.update_xaxes(type='category')  # Define o eixo x como uma categoria
col1.plotly_chart(fig)

# ========================================================================================================================
# Adicionando grafico 2 - Média de Receita por Ramo de Atividade
# Agrupando os dados pela coluna 'denominacoes' e calcular a média da coluna 'capital_social_da_empresa'
df_media = df_filtrado.groupby('mes_ano')['capital_social_da_empresa'].mean().reset_index()

# Plotando o gráfico de linha
fig_2 = px.line(df_media, x='mes_ano', y='capital_social_da_empresa', 
              labels={'mes_ano': 'Data', 'capital_social_da_empresa': 'Média do Capital Social da Empresa'},
              title='Média do Capital Social da Empresa por Denominação')
fig_2.update_xaxes(type='category')  # Define o eixo x como uma categoria

# Plotar o gráfico na col2
col2.plotly_chart(fig_2)