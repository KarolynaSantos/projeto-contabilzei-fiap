# Importações de bibliotecas necessárias
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Window
from pyspark.sql import functions as F
from caminho import ProjetoFiap  # Módulo personalizado para manipulação de caminhos
import os

# Definição de parâmetros
pasta = 'estabelecimentos'  # Pasta contendo os arquivos a serem processados
chunk = 500  # Tamanho do chunk para processamento em lote

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

# Leitura dos arquivos CSV para um DataFrame Spark
df = (spark.read.format('csv')
      .option("delimiter", ';')
      .option("encoding", "ISO-8859-1")
      .load(location))

# Renomeação das colunas conforme os cabeçalhos corretos
for idx, cabecalho in enumerate(cabecalhos):
    df = df.withColumnRenamed(df.columns[idx], cabecalho)

# Aplicação de substituições baseadas em um dicionário de para cada coluna
depara = bases.pegar_depara()
for coluna, linhas in depara.items():
    for linha in linhas:
        de = linha['de']
        para = linha['para']
        df = df.withColumn(coluna, when(col(coluna) == de, lit(para)).otherwise(col(coluna)))

# Colunas desejadas para processamento adicional
colunas_desejadas = ['cnpj', 'cnpj_basico', 'identificador_matriz_filial', 'situacao_cadastral',
                     'data_situacao_cadastral', 'data_de_inicio_atividade', 'cnae_fiscal_principal',
                     'uf', 'município']

# Manipulação adicional do DataFrame
cond_row_number = Window.orderBy(F.lit(1))
df = (df.withColumn('data_situacao_cadastral', to_date(col('data_situacao_cadastral'), 'yyyyMMdd'))
      .filter((col('data_situacao_cadastral') >= '2023-01-01')
              & (upper(col('uf')).isin('SP'))
              & (col('situacao_cadastral') == 'ATIVA'))
      .withColumn('cnpj', concat(col('cnpj_basico'), col('cnpj_ordem'), col('cnpj_dv')))
      .select(colunas_desejadas)
      .withColumn("row_number", F.row_number().over(cond_row_number))
      .limit(10_000)
      .cache())

# Contagem de linhas do DataFrame
quantidade_de_linhas = df.count()

# Salvamento de dados no banco de dados em chunks
voltas = 1
for x in range(0, quantidade_de_linhas + 1, chunk):
    inicio = x + 1
    fim = inicio + chunk - 1
    if inicio < quantidade_de_linhas:
        modo = 'overwrite' if voltas == 1 else 'append'
        voltas += 1
        print(f'Salvando de {inicio} até {fim}: ', end='')
        bases.salvar_no_banco(df.filter(col('row_number').between(inicio, fim)).drop('row_number'),
                              'contabilizei', 'estabelecimentos', modo)
