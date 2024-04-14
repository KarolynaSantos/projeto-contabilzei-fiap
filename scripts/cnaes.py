# Importações de bibliotecas necessárias
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from caminho import ProjetoFiap  # Módulo personalizado para manipulação de caminhos
import os

# Definição da pasta contendo os arquivos a serem processados
pasta = 'cnaes'

# Inicialização do objeto ProjetoFiap para gerenciamento de caminhos e arquivos
bases = ProjetoFiap()

# Obtendo cabeçalhos corretos para os arquivos da pasta especificada
cabecalhos = bases.pega_cabecalho(pasta)
bases.ajustar_arquivos()  # Ajustando arquivos conforme necessário

# Caminho dos arquivos CSV e parquet
location = bases.caminho_csv
location_parquet = location.replace('/csv/', '/parquet/')

# Inicialização da sessão Spark com configurações personalizadas
spark = (SparkSession
         .builder
         .appName(pasta)
         .config("spark.driver.extraClassPath", bases.caminho_jar_mysql)
         .getOrCreate())

# Leitura do arquivo CSV para um DataFrame Spark
df = (spark.read.format('csv')
      .option("delimiter", ';')
      .option("encoding", "ISO-8859-1")
      .load(location))

# Renomeação das colunas do DataFrame conforme os cabeçalhos corretos
colunas_antigas = df.columns
for idx, cabecalho in enumerate(cabecalhos):
    df = df.withColumnRenamed(df.columns[idx], cabecalho)

# Aplicação de substituições baseadas em um dicionário de para cada coluna
depara = bases.pegar_depara()
for coluna, linhas in depara.items():
    for linha in linhas:
        de = linha['de']
        para = linha['para']
        df = df.withColumn(coluna, when(col(coluna) == de, lit(para)).otherwise(col(coluna)))

# Salvamento dos dados resultantes no banco de dados
bases.salvar_no_banco(df, 'contabilizei', 'cnaes')
