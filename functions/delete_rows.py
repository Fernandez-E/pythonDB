import sqlite3

def delete_rows(
        database_name:str,
        table_name:str,
        query:str
) -> None:
    """ Delete rows
    Args:
        database_name (str): A database's name    
        table_name (str): A table's name  
        query (str): Query to WHERE clause

    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"""
               DELETE FROM {table_name}
               WHERE {query}
               """)

    conn.commit()

