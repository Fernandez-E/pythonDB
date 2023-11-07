import sqlite3

def insert_one_row(
        database_name:str,
        table_name:str,
        columns_name:str,
        values: str
) -> None:
    
    """ Insert one row
    Args:
        database_name (str): A database's name    
        table_name (str): A table's name  
        columns (str): Columns query 
        columns_name (str): Columns to insert values
        values (str): 

    """
    conn = sqlite3.connect(f'{database_name}')
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {table_name} ({columns_name}) VALUES ({values})    
    """)

    conn.commit()
    conn.close()