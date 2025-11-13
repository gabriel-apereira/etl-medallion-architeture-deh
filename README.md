# 🐍 Medallion Architecture — ETL em Python (Local + AWS)

Este projeto foi desenvolvido como parte do curso do **[Data Engineer Help]**

Este projeto demonstra como implementar a **Arquitetura Medallion**  de duas formas:  
- **Local:** execução e testes na máquina do desenvolvedor com Python, utilizando scripts em python e armazenamento final no SQL Server local.  
- **AWS:** implantação em serviços gerenciados para escalabilidade e análise avançada.  

A arquitetura é dividida em três camadas (Bronze, Silver e Gold), utilizando **S3, Glue, Athena e Redshift** para criar um pipeline robusto de ingestão, transformação e análise de dados.

---

## 🎯 Objetivos
- Armazenar dados brutos (CSV, JSON) de forma segura e escalável  
- Validar e transformar os dados para formatos otimizados (Parquet)  
- Enriquecer os dados para análises e dashboards  
- Utilizar serviços gerenciados da AWS para orquestração e consulta  
- Fornecer um ambiente acessível para análise exploratória e visualização  

---

## 🛠️ Tecnologias Utilizadas
- **Python**  
- **SQL**  
- **AWS S3, Glue, Athena, Redshift, QuickSight**

---

## 📂 Estrutura do Projeto
```
medallion-architecture/
│
├── data/                      # Dados organizados por camadas
│   ├── bronze/                # Camada Bronze: dados brutos
│   │   ├── cep_info.csv
│   │   ├── products.json
│   │   └── users.csv
│   │
│   ├── silver/                # Camada Silver: dados tratados/validados
│   │   ├── cep_info.parquet
│   │   ├── products.parquet
│   │   └── users.parquet
│   │
│   └── gold/                  # Camada Gold: dados prontos para análise
│       └── query.sql
│
├── etl/                       # Scripts de ETL (local)
│   ├── extract/               # Extração
│   │   └── get_data.py
│   │
│   ├── transform/             # Transformação
│   │   ├── normalize_data.py
│   │   └── normalize_data_class.py
│   │
│   ├── load/                  # Carregamento
│   │   └── populate_db.py
│   │
│   ├── utils/                 # Utilitários
│   │   ├── db.py              # Conexão com banco
│   │   ├── data-view.py       # Visualização dos dados
│   │   └── teste_conexao.py   # Teste de conexão
│
└── docs/                      # Documentação e diagramas
    └── architecture-diagram.png
```

## ☁️ Guia Rápido na AWS
- **Bronze**: : Armazene os dados brutos em buckets S3 
- **Silver**: Use AWS Glue para validar e transformar os dados (Parquet)
- **Gold**: Faça queries com Athena diretamente nos dados prontos no S3
- **Data Access**: Importe os dados no Amazon Redshift e conecte ao Amazon QuickSight para dashboards

## 📸 Diagrama

<img width="1194" height="1572" alt="architecture-diagram" src="https://github.com/user-attachments/assets/2be4cbbb-8519-48e9-b4f3-91f8580d9815" />

