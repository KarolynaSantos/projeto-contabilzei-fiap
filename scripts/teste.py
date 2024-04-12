import pandas as pd
import boto3
import io

# Inicialize o cliente S3
s3 = boto3.client('s3')

# Especifique o bucket e o caminho do arquivo no S3
bucket_name = 'contabilizei-fiap'
file_key = 'dados/denominacao.xlsx'

# Use o método `get_object` do cliente S3 para obter o objeto
obj = s3.get_object(Bucket=bucket_name, Key=file_key)

# Leia o conteúdo do objeto usando o pandas
df_denominacao = pd.read_excel(io.BytesIO(obj['Body'].read()))


divisoes = df_denominacao['Divisões'].to_list()

denominacoes = df_denominacao['Denominação'].to_list()

novas_denominacoes = []
for x in range(len(divisoes)):
    linha = divisoes[x]
    inicio = int(linha.split(' .. ')[0])
    fim = int(linha.split(' .. ')[-1])

    for y in range(inicio, fim+1):
        novas_denominacoes.append({'divisoes': y ,'denominacoes': denominacoes[x]})

df = pd.DataFrame(novas_denominacoes)

print(df)