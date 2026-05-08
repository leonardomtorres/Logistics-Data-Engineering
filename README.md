# Logistics Data Engineering Pipeline

Pipeline de Engenharia de Dados para processamento e análise logística utilizando Python, Pandas, PostgreSQL, Docker e Power BI.

## Arquitetura do Pipeline

## Objetivo

Este projeto simula um pipeline moderno de Engenharia de Dados aplicado ao contexto logístico, contemplando ingestão, transformação, armazenamento e análise de dados.

O pipeline foi desenvolvido com foco em:
- Organização de ambientes de dados
- Processos ETL
- Integração Python + PostgreSQL
- Containerização com Docker
- Estrutura escalável para análises futuras

- ## Stack Tecnológica

| Categoria | Tecnologias |
|---|---|
| Linguagem | Python |
| Processamento | Pandas, NumPy |
| Banco de Dados | PostgreSQL |
| ORM/Conexão | SQLAlchemy, psycopg2 |
| Containerização | Docker, Docker Compose |
| Visualização | Power BI |
| Versionamento | Git, GitHub |


Logistics Data Engineering

Pipeline de Engenharia de Dados voltada para análise logística utilizando Python, Pandas, PostgreSQL e Docker.

Visão Geral do Projeto

Este projeto foi desenvolvido com o objetivo de simular um ambiente real de Engenharia de Dados, aplicando conceitos de ingestão, transformação, armazenamento e preparação de dados logísticos.

A proposta do projeto é construir uma pipeline organizada e escalável para tratamento de dados logísticos utilizando tecnologias amplamente utilizadas pelo mercado.

Objetivos
Estruturar um projeto de Engenharia de Dados de forma profissional
Trabalhar com ingestão e tratamento de dados CSV
Utilizar Python e Pandas para transformação de dados
Utilizar PostgreSQL como banco de dados relacional
Executar o banco em containers Docker
Organizar o ambiente utilizando Docker Compose
Criar uma estrutura preparada para futuras automações ETL
Versionar todo o projeto com Git e GitHub


Tecnologias Utilizadas
Python
Pandas
NumPy
PostgreSQL
SQLAlchemy
psycopg2-binary
Docker
Docker Compose
Jupyter Notebook
Git
GitHub

FLUXOGRAMA 

<img width="1536" height="1024" alt="fluxograma" src="https://github.com/user-attachments/assets/07c7e8d0-558f-40d6-b4da-e45ef903dac2" />  



Estrutura do Projeto  

<img width="1917" height="1042" alt="Estrutura" src="https://github.com/user-attachments/assets/0c4d3287-4d2a-4b5c-9e9b-b9a64fe40ac9" />  

INSIGHT PowerBI do transporte que gera mais lucro  

<img width="1916" height="1002" alt="powerbi" src="https://github.com/user-attachments/assets/4def4248-3f86-48b2-aabf-b784f5c6818d" />  




Fluxo da Pipeline  
Dataset CSV  
     ↓  
Python + Pandas  
     ↓  
Tratamento e Limpeza  
     ↓  
PostgreSQL (Docker)  
     ↓  
Análises e consultas SQL  
Configuração do Ambiente  
1. Clonar repositório
git clone <url-do-repositorio>
2. Criar ambiente virtual
python -m venv venv
3. Ativar ambiente virtual
Windows
.\venv\Scripts\activate  
Instalação das Dependências
pip install -r requirements.txt  
Executando PostgreSQL com Docker
docker compose up -d

Verificar containers:

docker ps
Principais Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos importantes de Engenharia de Dados:

Estruturação de projetos profissionais  
Criação de ambientes isolados com venv  
Manipulação e limpeza de dados com Pandas  
Integração Python + PostgreSQL  
Conexão utilizando SQLAlchemy  
Containers Docker para banco de dados  
Organização de pipeline de dados  
Versionamento com Git e GitHub  


Autor

Projeto desenvolvido por Leonardo Marchetti Torres.
