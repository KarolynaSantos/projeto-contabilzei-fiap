from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os
from caminho import ProjetoFiap

pasta = 'cnaes'
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
        .config("spark.driver.extraClassPath", bases.caminho_jar_mysql)
        .getOrCreate()
        )

# Lendo arquivo csv com spark
df = (
    spark
    .read
    .format('csv')
    .option("delimiter", ';')
    .option("encoding", "ISO-8859-1")
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
        

# Salvando dados no banco
bases.salvar_no_banco(df, 'contabilizei', 'cnaes')