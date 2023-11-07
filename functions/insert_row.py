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

        Example:
        ```{python}
        insert_one_row (
            'test.db', 
            'tabela', 
            'id, name, age',
            '1, "Eric", 28'
        )
        ```

    """
    conn = sqlite3.connect(f'{database_name}')
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {table_name} ({columns_name}) VALUES ({values})    
    """)

    conn.commit()
    conn.close()


def insert_many_rows(
        database_name:str,
        table_name:str,
        columns_name:str,
        values_list: list
) -> None:
    
    """ Insert rows
    Args:
        database_name (str): A database's name    
        table_name (str): A table's name  
        columns (str): Columns query 
        columns_name (str): Columns to insert values
        values_list (str):

        Example:
        ```{python}
        insert_one_row (
            'test.db', 
            'tabela', 
            'id, name, age',
            [(1, "Eric", 28)], [(2, "qqqq", 28)]
        )
        ```
    """
        
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    query = f"INSERT INTO {table_name} ({columns_name}) VALUES (?, ?)"

    cursor.executemany(query, values_list)

    conn.commit()
    conn.close()
