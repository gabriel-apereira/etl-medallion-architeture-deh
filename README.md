# 🐍 Medallion Architecture — ETL em Python (Local + AWS)

Este projeto demonstra como implementar a **Arquitetura Medallion** em duas etapas:  
- **Local:** execução e testes na máquina do desenvolvedor com Python.  
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
- **Python** (ETL local)  
- **SQL** (consultas e análises)  
- **Docker** (ambiente isolado, opcional)  
- **AWS S3, Glue, Athena, Redshift, QuickSight**  

---

## 📂 Estrutura do Projeto

medallion-architecture/ │ ├── 01-bronze-raw/ # Dados brutos (CSV, JSON) │ ├── cep_info.csv │ ├── products.json │ └── users.csv │ ├── 02-silver-validated/ # Dados limpos e validados (Parquet) │ ├── cep_info.parquet │ ├── products.parquet │ └── users.parquet │ ├── 03-gold-enriched/ # Dados prontos para análise │ └── query.sql │ ├── data-access/ # Scripts e notebooks de acesso aos dados │ ├── db.py │ ├── data-view.py │ └── data-view.ipynb │ ├── etl-local/ # Scripts locais de ETL │ ├── get_data.py │ ├── normalize_data.py │ ├── populate_db.py │ └── teste_conexao.py │ └── architecture-diagram.png # Diagrama da arquitetura
