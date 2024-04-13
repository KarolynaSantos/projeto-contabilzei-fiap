#conector com banco de dados
import mysql.connector
import pandas as pd
import os
import boto3
import io


#visualizacao
import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

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

# Copiando df_sql para um novo dataframe
df_sql_join = df_sql.copy()

# Extraindo os dois primeiros dígitos da coluna 'cnae_fiscal_principal' e transformando em inteiros
df_sql_join['divisoes_'] = df_sql_join['cnae_fiscal_principal'].astype(str).str[:2].astype(int)

# Realizando o join entre df_sql_join e df_s3 usando a coluna 'divisoes'
df_final = pd.merge(df_sql_join, df_s3, left_on='divisoes_', right_on='divisoes', how='inner')

# Atribua o resultado ao DataFrame df
df = df_final

# ========================================================================================================================
# Convertendo a coluna 'data_situacao_cadastral' para datetime
df['data_situacao_cadastral'] = pd.to_datetime(df['data_situacao_cadastral'])

# Removendo caracteres não numéricos da coluna 'capital_social_da_empresa'
df['capital_social_da_empresa'] = df['capital_social_da_empresa'].str.replace(',', '')

# Convertendo para tipo inteiro
df['capital_social_da_empresa'] = df['capital_social_da_empresa'].astype(float)

# Feche a conexão
cursor.close()
conn.close()

# ========================================================================================================================
#INICIANDO DASHBOARD

#palhetade cores
cores = ['#00F7F7', '#00236A', '#F4F7FB']

# Definindo o tamanho da tela
st.set_page_config(layout="wide")

# Carregando e exibindo a logo
st.image("https://theme.zdassets.com/theme_assets/527873/d7addb22e6b934c69a805b22680038893c822101.png", width=300)

# Definindo o título com a cor e tamanho desejados
st.markdown(
    f"""
    <h1 style='color:#00236A; font-size:32px;'>Dashboard Analítico de Abertura de Empresas no Estado de São Paulo</h1>
    """,
    unsafe_allow_html=True
)

# Escrevendo uma linha em HTML para separar o titulo
st.write("<hr>", unsafe_allow_html=True)

# Criando filtro de ramo de atividade
filtro_ramo_atividade = df_final['denominacoes'].unique()

# Adicionando o filtro na interface Streamlit
opcao_selecionada = st.selectbox('Selecione um ramo de atividade:', filtro_ramo_atividade)

# Filtrando o dataframe com base na opção selecionada
df_filtrado = df[df['denominacoes'] == opcao_selecionada]

# # Exibindo o dataframe filtrado
# st.write('Dataframe filtrado:', df_filtrado)

# Dividindo a tela em duas colunas
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)
col6, col7 = st.columns(2)

# Filtrando o dataframe com base na opção selecionada
df_filtrado = df[df['denominacoes'] == opcao_selecionada]

# ========================================================================================================================
# Adicionando grafico 1 - Média do Capital Social
# Calcular a média do capital social
media_capital = df_filtrado['capital_social_da_empresa'].mean()

# Plotar o gráfico
# Exibir a média do capital em uma caixa na col1
col1.subheader("Média do Capital Social")
col1.write(f"R$ {media_capital:.2f}")

# ========================================================================================================================
# Adicionando grafico 2 - Tempo Média de Abertura de CNPJ

import requests
from bs4 import BeautifulSoup

# URL da página para extrair a informação
url = "https://www.contabilizei.com.br/contabilidade-online/quanto-tempo-leva-para-abrir-uma-empresa/?utm_device=c&utm_term=&utm_source=google&utm_medium=cpc&utm_campaign=%5BMAX%5D_Performance_RMKT_Vendas&hsa_cam=20859898068&hsa_grp=&hsa_mt=&hsa_src=x&hsa_ad=&hsa_acc=1466761651&hsa_net=adwords&hsa_kw=&hsa_tgt=&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwlN6wBhCcARIsAKZvD5jvTi4-tapqzrFGQbO54HZ98-j-14qVGzmvx8epFYjzrqiXfiv2HXwaAm_rEALw_wcB#quanto-tempo-demora-para-abrir-uma-empresa"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Faz o parsing do HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra o elemento que contém a informação desejada
    elemento = soup.find(text=lambda text: "São Paulo (SP):" in str(text))
else:
    # Se a requisição falhar, imprime uma mensagem de erro
    print("Falha ao acessar a página:", response.status_code)

# Plotando o gráfico
# Exibindo a média do capital em uma caixa na col2
col2.subheader("Tempo Médio Para Abrir Uma Empresal")
col2.write(elemento)

# ========================================================================================================================
# Adicionando grafico 3 

# ========================================================================================================================
# Adicionando grafico 4 - Evolução Abertura CNPJ por Periodo
# Extraindo o mês e o ano da coluna de data
df_filtrado['mes_ano'] = df_filtrado['data_situacao_cadastral'].dt.strftime('%Y-%m')

# Contando a quantidade de CNPJs por mês
df_agrupado = df_filtrado.groupby('mes_ano')['cnpj'].nunique().reset_index(name='quantidade')

# Plotando o gráfico de barras
fig = px.line(df_agrupado, x='mes_ano', y='quantidade', labels={'quantidade': 'Quantidade de CNPJs'},
             title='Crescimento de Abertura de CNPJ',
             color_discrete_sequence=cores)
fig.update_xaxes(type='category')  # Define o eixo x como uma categoria
col4.plotly_chart(fig)

# Escrevendo uma linha em HTML para separar os gráficos
st.write("<hr>", unsafe_allow_html=True)

# ========================================================================================================================
# Adicionando grafico 5 - Média de Receita por Ramo de Atividade
# Agrupando os dados pela coluna 'data' e calcular a média da coluna 'capital_social_da_empresa'
df_media = df_filtrado.groupby('mes_ano')['capital_social_da_empresa'].mean().reset_index()

# Plotando o gráfico de linha

fig_2 = px.line(df_media, x='mes_ano', y='capital_social_da_empresa', 
              labels={'capital_social_da_empresa': 'Média do Capital Social da Empresa'},
              title='Média de Capital Social por Ramo de Atividade',
              color_discrete_sequence=cores)
fig_2.update_xaxes(type='category')  # Define o eixo x como uma categoria

col5.plotly_chart(fig_2)

# ========================================================================================================================
# Agrupando os dados pela coluna 'CNAE (Descrição)' e calculando a média da coluna 'Média Capital Social'
df_capital = df_filtrado.groupby('descricao')['capital_social_da_empresa'].mean().reset_index()

# Renomeando as colunas
df_capital.rename(columns={'descricao': 'CNAE (Descrição)', 'capital_social_da_empresa': 'Média Capital Social'}, inplace=True)

# Exibindo a tabela sem o índice
col6.write(df_capital)

# ========================================================================================================================
# Grafico 7 -  Exibir documentos

col7.subheader("Documentos necessários para abrir uma empresa são:")
col7.write("""
- Cópia autenticada do RG;
- Cópia simples do CPF;
- Certidão de casamento (se for casado);
- Carteira do órgão regulamentador (como OAB, CRA, CREA, CORE, entre outros);
- Cópia simples do comprovante de endereço residencial; 
- Última declaração do IR (Imposto de Renda).

Já os documentos da futura empresa são:
- Cópia simples do comprovante de endereço comercial onde será a sede da empresa (se for diferente do endereço residencial);
- Cópia do IPTU (Imposto Predial e Territorial Urbano) ou de outro documento que conste a Inscrição Imobiliária, ou Indicação Fiscal do imóvel que irá abrigar o estabelecimento;  
- Atividades da empresa;  
- Nome fantasia da empresa.
""")
