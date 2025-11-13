import os
import pandas as pd
import pyodbc

class DB:
    def __init__(self, server, database, driver="ODBC Driver 17 for SQL Server"):
        self.server = server
        self.database = database
        self.driver = driver

        # Primeiro garante que a database existe
        self.create_database()

        # Agora conecta já na database
        self.conn = pyodbc.connect(
            f"DRIVER={{{self.driver}}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            "Trusted_Connection=yes;"
        )

    def create_database(self):
        # Conecta no master para poder criar a database
        conn_tmp = pyodbc.connect(
            f"DRIVER={{{self.driver}}};"
            f"SERVER={self.server};"
            "DATABASE=master;"
            "Trusted_Connection=yes;",
            autocommit=True 
        )
        cursor = conn_tmp.cursor()
        cursor.execute(
            f"IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{self.database}') "
            f"CREATE DATABASE {self.database}"
        )
        conn_tmp.commit()
        cursor.close()
        conn_tmp.close()

    def create_table(self, table_name, columns):
        cursor = self.conn.cursor()
        columns_with_types = [f"{col} NVARCHAR(MAX)" for col in columns]
        cursor.execute(
            f"IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table_name}' AND xtype='U') "
            f"CREATE TABLE {table_name} ({', '.join(columns_with_types)})"
        )
        self.conn.commit()
        cursor.close()

    def insert_data(self, table_name, df):
        cursor = self.conn.cursor()
        for _, row in df.iterrows():
            values = [str(v) if v is not None else None for v in row.values]
            placeholders = ', '.join(['?'] * len(values))
            cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", values)
        self.conn.commit()
        cursor.close()

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def select_all_data_from_table(self, table_name, limit=10):
        query = f"SELECT TOP {limit} * FROM {table_name}"
        return self.execute_query(query)

    def close(self):
        self.conn.close()
