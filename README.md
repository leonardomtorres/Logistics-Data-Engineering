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


## Estrutura do Projeto

```bash
logistics-data-engineering/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── analytics/
│
├── scripts/
│   └── etl.py
│
├── sql/
│   └── analysis.sql
│
├── dashboard/
│
├── docker-compose.yml
├── requirements.txt
└── README.md


Isso passa MUITA organização.

---

# Pipeline ETL

Aqui você demonstra maturidade técnica.

```md
## Pipeline ETL

O pipeline executa as seguintes etapas:

1. Extração dos dados CSV
2. Limpeza e padronização
3. Tratamento de valores nulos
4. Transformações analíticas
5. Carga no PostgreSQL
6. Consultas SQL para análise
7. Visualização no Power BI


## Como Executar

### 1. Clonar repositório

```bash
git clone https://github.com/seuusuario/logistics-data-engineering.git
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente

#### Windows
```bash
venv\Scripts\activate
```

#### Linux/Mac
```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Subir PostgreSQL com Docker

```bash
docker compose up -d
```

### 6. Executar pipeline ETL

```bash
python scripts/etl.py
```



























FLUXOGRAMA 

<img width="1536" height="1024" alt="fluxograma" src="https://github.com/user-attachments/assets/07c7e8d0-558f-40d6-b4da-e45ef903dac2" />  



Estrutura do Projeto  

<img width="1917" height="1042" alt="Estrutura" src="https://github.com/user-attachments/assets/0c4d3287-4d2a-4b5c-9e9b-b9a64fe40ac9" />  

INSIGHT PowerBI do transporte que gera mais lucro  

<img width="1916" height="1002" alt="powerbi" src="https://github.com/user-attachments/assets/4def4248-3f86-48b2-aabf-b784f5c6818d" />  





