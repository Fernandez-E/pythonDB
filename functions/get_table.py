import pandas as pd
import sqlite3
from queries.build_entire_tabel_query import build_table_query

def get_table(
        database_name:str,
        table_name:str
) -> pd.DataFrame:
    conn = sqlite3.connect(database_name)

    query = build_table_query(table_name)

    df = pd.read_sql_query(query, conn)

    return df
