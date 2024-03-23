import json 
import os
import pymysql

class ProjetoFiap():
    
    def __init__(self):

        self.caminho_geral = '/tmp/arquivos-fiap/'
        caminho_json = self.caminho_geral + 'config/layout_para_os_dados.json'
        self.caminho_jar_mysql = self.caminho_geral + 'config/d84e8af7_2ed8_4573_9232_9493078f73c4-mysql_connector_java_8_0_13-4ac45.jar'

        with open(caminho_json, 'r', encoding="utf-8") as f:
            self.arquivo_json = json.load(f)

        caminho_credenciais = self.caminho_geral + 'config/credenciais.env'

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
                # Criação do banco de dados
                create_database_query = f"CREATE DATABASE IF NOT EXISTS {database}"

                cursor.execute(create_database_query)
        
            # Confirmação das alterações
            connection.commit()
            print(f"Banco de dados '{database}' criado com sucesso!")
        
        finally:
            # Fechamento da conexão
            connection.close()

    @staticmethod
    def credenciais(arquivo):
        for linha in arquivo.split('\n'):
            valores = linha.split('=')
            chave = valores[0].strip()
            valor = valores[1].strip()
        
            os.environ[chave] = valor
        
    
    def pega_cabecalho(self, chave):

        self.chave = chave

        self.caminho_csv = self.caminho_geral + f'dados/{self.chave}/csv/'

        colunas = [x['coluna'] for x in self.arquivo_json[chave][0]['colunas']]
        return colunas

    def pegar_depara(self):
        dicionario = {}
        for x in self.arquivo_json[self.chave][0]['colunas']:
            if 'de_para' in x.keys():
        
                linha = x
                dicionario[linha['coluna']] = linha['de_para']

        return dicionario

    def ajustar_arquivos(self):
        location = self.caminho_csv
        
        arquivos = os.listdir(location)
        
        for arquivo in arquivos:
            
        
            nome_antigo = os.path.join(location, arquivo)
            nome_novo = arquivo.split('.')
            nome_novo[-1] = 'csv'
            nome_novo = '.'.join(nome_novo)
            nome_novo = os.path.join(location, nome_novo)
            os.rename(nome_antigo, nome_novo)

    def salvar_no_banco(self, df, database, tabela):

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
            .mode("overwrite")
            .save()
        )

        print(f'Tabela {tabela}, salva no banco')
        