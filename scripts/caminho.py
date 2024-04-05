import json 
import os
import pymysql
from pyspark.sql import SparkSession

class ProjetoFiap():
    
    def __init__(self):

        # Define o caminho geral onde estão localizados os arquivos
        self.caminho_geral = '/tmp/arquivos-fiap/'
        # Caminho para o arquivo JSON que contém o layout dos dados
        caminho_json = self.caminho_geral + 'config/layout_para_os_dados.json'
        # Caminho para o JAR do conector MySQL
        self.caminho_jar_mysql = self.caminho_geral + 'config/d84e8af7_2ed8_4573_9232_9493078f73c4-mysql_connector_java_8_0_13-4ac45.jar'

        # Lê o arquivo JSON e carrega seu conteúdo em uma variável
        with open(caminho_json, 'r', encoding="utf-8") as f:
            self.arquivo_json = json.load(f)

        # Caminho para o arquivo de credenciais
        caminho_credenciais = self.caminho_geral + 'config/credenciais.env'

        # Cria uma sessão Spark
        self.spark = (SparkSession
                .builder
                .appName('def_apoio')
                .config("spark.driver.extraClassPath", self.caminho_jar_mysql)
                .getOrCreate()
                )

         # Tenta abrir e ler o arquivo de credenciais
        try:
            with open(caminho_credenciais, 'r', encoding="utf-8") as f:
                self.arquivo_credenciais = f.read()
        except:
            pass

    @staticmethod
    def criar_database(database, host, user, password):
        # Conexão com o servidor MySQL
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password
        )
        
        try:
            with connection.cursor() as cursor:
                # Criação do banco de dados se não existir
                create_database_query = f"CREATE DATABASE IF NOT EXISTS {database}"

                cursor.execute(create_database_query)
        
            # Confirmação das alterações
            connection.commit()
        
        finally:
            # Fechamento da conexão
            connection.close()

    @staticmethod
    def credenciais(arquivo):
        # Itera sobre as linhas do arquivo de credenciais
        for linha in arquivo.split('\n'):
            # Divide cada linha em chave e valor
            valores = linha.split('=')
            chave = valores[0].strip() # Remove espaços em branco em excesso
            valor = valores[1].strip() # Remove espaços em branco em excesso
        
            # Define as variáveis de ambiente com as credenciais
            os.environ[chave] = valor
        
    
    def pega_cabecalho(self, chave):
        # Obtém o caminho para o CSV com base na chave

        self.chave = chave

        self.caminho_csv = self.caminho_geral + f'dados/{self.chave}/csv/'

        # Obtém as colunas do arquivo JSON
        colunas = [x['coluna'] for x in self.arquivo_json[chave][0]['colunas']]
        return colunas

    def pegar_depara(self):
        # Obtém o mapeamento de colunas de_para do arquivo JSON
        dicionario = {}
        for x in self.arquivo_json[self.chave][0]['colunas']:
            if 'de_para' in x.keys():
        
                linha = x
                dicionario[linha['coluna']] = linha['de_para']

        return dicionario

    def ajustar_arquivos(self):
        # Renomeia arquivos CSV em um diretório específico
        location = self.caminho_csv
        
        arquivos = os.listdir(location)
        
        for arquivo in arquivos:
            
            nome_antigo = os.path.join(location, arquivo)
            nome_novo = arquivo.split('.')
            nome_novo[-1] = 'csv'
            nome_novo = '.'.join(nome_novo)
            nome_novo = os.path.join(location, nome_novo)
            os.rename(nome_antigo, nome_novo)

    def salvar_no_banco(self, df, database, tabela, modo='overwrite'):

        ProjetoFiap.credenciais(self.arquivo_credenciais)
        hostname = os.getenv("HOST-MYSQL")
        username = os.getenv("USER-MYSQL")
        password = os.getenv("PASSWORD-MYSQL")
        port = os.getenv("PORT-MYSQL")

        ProjetoFiap.criar_database(database, hostname, username, password)
        

        (
            df
            .write
            .format("jdbc")
            .option("url", f"jdbc:mysql://{hostname}:{port}/{database}?useUnicode=true&characterEncoding=UTF-8&useSSL=false") \
            .option("driver", "com.mysql.jdbc.Driver")
            .option("dbtable", tabela)
            .option("user", username)
            .option("password", password)
            .mode(modo)
            .save()
        )

        print(f'Tabela {tabela}, salva no banco')

    def lendo_do_banco(self, database, tabela):

        ProjetoFiap.credenciais(self.arquivo_credenciais)
        hostname = os.getenv("HOST-MYSQL")
        username = os.getenv("USER-MYSQL")
        password = os.getenv("PASSWORD-MYSQL")
        port = os.getenv("PORT-MYSQL")

        ProjetoFiap.criar_database(database, hostname, username, password)
        

        df = (
            self.spark
            .read
            .format("jdbc")
            .option("url", f"jdbc:mysql://{hostname}:{port}/{database}?useUnicode=true&characterEncoding=UTF-8&useSSL=false")
            .option("driver", "com.mysql.jdbc.Driver")
            .option("dbtable", tabela)
            .option("user", username)
            .option("password", password)
            .load()
        )

        return df
        