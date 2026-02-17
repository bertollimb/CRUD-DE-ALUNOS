# Sistema de Cadastro de Alunos (CRUD) com Flask e SQLite

Este é um projeto de aplicação web desenvolvido em Python utilizando Flask e SQLite, que permite realizar operações completas de CRUD (Create, Read, Update, Delete) em um banco de dados de alunos.

O sistema permite:

- Adicionar novos alunos
- Visualizar lista de alunos
- Atualizar dados de alunos existentes
- Excluir alunos
- Interface web moderna com Bootstrap

---

## Tecnologias utilizadas

- Python 3
- Flask
- SQLite3
- HTML5
- Bootstrap 5
- Jinja2

---

## Estrutura do projeto


projeto/
│
├── app.py # Arquivo principal da aplicação Flask
├── dB.py # Conexão com o banco de dados
├── models.py # Criação da tabela
├── banco.db # Arquivo do banco de dados SQLite
│
└── templates/
    ├── base.html
    ├── index.html
    ├── adicionar.html
    ├── atualizar.html
    └── excluir.html

---

## Funcionalidades

### 1. Criar aluno
Permite adicionar um novo aluno com:

- Nome
- Idade
- Nota

---

### 2. Listar alunos

Exibe todos os alunos cadastrados em formato de tabela.

---

### 3. Atualizar aluno

Permite editar:

- Nome
- Idade
- Nota

Atualização parcial é suportada.

---

### 4. Excluir aluno

Remove permanentemente um aluno do banco de dados.

---

## Banco de dados

O banco utilizado é o SQLite, armazenado no arquivo:

banco.db


A tabela criada:

CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    nota REAL NOT NULL
);

## Arquitetura utilizada

O projeto segue o princípio de separação de responsabilidades:

- db.py → conexão com o banco

models.py → criação das tabelas

app.py → rotas e lógica da aplicação

templates → interface web

## Objetivo do projeto

Este projeto foi desenvolvido com fins educacionais para praticar:

Desenvolvimento backend com Flask

Integração com banco de dados SQLite

Operações CRUD

Arquitetura básica de aplicações web

Organização profissional de código

## Autor

Matheus Bertolli

Software Developer | Backend