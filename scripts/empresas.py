# Importações de bibliotecas necessárias
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from caminho import ProjetoFiap  # Módulo personalizado para manipulação de caminhos
import os

# Definição da pasta contendo os arquivos a serem processados
pasta = 'empresas'

# Inicialização do objeto ProjetoFiap para gerenciamento de caminhos e arquivos
bases = ProjetoFiap()

# Obtendo cabeçalhos corretos para os arquivos da pasta especificada
cabecalhos = bases.pega_cabecalho(pasta)
bases.ajustar_arquivos()  # Ajustando arquivos conforme necessário

# Caminho do arquivo CSV
location = bases.caminho_csv

# Inicialização da sessão Spark com configurações personalizadas
spark = (SparkSession
         .builder
         .appName(pasta)
         .config("spark.driver.extraClassPath", bases.caminho_jar_mysql)
         .getOrCreate())

# Leitura do arquivo CSV para um DataFrame Spark
df = (spark.read.format('csv')
      .option("delimiter", ';')
      .load(location))

# Leitura dos dados dos estabelecimentos tratados para realizar o join
df_estab = bases.lendo_do_banco('contabilizei', 'estabelecimentos')

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

# Colunas desejadas para o DataFrame resultante após o join
colunas_desejadas = [
    'empresas.cnpj_basico',
    'empresas.natureza_juridica',
    'empresas.capital_social_da_empresa',
    'empresas.porte_da_empresa'
]

# Adicionando alias às tabelas
df = df.alias('empresas')
df_estab = df_estab.alias('estab')

# Realização do join entre os DataFrames
df_join = (df
           .join(df_estab, col('empresas.cnpj_basico') == col('estab.cnpj_basico'), 'inner')
           .select(colunas_desejadas))

# Salvamento dos dados resultantes no banco de dados
bases.salvar_no_banco(df_join, 'projeto_fiap', 'empresas')
