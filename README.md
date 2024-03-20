# Pyspark e MySQL com Docker

Estou criando esse projetinho para ajudar com os estudos de pyspark junto a SQL localmente e sem muitas dificuldades. Para isso utilizei o Docker para rodar dois containers, o primeiro com pyspark e o segundo com MySQL.

Abaixo um passo a passo de como configurar o Docker com os dois containers e deixar ambos na mesma rede para que possam se comunicar. 

### 1 - Criando docker network
Uma Docker network é um recurso que permite a comunicação entre contêineres Docker e entre contêineres e o host ou outras redes externas. Ela fornece isolamento, segurança e controle sobre como os contêineres se comunicam entre si, permitindo a criação de ambientes complexos e distribuídos de forma eficiente.

Resumindo, criaremos para que o container contendo o spark se comunique com o que tem o MySQL. Para isso será criada a network de nome AULA (coloque o nome que achar melhor), com o seguinte comando.

```shell
docker network create FIAP
```

### 2 - Criando container MySQL
Criei um banco MySQL para poder praticar a escrita de dados com pyspark. Abaixo comando que deve ser executado para criar o container com esse banco.

```shell
docker run --name mysql-FIAP -e MYSQL_ROOT_PASSWORD=root -p 3307:3306 -d --network=FIAP mysql
```

Esse comando fara o download de uma imagem MySQL e criara um container de nome mysql-FIAP. Seu computador passara a se comunicar a partir da porta local **3307** com o Docker na porta **3306** e o colocara na network FIAP. Também será criado um usuário de nome root com a senha root, esses parâmetros podem ser alterados.

### 3 - Criando Container Pyspark
Acesse a pasta docker_file com o terminal, dentro dela tem o arquivo docker-compose.yaml (peguei esse arquivo no [LINK](https://github.com/ibqn/pyspark-jupyter/blob/master/docker-compose.yaml)), dentro desse arquivo tem um parâmetro chamado **volume**, optei por apontar para uma pasta na minha maquina local, com isso o Docker consegue consumir os arquivos que eu disponibilizar nessa pasta e a reconhece internamente como **/tmp/arquivos-fiap**, altere para a pasta que desejar, ou use os volumes do Docker se preferir.

Execute o seguinte comando no terminal.

```shell
docker-compose -p pyspark_fiap up -d
```

Com isso será realizado o download de todas as dependências para rodar o pyspark e criara um container de nome **pyspark_fiap** com jupyter notebook na portal local **9999** e no Docker na porta **8888**, além coloca-los na network FIAP.

Caso tenha optado por outro nome de network, altere esse parâmetro no arquivo yaml

```yaml
    networks:
      - FIAP

networks:
  FIAP:
    external: true
```

Feito isso, acesso o container, pegue o token do notebook e use o jupyter no navegador.

Para testar a conexão com o banco de dados utilize o Dbeaver (ou outro software de sua preferência). Em **Server Host** coloque **localhost**, **user** coloque **root** e **senha** coloque **hoot**. Com isso você poderá executar queries no banco MySQL.

Para este projeto foram utilizados os dados de **cnaes**, **empresas** e **estabelecimentos** do site [Dados Abertos]( https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj). A organização das pastas já está no git dentro de **dados**. Para reproduzir esse projeto (caso queira), basta baixar esses arquivos no site, colocar em suas respectivas pastas, extrair e deixar na pasta **csv**, não precisa converter para o formato csv pois o script já faz isso.