from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os
from caminho import ProjetoFiap

pasta = 'empresas'

# Pegando nomes corretos do df
bases = ProjetoFiap()
cabecalhos = bases.pega_cabecalho(pasta) #trocar nome da pasta que contem os arquivos que quero tratar 
bases.ajustar_arquivos()

location = bases.caminho_csv
location_estab = location.replace('/empresas/csv/', '/estabelecimentos/parquet/')

# iniciando sessao spark
spark = (SparkSession
        .builder
        .appName(pasta)
        .getOrCreate()
        )

# Lendo arquivo csv com spark
df = (
    spark
    .read
    .format('csv')
    .option("delimiter", ';')
    .load(location)
)

# lendo estabelecimentos tratados para fazer o join
df_estab = (
    spark
    .read
    .format('parquet')
    .load(location_estab)
)

# Pegando colunas do df
colunas_antigas = df.columns

# Renomeando os cabecalhos
for x in range(len(cabecalhos)):
    df = df.withColumnRenamed(colunas_antigas[x],cabecalhos[x])

# ajustando depara
depara = bases.pegar_depara()
for coluna in depara.keys():
    for linha in depara[coluna]:
        de = linha['de']
        para = linha['para']

        df = df.withColumn(coluna, when(col(coluna) == de, lit(para)).otherwise(col(coluna)))


# Colunas desejadas
colunas_desejadas = [
    'empresas.cnpj_basico',
     'empresas.natureza_juridica',
     'empresas.capital_social_da_empresa',
     'empresas.porte_da_empresa'
]

# colocando alias nas tabelas 

df = df.alias('empresas')
df_estab = df_estab.alias('estab')

# fazendo o join 

df_join = (
    df
    .join(df_estab, col('empresas.cnpj_basico') == col('estab.cnpj_basico'), 'inner')
    .select(colunas_desejadas)
)

# apagando arquivos parquet
for x in os.listdir(location_estab):
    arquivo = os.path.join(location_estab, x)
    os.remove(arquivo)

# apagando pasta
os.rmdir(location_estab)