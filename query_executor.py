import sqlite3
import pandas as pd

def execute_query(sql: str):
    try:
        conn = sqlite3.connect("ecommerce.db")
        df = pd.read_sql_query(sql, conn)
        return df.to_dict(orient="records")
    except Exception as e:
        return f"[SQL ERROR] {str(e)}"