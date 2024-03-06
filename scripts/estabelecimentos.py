from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os
from caminho import ProjetoFiap

pasta = 'estabelecimentos'
# Pegando nomes corretos do df
bases = ProjetoFiap()
cabecalhos = bases.pega_cabecalho(pasta) #trocar nome da pasta que contem os arquivos que quero tratar 
bases.ajustar_arquivos()

location = bases.caminho_csv

location_parquet = location.replace('/csv/','/parquet/')

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
    'cnpj'
    ,'cnpj_basico'
    ,'identificador_matriz_filial'
    ,'situacao_cadastral'
    ,'data_situacao_cadastral'
    ,'data_de_inicio_atividade'
    ,'cnae_fiscal_principal'
    ,'uf'
    ,'município'
]

#manipulando df

df = (
    df
    # Ajustando coluna de data
    .withColumn('data_situacao_cadastral', to_date(col('data_situacao_cadastral'), 'yyyyMMdd'))
    # Filtrando data, uf e situacao cadastral ativa do df
    .filter(
        (col('data_situacao_cadastral') >= '2023-01-01')
        &(upper(col('uf')).isin('SP', 'RJ'))
        &(col('situacao_cadastral') == 'ATIVA')
    )
    # Concatenando coluna de cnpj do df
    .withColumn('cnpj', concat(col('cnpj_basico'), col('cnpj_ordem'), col('cnpj_dv')))
    # Selecionando colunas
    .select(colunas_desejadas)
)

# escrevando o arquivo em parquet para usar no processo de empresas

(
    df
    .write
    .format('parquet')
    .mode('overwrite')
    .save(location_parquet)
)