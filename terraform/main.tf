# usar terraform init no terminal na primeira vez que for rodar

# terraform plan para mostrar tudo que vai ser executado e se tá correto
# terraform apply para subir os parametros no ambiente
# terraform destroy para derrubar o ambiente

# ___________________________________
# |  Criado por: Karolyna Fernanda  |
# |  Data de criação: 12-03-2023    |
# |  Objetivo: Subir ambiente AWS   |
# ___________________________________

#================================================

# Setar qual provedor sera usado
# passar qual região deve ser alocado o provider

provider "aws" {
    region = "us-east-1"
}

#================================================

# Criando VPC
resource "aws_vpc" "vpc_prd" {
    cidr_block = "10.0.0.0/16"
    enable_dns_hostnames = true
    tags = {
        Name = "vpc-terraform-contabilizei"
    }
}
#================================================

# criando as subnets

# subnet_a
resource "aws_subnet" "public_subnet_a" {
    vpc_id = aws_vpc.vpc_prd.id
    cidr_block = "10.0.1.0/24"
    availability_zone = "us-east-1a"
    tags = {
        Name = "subnet-a"
    }
}

# Subnet_b
resource "aws_subnet" "pulic_subnet_b" {
    vpc_id = aws_vpc.vpc_prd.id
    cidr_block = "10.0.2.0/24"
    availability_zone = "us-east-1b"
    tags = {
        Name = "subnet-b"
    }
}

# Subnet_c
resource "aws_subnet" "public_subnet_c" {
    vpc_id = aws_vpc.vpc_prd.id
    cidr_block = "10.0.3.0/24"
    availability_zone = "us-east-1c"
    tags = {
        Name = "subnet-c"
    }
}

# Subnet_d
resource "aws_subnet" "public_subnet_d" {
    vpc_id = aws_vpc.vpc_prd.id
    cidr_block = "10.0.4.0/24"
    availability_zone = "us-east-1d"
    tags = {
        Name = "subnet-d"
    }
}

# Subnet_e
resource "aws_subnet" "public_subnet_e" {
    vpc_id = aws_vpc.vpc_prd.id
    cidr_block = "10.0.5.0/24"
    availability_zone = "us-east-1e"
    tags = {
        Name = "subnet-e"
    }
}

# Subnet_f
resource "aws_subnet" "public_subnet_f" {
    vpc_id = aws_vpc.vpc_prd.id
    cidr_block = "10.0.6.0/24"
    availability_zone = "us-east-1f"
    tags = {
        Name = "subnet-f"
    }
}

#================================================

# Criando internt Gateway
resource "aws_internet_gateway" "internet_gateway" {
    vpc_id = aws_vpc.vpc_prd.id
    tags = {
        Name = "ig_contabilizei"
    }
}

#================================================

# Criando tabela de rotas 

resource "aws_route_table" "tabela_de_rota_contabilizei" {
    vpc_id = aws_vpc.vpc_prd.id
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.internet_gateway.id
    }
    tags = {
        Name = "tabela_rota_contabilizei"
    }
}

#================================================

# Associando subnet a tabela de rotas
resource "aws_route_table_association" "subnet_rota_1" {
  subnet_id = aws_subnet.public_subnet_a.id
  route_table_id = aws_route_table.tabela_de_rota_contabilizei.id
}

resource "aws_route_table_association" "subnet_rota_2" {
  subnet_id = aws_subnet.pulic_subnet_b.id
  route_table_id = aws_route_table.tabela_de_rota_contabilizei.id
}

resource "aws_route_table_association" "subnet_rota_3" {
  subnet_id = aws_subnet.public_subnet_c.id
  route_table_id = aws_route_table.tabela_de_rota_contabilizei.id
}

resource "aws_route_table_association" "subnet_rota_4" {
  subnet_id = aws_subnet.public_subnet_d.id
  route_table_id = aws_route_table.tabela_de_rota_contabilizei.id
}

resource "aws_route_table_association" "subnet_rota_5" {
  subnet_id = aws_subnet.public_subnet_e.id
  route_table_id = aws_route_table.tabela_de_rota_contabilizei.id
}

resource "aws_route_table_association" "subnet_rota_6" {
  subnet_id = aws_subnet.public_subnet_f.id
  route_table_id = aws_route_table.tabela_de_rota_contabilizei.id
}

#================================================

# Criando grupo de seguranca
resource "aws_security_group" "security_group_contabilizei" {
    vpc_id = aws_vpc.vpc_prd.id
    description = "contabilizei-sg"
    ingress {
        protocol = "tcp"
        from_port = "3306"
        to_port = "3306"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        protocol = "tcp"
        from_port = "3306"
        to_port = "3306"
        cidr_blocks = ["0.0.0.0/0"]
    }
    tags = {
        Name = "security-group-contabilizei"
    }
}

#================================================

# Criar RDS
# Criar Grupo de subnet para o RDS

resource "aws_db_subnet_group" "subgroup_contabilizei" {
    subnet_ids = [ aws_subnet.public_subnet_a.id
    ,aws_subnet.pulic_subnet_b.id
    ,aws_subnet.public_subnet_c.id
    ,aws_subnet.public_subnet_d.id
    ,aws_subnet.public_subnet_e.id
    ,aws_subnet.public_subnet_f.id]
    tags = {
        Name = "db-subnet"
    }
}

# Criar DB RDS

resource "aws_db_instance" "rds_contabilizei" {
  allocated_storage    = 10
  db_name              = "contabilizei"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t3.micro"
  username             = "karol"
  password             = "contabilizei2024"
  db_subnet_group_name = aws_db_subnet_group.subgroup_contabilizei.name
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
  identifier = "fiap-contabilizei"
  vpc_security_group_ids = [aws_security_group.security_group_contabilizei.id]
  publicly_accessible = true
  tags = {
    Name = "db-fiap-contabilizei"
  }  
}
