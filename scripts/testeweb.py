import requests
from bs4 import BeautifulSoup

# URL da página que você quer extrair a informação
url = "https://www.contabilizei.com.br/contabilidade-online/quanto-tempo-leva-para-abrir-uma-empresa/?utm_device=c&utm_term=&utm_source=google&utm_medium=cpc&utm_campaign=%5BMAX%5D_Performance_RMKT_Vendas&hsa_cam=20859898068&hsa_grp=&hsa_mt=&hsa_src=x&hsa_ad=&hsa_acc=1466761651&hsa_net=adwords&hsa_kw=&hsa_tgt=&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwlN6wBhCcARIsAKZvD5jvTi4-tapqzrFGQbO54HZ98-j-14qVGzmvx8epFYjzrqiXfiv2HXwaAm_rEALw_wcB#quanto-tempo-demora-para-abrir-uma-empresa"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Faz o parsing do HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra o elemento que contém a informação desejada
    elemento = soup.find(text=lambda text: "São Paulo (SP):" in str(text))
    
    # Se o elemento for encontrado, imprime o texto
    if elemento:
        print(elemento.strip())  # Remove espaços em branco em excesso
    else:
        print("Informação não encontrada.")
else:
    # Se a requisição falhar, imprime uma mensagem de erro
    print("Falha ao acessar a página:", response.status_code)
