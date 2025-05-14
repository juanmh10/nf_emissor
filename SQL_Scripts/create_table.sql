CREATE TABLE clientes(
    id serial primary key,
    nome varchar(100) not null,
    cnpj_cpf varchar(14) not null,
    endereco varchar(100) not null,
    email varchar(100) not null,
    telefone varchar(15) not null   
);

CREATE TABLE servicos(
    id serial primary key,
    descicao text,
    preco_unitario decimal(10,2) not null,
    codigo_tributo varchar(10) not null,
);

CREATE TABLE notas_fiscais(
    id serial primary key,
    cliente_id int references clientes(id),
    data_emissao date not null,
    total decimal(10,2) not null,
);

CREATE TABLE itens_nota(
    id serial PRIMARY KEY,
    nota_id int REFERENCES notas_fiscais(id),
    quantidade int NOT NULL,
    valor_unitario decimal(10,2) NOT NULL,
);

