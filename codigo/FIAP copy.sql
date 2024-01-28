-- Formatando data
ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'

-- a) Popular a tabela DEPARTAMENTO, inserindo no m�nimo 3 departamentos;
-- b) Escolha 2 departamentos e popule a tabela FUNCIONARIO, inserindo no m�nimo 3 (tr�s) funcion�rios para os departamentos escolhidos.

-- Inserindo Departamento DIRETORIA, resposta comando SQL item a)
INSERT INTO MC_DEPTO(CD_DEPTO, NM_DEPTO, ST_DEPTO) VALUES (SQ_MC_DEPTO.NEXTVAL, 'DIRETORIA', 'A');

-- Inserindo dados funcionarios, resposta comando SQL b)
INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, fl_sexo_biologico, ds_genero, DS_CARGO, VL_SALARIO, ds_email, st_func, DT_CADASTRAMENTO, DT_NASCIMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, NULL, 'Florinda Glup', 'F', 'Feminino', 'PRESIDENTE', 54732, 'florinda@example.com', 'A', TO_DATE('10102000','DDMMYYYY'), TO_DATE('13031960','DDMMYYYY'));

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, 1, 'Silvana Silva', 'CONSELHEIRA', 8498, TO_DATE('18072008','DDMMYYYY'), TO_DATE('11051950','DDMMYYYY'), 'F', 'Feminino', 'silvana@example.com', 'A');

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, 1, 'Thais Luppy', 'CONSELHEIRA', 8765, TO_DATE('31032009','DDMMYYYY'), TO_DATE('21051980','DDMMYYYY'), 'F', 'Feminino', 'thais@example.com', 'A');

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, 1, 'Maria Linda Tunner', 'CONSELHEIRA', 8812, TO_DATE('31031990','DDMMYYYY'), TO_DATE('27121997','DDMMYYYY'), 'F', 'Feminino', 'maria@example.com', 'A');

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, 1, 'Telma Reitzman', 'CONSELHEIRA', 8760, TO_DATE('31082011','DDMMYYYY'), TO_DATE('26121997','DDMMYYYY'), 'F', 'Feminino', 'telma@example.com', 'A');

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, 1, 'Vilma Dias', 'CONSELHEIRA', 8753, TO_DATE('21072010','DDMMYYYY'), TO_DATE('25111997','DDMMYYYY'), 'F', 'Feminino', 'vilma@example.com', 'A');

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, 1, 'Miriam Lee', 'CONSELHEIRA', 8761, TO_DATE('14062011','DDMMYYYY'), TO_DATE('25012002','DDMMYYYY'), 'F', 'Feminino', 'miriam@example.com', 'A');


-- Inserindo Departamento PLANEJAMENTO ESTRATEGICO, resposta comando SQL item a)
INSERT INTO MC_DEPTO(CD_DEPTO, NM_DEPTO, ST_DEPTO) VALUES (SQ_MC_DEPTO.NEXTVAL, 'PLANEJAMENTO ESTRATEGICO', 'A');

-- Inserindo dados funcionarios, resposta comando SQL item b)
INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, fl_sexo_biologico, ds_genero, DS_CARGO, VL_SALARIO, ds_email, st_func, DT_CADASTRAMENTO, DT_NASCIMENTO, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, 1, 'Alice Lopes', 'F', 'Feminino', 'GERENTE PLANEJAMENTO ESTRATEGICO', 11433, 'alice@example.com', 'A', TO_DATE('18051991','DDMMYYYY'), TO_DATE('31072000','DDMMYYYY'), NULL);

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-1, 'Margarida Figueira', 'COORDENADORA PLANEJAMENTO ESTRATEGICO', 9988, TO_DATE('18052005','DDMMYYYY'), TO_DATE('21041990','DDMMYYYY'), 'F', 'Feminino', 'margarida@example.com', 'A', NULL);

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-2, 'Cintia Sousa', 'ANALISTA PLANEJAMENTO', 5600, TO_DATE('23092009','DDMMYYYY'), TO_DATE('04051990','DDMMYYYY'), 'F', 'Feminino', 'cintia@example.com', 'A', NULL);

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-3, 'Fernanda Yamaha', 'ANALISTA PLANEJAMENTO', 5800, TO_DATE('20112006','DDMMYYYY'), TO_DATE('19111970','DDMMYYYY'), 'F', 'Feminino', 'fernanda@example.com', 'A', NULL);

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-4, 'Dinah Honda', 'ANALISTA PLANEJAMENTO', 6800, TO_DATE('20111992','DDMMYYYY'), TO_DATE('11011992','DDMMYYYY'), 'F', 'Feminino', 'dinah@example.com', 'A', NULL);

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-5, 'Samantha Vieira', 'ANALISTA PLANEJAMENTO', 6800, TO_DATE('02101997','DDMMYYYY'), TO_DATE('13091994','DDMMYYYY'), 'F', 'Feminino', 'samantha@example.com', 'I', TO_DATE('22122022','DDMMYYYY'));


-- Inserindo Departamento COMERCIAL, resposta comando SQL item a)
INSERT INTO MC_DEPTO(CD_DEPTO, NM_DEPTO, ST_DEPTO) VALUES (SQ_MC_DEPTO.NEXTVAL, 'COMERCIAL', 'A');

-- Inserindo dados funcionarios, resposta comando SQL item b)
INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, fl_sexo_biologico, ds_genero, DS_CARGO, VL_SALARIO, ds_email, st_func, DT_CADASTRAMENTO, DT_NASCIMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-6, 'Nivia Maria Mello', 'F', 'Feminino', 'ANALISTA FINANCEIRO', 9700, 'nivia@example.com', 'A', TO_DATE('17062006','DDMMYYYY'), TO_DATE('25031991','DDMMYYYY'));

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-7, 'Noemia Lima', 'ANALISTA FINANCEIRO', 9887, TO_DATE('18092012','DDMMYYYY'), TO_DATE('16071992','DDMMYYYY'), 'F', 'Feminino', 'noemia@example.com', 'A', NULL);

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-8, 'Camila Limytz', 'ANALISTA FINANCEIRO', 7543, TO_DATE('18052005','DDMMYYYY'), TO_DATE('12081998','DDMMYYYY'), 'F', 'Feminino', 'camila@example.com', 'A', NULL);

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-9, 'Giovanna Potker', 'ANALISTA FINANCEIRO', 6890, TO_DATE('18052005','DDMMYYYY'), TO_DATE('18071995','DDMMYYYY'), 'F', 'Feminino', 'giovanna@example.com', 'A', NULL);

INSERT INTO MC_FUNCIONARIO(CD_FUNCIONARIO, CD_DEPTO, CD_GERENTE, NM_FUNCIONARIO, DS_CARGO, VL_SALARIO, DT_CADASTRAMENTO, DT_NASCIMENTO, fl_sexo_biologico, ds_genero, ds_email, st_func, DT_DESLIGAMENTO)
VALUES (SQ_MC_FUNCIONARIO.NEXTVAL, SQ_MC_DEPTO.CURRVAL, SQ_MC_FUNCIONARIO.CURRVAL-10, 'Giulia Mendez', 'ANALISTA FINANCEIRO', 8076, TO_DATE('18052005','DDMMYYYY'), TO_DATE('21061999','DDMMYYYY'), 'F', 'Feminino', 'giulia@example.com', 'A', NULL);


-- c) Popular 2 ESTADOS do Brasil. Associe no m�nimo 2 cidades para cada Estado. Para cada cidade, associe no m�nimo 1 bairro e para cada bairro associe 2 endere�os, totalizando no m�nimo 8 endere�os diferentes. 
--Utilize nomes significativos e coerentes, de acordo com a base do Correio. Uma sugest�o de link para acesso seria:  https://buscacepinter.correios.com.br/app/endereco/index.php

-- Resposta do comando SQL item c) 

-- Inserindo dados para Estado 
INSERT INTO MC_ESTADO(SG_ESTADO, NM_ESTADO) 
VALUES ('SP', 'S�o Paulo');

INSERT INTO MC_ESTADO(SG_ESTADO, NM_ESTADO) 
VALUES ('RJ', 'Rio de Janeiro');

INSERT INTO MC_ESTADO(SG_ESTADO, NM_ESTADO) 
VALUES ('MG', 'Campinas');

-- Inserindo dados para Cidade 
INSERT INTO MC_CIDADE(CD_CIDADE, SG_ESTADO, NM_CIDADE, CD_IBGE, NR_DDD) 
VALUES (SQ_MC_CIDADE.NEXTVAL, 'SP', 'S�o Paulo', 123, 11);

INSERT INTO MC_CIDADE(CD_CIDADE, SG_ESTADO, NM_CIDADE, CD_IBGE, NR_DDD) 
VALUES (SQ_MC_CIDADE.NEXTVAL, 'RJ', 'Rio de Janeiro', 456, 21);

INSERT INTO MC_CIDADE(CD_CIDADE, SG_ESTADO, NM_CIDADE, CD_IBGE, NR_DDD) 
VALUES (SQ_MC_CIDADE.NEXTVAL, 'RJ', 'Niteroi', 789, 21);

INSERT INTO MC_CIDADE(CD_CIDADE, SG_ESTADO, NM_CIDADE, CD_IBGE, NR_DDD) 
VALUES (SQ_MC_CIDADE.NEXTVAL, 'MG', 'CAMPINAS', 1110, 21);

-- Inserindo dados para Bairro
INSERT INTO MC_BAIRRO(CD_BAIRRO, CD_CIDADE, NM_BAIRRO, NM_ZONA_BAIRRO) 
VALUES (SQ_MC_BAIRRO.NEXTVAL, 1 , 'Jardins', 'Zona Leste');

INSERT INTO MC_BAIRRO(CD_BAIRRO, CD_CIDADE, NM_BAIRRO, NM_ZONA_BAIRRO) 
VALUES (SQ_MC_BAIRRO.NEXTVAL, 2 ,'Copacabana', 'Zona Sul');

INSERT INTO MC_BAIRRO(CD_BAIRRO, CD_CIDADE, NM_BAIRRO, NM_ZONA_BAIRRO) 
VALUES (SQ_MC_BAIRRO.NEXTVAL, 3 ,'Icara�', 'Zona Oseste');

INSERT INTO MC_BAIRRO(CD_BAIRRO, CD_CIDADE, NM_BAIRRO, NM_ZONA_BAIRRO) 
VALUES (SQ_MC_BAIRRO.NEXTVAL, 4 ,'Cambu�', 'Zona Leste');

-- Inserindo dados para Logradouro
INSERT INTO MC_LOGRADOURO(CD_LOGRADOURO, CD_BAIRRO, NM_LOGRADOURO, NR_CEP) 
VALUES (SQ_MC_LOGRADOURO.NEXTVAL, 1 , 'Rua Oscar Freire', 01426001);

INSERT INTO MC_LOGRADOURO(CD_LOGRADOURO, CD_BAIRRO, NM_LOGRADOURO, NR_CEP) 
VALUES (SQ_MC_LOGRADOURO.NEXTVAL, 1, 'Alameda Lorena', 01424002);

INSERT INTO MC_LOGRADOURO(CD_LOGRADOURO, CD_BAIRRO, NM_LOGRADOURO, NR_CEP) 
VALUES (SQ_MC_LOGRADOURO.NEXTVAL, 2, 'Avenida Atl�ntica', 22010000);

INSERT INTO MC_LOGRADOURO(CD_LOGRADOURO, CD_BAIRRO, NM_LOGRADOURO, NR_CEP) 
VALUES (SQ_MC_LOGRADOURO.NEXTVAL, 2, 'Rua Barata Ribeiro', 22011002);

INSERT INTO MC_LOGRADOURO(CD_LOGRADOURO, CD_BAIRRO, NM_LOGRADOURO, NR_CEP) 
VALUES (SQ_MC_LOGRADOURO.NEXTVAL, 3, 'Rua Gavi�o Peixoto', 24230091);

INSERT INTO MC_LOGRADOURO(CD_LOGRADOURO, CD_BAIRRO, NM_LOGRADOURO, NR_CEP) 
VALUES (SQ_MC_LOGRADOURO.NEXTVAL, 3, 'Avenida Sete de Setembro', 28400000);

INSERT INTO MC_LOGRADOURO(CD_LOGRADOURO, CD_BAIRRO, NM_LOGRADOURO, NR_CEP) 
VALUES (SQ_MC_LOGRADOURO.NEXTVAL, 4, 'Avenida J�lio de Mesquita', 06070156);

INSERT INTO MC_LOGRADOURO(CD_LOGRADOURO, CD_BAIRRO, NM_LOGRADOURO, NR_CEP) 
VALUES (SQ_MC_LOGRADOURO.NEXTVAL, 4, 'Rua Coronel Quirino', 13025004);


-- d) Por fim, cadastre na tabela de ENDERECO FUNCIONARIO os endere�os de 2 funcion�rios � sua escolha. Diversifique os dados escolhendo cidades e estados diferentes. 
--Caso deseje, voc� poder� cadastrar mais de um endere�o por funcion�rio.
-- Resposta do comando SQL item D) 

INSERT INTO MC_END_FUNC(CD_FUNCIONARIO, CD_LOGRADOURO, NR_END, DS_COMPLEMENTO_END, DT_INICIO, DT_TERMINO, ST_END) 
VALUES (1, 1 , 123, 'AP 81', TO_DATE('18052005','DDMMYYYY'), null, 'A');

INSERT INTO MC_END_FUNC(CD_FUNCIONARIO, CD_LOGRADOURO, NR_END, DS_COMPLEMENTO_END, DT_INICIO, DT_TERMINO, ST_END)  
VALUES (2, 4 , 456, 'CASA 1', TO_DATE('18052005','DDMMYYYY'), null, 'A');


-- e) Cadastre no m�nimo 2 CLIENTES PESSOAS F�SICAS e 1 CLIENTES PESSOA J�RIDICA e associe no m�nimo 1 endere�o para cada cliente. Utilize nomes significativos e relevantes.
-- Resposta do comando SQL item E) 

INSERT INTO MC_CLIENTE(NR_CLIENTE, NM_CLIENTE, QT_ESTRELAS, VL_MEDIO_COMPRA, ST_CLIENTE, DS_EMAIL, NR_TELEFONE, NM_LOGIN, DS_SENHA) 
VALUES (SQ_MC_CLIENTE.NEXTVAL, 'Jo�o da Silva', 2, 120, 'A', 'joao@gmail.com', 11959826578, 's.jo�o', 1489);

INSERT INTO MC_CLIENTE(NR_CLIENTE, NM_CLIENTE, QT_ESTRELAS, VL_MEDIO_COMPRA, ST_CLIENTE, DS_EMAIL, NR_TELEFONE, NM_LOGIN, DS_SENHA) 
VALUES (SQ_MC_CLIENTE.NEXTVAL, 'Maria Santos', 4, 160, 'A', 'maria@gmail.com', 11959828964, 's.maria', 2402);

INSERT INTO MC_CLIENTE(NR_CLIENTE, NM_CLIENTE, QT_ESTRELAS, VL_MEDIO_COMPRA, ST_CLIENTE, DS_EMAIL, NR_TELEFONE, NM_LOGIN, DS_SENHA) 
VALUES (SQ_MC_CLIENTE.NEXTVAL, 'Empresa Comercial de Tecnologia Ltda', 5, 560, 'A', 'empresa@hotmail.com', 1198574172, 'c.tecnologia', 6478);

-- f) Cadastre um novo cliente que j� tenha um mesmo login j� criado. 
-- Exiba a instru��o SQL executada para realizar a tarefa e apresente o resultado dessa execu��o).  Foi poss�vel incluir esse novo cliente?  Explique?
-- Resposta do comando SQL item f) 

INSERT INTO MC_CLIENTE(NR_CLIENTE, NM_CLIENTE, QT_ESTRELAS, VL_MEDIO_COMPRA, ST_CLIENTE, DS_EMAIL, NR_TELEFONE, NM_LOGIN, DS_SENHA) 
VALUES (SQ_MC_CLIENTE.NEXTVAL, 'Empresa Alimentos SA', 1, 860, 'A', 'empresarial@hotmail.com', 119857412, 'c.tecnologia', 6478);

-- N�o � possivel incluir o novo cliente, pois decorre da quebra de uma restri��o exclusiva (unique constraint) denominada "UK_MC_CLIENTE_MM_LOGIN" na tabela "MC_CLIENTE". 
--Essa situa��o ocorre quando se tenta adicionar um novo cliente com o mesmo valor no campo "NM_LOGIN" que j� existe na tabela para outro cliente.
-- A restri��o exclusiva tem o prop�sito de assegurar que n�o ocorram duplicatas no campo "NM_LOGIN", todos os valores neste campo devem ser �nicos. 
--Visto que j� existe um cliente com o mesmo nome de login registrado no banco de dados, a tentativa de incluir um novo cliente com o mesmo "NM_LOGIN" infringe essa restri��o, levando � exibi��o do erro ORA-00001.

-- Inserindo dados para cadastro de pessoa f�sica
INSERT INTO MC_CLI_FISICA(NR_CLIENTE, DT_NASCIMENTO, FL_SEXO_BIOLOGICO, DS_GENERO, NR_CPF) 
VALUES (1, TO_DATE('15041993','DDMMYYYY'), 'M', 'Masculino', '123.456.789-00');

INSERT INTO MC_CLI_FISICA(NR_CLIENTE, DT_NASCIMENTO, FL_SEXO_BIOLOGICO, DS_GENERO, NR_CPF) 
VALUES (2, TO_DATE('17082001','DDMMYYYY'), 'F', 'Feminino', '987.654.321-00');

-- Inserindo dados para cadastro de pessoa jur�dica
INSERT INTO MC_CLI_JURIDICA(NR_CLIENTE, DT_FUNDACAO, NR_CNPJ, NR_INSCR_EST) 
VALUES (3, TO_DATE('18051995', 'DDMMYYYY'), '98765432109876', '12345678');

-- Inserindo dados para endere�o cliente
INSERT INTO MC_END_CLI(NR_CLIENTE, CD_LOGRADOURO_CLI, NR_END, DS_COMPLEMENTO_END, DT_INICIO, DT_TERMINO, ST_END) 
VALUES (1, 2, 123, 'AP 75', TO_DATE('19062023','DDMMYYYY'), null, 'A');

INSERT INTO MC_END_CLI(NR_CLIENTE, CD_LOGRADOURO_CLI, NR_END, DS_COMPLEMENTO_END, DT_INICIO, DT_TERMINO, ST_END)
VALUES (2, 8, 456, 'CASA 3', TO_DATE('16072022','DDMMYYYY'), null, 'A');

INSERT INTO MC_END_CLI(NR_CLIENTE, CD_LOGRADOURO_CLI, NR_END, DS_COMPLEMENTO_END, DT_INICIO, DT_TERMINO, ST_END)  
VALUES (3,  7, 965, 'CASA 6', TO_DATE('19042023','DDMMYYYY'), null, 'A');


-- g) Cadastre as seguintes categorias para os produtos: Eletr�nicos, Esporte e Lazer;  Pet Shop.
-- Resposta do comando SQL item g) 

INSERT INTO MC_CATEGORIA_PROD(CD_CATEGORIA, TP_CATEGORIA, DS_CATEGORIA, DT_INICIO, DT_TERMINO, ST_CATEGORIA) 
VALUES (SQ_MC_CATEGORIA.NEXTVAL, 'P', 'Produtos Eletr�nicos',TO_DATE('19042023','DDMMYYYY'), null, 'A');

INSERT INTO MC_CATEGORIA_PROD(CD_CATEGORIA, TP_CATEGORIA, DS_CATEGORIA, DT_INICIO, DT_TERMINO, ST_CATEGORIA) 
VALUES (SQ_MC_CATEGORIA.NEXTVAL, 'P', 'Produtos Esportivos e de Lazer',TO_DATE('19042023','DDMMYYYY'), null, 'A');

INSERT INTO MC_CATEGORIA_PROD(CD_CATEGORIA, TP_CATEGORIA, DS_CATEGORIA, DT_INICIO, DT_TERMINO, ST_CATEGORIA) 
VALUES (SQ_MC_CATEGORIA.NEXTVAL, 'P', 'Produtos de Pets',TO_DATE('19042023','DDMMYYYY'), null, 'A');

-- h) Cadastre 5 produtos e associe as categorias adequadas ao produto.
-- Resposta do comando SQL item h) 

INSERT INTO MC_PRODUTO(CD_PRODUTO, CD_CATEGORIA, NR_CD_BARRAS_PROD, DS_PRODUTO, VL_UNITARIO, TP_EMBALAGEM, ST_PRODUTO, VL_PERC_LUCRO, DS_COMPLETA_PROD) 
VALUES (SQ_MC_PRODUTO.NEXTVAL, 1, 0152795831475, 'Caixa de Som', 1500, 'Pacote', 'A', 0.12, 'Caixa de som de alta qualidade.');

INSERT INTO MC_PRODUTO(CD_PRODUTO, CD_CATEGORIA, NR_CD_BARRAS_PROD, DS_PRODUTO, VL_UNITARIO, TP_EMBALAGEM, ST_PRODUTO, VL_PERC_LUCRO, DS_COMPLETA_PROD) 
VALUES (SQ_MC_PRODUTO.NEXTVAL, 2, 0152795831476, 'Bola de Futebol', 50, 'Unidade', 'A', 0.10, 'Bola de futebol oficial.');

INSERT INTO MC_PRODUTO(CD_PRODUTO, CD_CATEGORIA, NR_CD_BARRAS_PROD, DS_PRODUTO, VL_UNITARIO, TP_EMBALAGEM, ST_PRODUTO, VL_PERC_LUCRO, DS_COMPLETA_PROD) 
VALUES (SQ_MC_PRODUTO.NEXTVAL, 3, 0152795831477, 'Ra��o para C�es', 30, 'Pacote', 'A', 0.15, 'Ra��o de alta qualidade.');

INSERT INTO MC_PRODUTO(CD_PRODUTO, CD_CATEGORIA, NR_CD_BARRAS_PROD, DS_PRODUTO, VL_UNITARIO, TP_EMBALAGEM, ST_PRODUTO, VL_PERC_LUCRO, DS_COMPLETA_PROD) 
VALUES (SQ_MC_PRODUTO.NEXTVAL, 1, 0152795831478, 'Fone de Ouvido', 200, 'Unidade', 'A', 0.10, 'Fones de ouvido premium.');

INSERT INTO MC_PRODUTO(CD_PRODUTO, CD_CATEGORIA, NR_CD_BARRAS_PROD, DS_PRODUTO, VL_UNITARIO, TP_EMBALAGEM, ST_PRODUTO, VL_PERC_LUCRO, DS_COMPLETA_PROD) 
VALUES (SQ_MC_PRODUTO.NEXTVAL, 1, 0152795831479, 'Mouse Sem Fio', 80, 'Unidade', 'A', 0.15, 'Mouse de alta precis�o.');

-- i) Cadastre duas categorias para os v�deos: Instala��o do produto e Uso no cotidiano. Voc� � livre para cadastrar outras categorias, caso deseje.
-- Resposta do comando SQL item i) 

INSERT INTO MC_CATEGORIA_PROD(CD_CATEGORIA, TP_CATEGORIA, DS_CATEGORIA, DT_INICIO, DT_TERMINO, ST_CATEGORIA) 
VALUES (SQ_MC_CATEGORIA.NEXTVAL, 'V', 'Instala��o do produto',TO_DATE('12082023','DDMMYYYY'), null, 'A');

INSERT INTO MC_CATEGORIA_PROD(CD_CATEGORIA, TP_CATEGORIA, DS_CATEGORIA, DT_INICIO, DT_TERMINO, ST_CATEGORIA) 
VALUES (SQ_MC_CATEGORIA.NEXTVAL, 'V', 'Uso no cotidiano',TO_DATE('17072023','DDMMYYYY'), null, 'A');

-- j) Cadastre 2 v�deos de produtos na tabela MC_SGV_PRODUTO_VIDEO e associe esses 2 v�deos em um �nico produto j� cadastrado. Associe tamb�m as categorias adequadas ao v�deo.
-- Resposta do comando SQL item j) 

INSERT INTO MC_SGV_PRODUTO_VIDEO(CD_PRODUTO, NR_SEQUENCIA, CD_CATEGORIA, VD_PRODUTO, TP_VIDEO_PROD, ds_path_video_prod, st_video_prod) 
VALUES (1, SQ_MC_SGV_SAC.NEXTVAL, 1 , null, 'Padr�o', 'Video como usar', 'A');

INSERT INTO MC_SGV_PRODUTO_VIDEO(CD_PRODUTO, NR_SEQUENCIA, CD_CATEGORIA, VD_PRODUTO, TP_VIDEO_PROD, ds_path_video_prod, st_video_prod) 
VALUES (1, SQ_MC_SGV_SAC.NEXTVAL, 2 , null, 'Padr�o', 'Video como usar', 'A');

-- k) Por fim, cadastre 2 visualiza��es de v�deos de produtos na tabela MC_SGV_VISUALIZACAO_VIDEO e associe a um cliente a seu crit�rio.
-- Resposta do comando SQL item k) 

INSERT INTO MC_SGV_VISUALIZACAO_VIDEO(cd_visualizacao_video, nr_cliente, cd_produto, nr_sequencia, dt_visualizacao, nr_hora_visualizacao, nr_minuto_video, nr_segundo_video) 
VALUES (1, SQ_MC_SGV_VISUAL_PROD.NEXTVAL, 1, 1, TO_DATE('12082023','DDMMYYYY'), 14, 30, 0);

INSERT INTO MC_SGV_VISUALIZACAO_VIDEO(cd_visualizacao_video, nr_cliente, cd_produto, nr_sequencia, dt_visualizacao, nr_hora_visualizacao, nr_minuto_video, nr_segundo_video) 
VALUES (2, SQ_MC_SGV_VISUAL_PROD.NEXTVAL, 1, 2, TO_DATE('12082023','DDMMYYYY'), 15, 20, 0);

-- Resposta do comando SQL item l)
commit;

-- m) Selecione um espec�fico funcion�rio e atualize o Cargo e aplique 12% de aumento de sal�rio. 
-- -- Resposta do comando SQL item m) 

UPDATE MC_FUNCIONARIO
SET VL_SALARIO = VL_SALARIO * 1.12  -- Aumento de 12%
WHERE cd_funcionario = '1';

-- n) Atualize o nome de um departamento a sua escolha, utilizando como filtro o nome do departamento antes de ser atualizado.
-- Resposta do comando SQL item n) 

UPDATE MC_DEPTO
SET NM_DEPTO = 'SAC'
WHERE cd_depto = '1';

-- o) Atualize a data de nascimento de um cliente pessoa f�sica. Defina a nova data como sendo 18/05/2002.
-- Resposta do comando SQL item o)

UPDATE MC_CLI_FISICA
SET DT_NASCIMENTO = TO_DATE('18052002', 'DDMMYYYY')
WHERE NR_CLIENTE = 1; 

-- p) Desative um funcion�rio colocando o status como I(nativo) e tamb�m a data de desligamento como sendo a data de hoje (sysdate).
-- -- Resposta do comando SQL item p) 

UPDATE MC_FUNCIONARIO
SET ST_FUNC = 'I',
    DT_DESLIGAMENTO = SYSDATE
WHERE CD_FUNCIONARIO = 1;

-- q) Selecione um endere�o de cliente e coloque o status como I(nativo) e preencha a data de t�rmino como sendo a data limite de entrega do trabalho. 
-- Utilize a fun��o to_date para registrar esse novo valor da data.
-- -- Resposta do comando SQL item q)

UPDATE MC_END_ClI
SET ST_END = 'I',
    DT_TERMINO = TO_DATE('10102023', 'DDMMYYYY')
WHERE NR_CLIENTE = 1;

-- r) Tente eliminar um estado que tenha uma cidade cadastrada. Isso foi poss�vel? Justifique o motivo.
-- Resposta do comando SQL item r) 

DELETE from MC_ESTADO
WHERE SG_ESTADO = 'SP'

--N�o � poss�vel excluir o estado 'SP' da tabela 'MC_ESTADO' porque existem restri��es de integridade referencial ou depend�ncias em outras tabelas que est�o vinculadas a este estado. 
--O erro 'ORA-02292' ocorre quando uma tentativa de exclus�o viola a integridade referencial, o que significa que h� registros filhos na tabela 'MC_CIDADE' que dependem do estado 'SP'. 
--Essas restri��es de integridade existem para garantir a consist�ncia dos dados e evitar a remo��o acidental de registros que est�o sendo referenciados em outras partes do banco de dados.

-- s) Selecione um produto e tente atualizar o status do produto com o status X. Isso foi poss�vel? Justifique o motivo.
-- Resposta do comando SQL item s) 

UPDATE MC_PRODUTO
SET ST_PRODUTO = 'X'
WHERE CD_PRODUTO = 1;

--O erro 'ORA-02290' ocorre porque a tentativa de atualiza��o do status do produto para 'X' na tabela 'MC_PRODUTO' viola uma restri��o de verifica��o (CHECK constraint) chamada 'MC_PRODUTO_CK_ST_PROD'. 
--Esta restri��o de verifica��o foi definida para garantir que apenas valores espec�ficos sejam permitidos no campo 'ST_PRODUTO'. Como 'X' n�o � um valor permitido pela restri��o de verifica��o, 
--a tentativa de atualiza��o viola essa regra, resultando no erro. Essas restri��es de verifica��o s�o usadas para garantir a integridade dos dados e manter a consist�ncia das informa��es na tabela.

-- -- Resposta do comando SQL item t) 
commit;