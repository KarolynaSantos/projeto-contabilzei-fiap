from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Window
from pyspark.sql import functions as F
import os
from caminho import ProjetoFiap

pasta = 'estabelecimentos'
chunk = 500
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

cond_row_number = Window.orderBy(F.lit(1))

df = (
    df
    # Ajustando coluna de data
    .withColumn('data_situacao_cadastral', to_date(col('data_situacao_cadastral'), 'yyyyMMdd'))
    # Filtrando data, uf e situacao cadastral ativa do df
    .filter(
        (col('data_situacao_cadastral') >= '2023-01-01')
        &(upper(col('uf')).isin('SP'))
        &(col('situacao_cadastral') == 'ATIVA')
    )
    # Concatenando coluna de cnpj do df
    .withColumn('cnpj', concat(col('cnpj_basico'), col('cnpj_ordem'), col('cnpj_dv')))
    # Selecionando colunas
    .select(colunas_desejadas)
    .withColumn("row_number", F.row_number().over(cond_row_number))
    .limit(10_000) #limitando df para uma poc
    .cache()
)

quantidade_de_linhas = df.count()

# Salvando dados no banco

voltas = 1
for x in range(0, quantidade_de_linhas + 1, chunk):
    inicio = x + 1
    fim = inicio + chunk -1
    if inicio < quantidade_de_linhas:
        if voltas == 1:
            modo = 'overwrite'
        else:
            modo = 'append'
        voltas +=1
        print(f'Salvando de {inicio} até {fim}: ',end='')
        
        bases.salvar_no_banco(df.filter(col('row_number').between(inicio, fim).drop('row_number')), 'contabilizei', 'estabelecimentos', modo)