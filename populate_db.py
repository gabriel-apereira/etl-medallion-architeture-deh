from db import DB
import pandas as pd
import os

db = DB(
    server="localhost\\SQLEXPRESS", 
    database="ETL_DB"
)
   

for file in os.listdir("silver"):
    df = pd.read_parquet(f"silver/{file}")

    db.create_table(
        file.replace(".parquet", ""), 
        df.columns.tolist()
    )

    db.insert_data(
        file.replace(".parquet", ""), 
        df
    )