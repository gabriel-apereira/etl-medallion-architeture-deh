import pyodbc

server = 'localhost\\SQLEXPRESS'
database = 'teste'

# Conexão com autenticação do Windows
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Cliente")
for row in cursor.fetchall():
    print(row)