import requests
from bs4 import BeautifulSoup

# URL da página para extrair a informação
url = "https://www.contabilizei.com.br/contabilidade-online/documentacao-para-abrir-empresa-saiba-o-que-e-solicitado-durante-o-processo/"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Faz o parsing do HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra todos os parágrafos da página
    paragrafos = soup.find_all('p')
    
    # Procura dentro dos parágrafos o conteúdo desejado
    for paragrafo in paragrafos:
        if "documentos necessários para abrir uma empresa são:" in paragrafo.get_text():
            texto_apos_elemento = paragrafo.find_next_sibling().get_text()
            print(texto_apos_elemento)
            break
    else:
        print("Texto não encontrado.")
else:
    # Se a requisição falhar, imprime uma mensagem de erro
    print("Falha ao acessar a página:", response.status_code)
