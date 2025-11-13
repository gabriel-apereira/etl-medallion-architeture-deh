import pandas as pd
import sqlalchemy

db_url = (
    "mssql+pyodbc://localhost\\SQLEXPRESS/ETL_DB"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Ler a query do arquivo
with open('gold/query.sql', 'r', encoding='utf-8') as f:
    query = f.read()

# Conectar ao banco de dados e executar a query
engine = sqlalchemy.create_engine(db_url)
with engine.connect() as conn:
    df = pd.read_sql_query(query, conn)

# Visualizar os dados
print(df.head())