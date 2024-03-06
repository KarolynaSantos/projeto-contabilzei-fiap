import json 
import os 

class ProjetoFiap():
    
    def __init__(self):

        self.caminho_geral = '/tmp/arquivos-fiap/'
        caminho_json = self.caminho_geral + 'config/layout_para_os_dados.json'

        with open(caminho_json, 'r', encoding="utf-8") as f:
            self.arquivo_json = json.load(f)

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