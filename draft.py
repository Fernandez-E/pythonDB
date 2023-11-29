import sqlite3
from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_row import insert_one_row, insert_many_rows
from queries.build_entire_tabel_query import build_table_query
import pandas as pd

from functions.get_table import get_table


conn = sqlite3.connect("veiculos.db")
cursor = conn.cursor()

cursor.execute(f"""
                SELECT * FROM veiculos WHERE cor = "Preto" 
               """)


for item in cursor.fetchall():
    print(f"Resultado da busca: {item[4]} {item[3]} {item[6]}, {item[7]}cv, Ano {item[5]} - R${item[8]}")



















DB = 'database3.db'
TB = 'tabela'

get_table(DB, TB)

#############################
import sqlite3

conn = sqlite3.connect("database3.db")
cursor = conn.cursor()

cursor.execute("""
               DELETE FROM tabela
               WHERE nome = 'ccc'
               """)

conn.commit()

create_db('bd.db')

create_table('bd.db', 'tabela', )


conn = sqlite3.connect('database3.db')
cursor = conn.cursor()

cursor.executemany(
    """
    INSERT INTO tabela (nome, idade) VALUES (?, ?)
    """,
    [('AAA', 33),
    ('BBB', 55),
    ('ccc', 11)]
)

conn.commit()

insert_many_rows(
    DB, 
    TB, 
    'id, nome', 
    [(1, 'srydfg')])

df = pd.read_sql_query(
    """
    SELECT * FROM tabela
    """
    ,conn
)

df = pd.read_sql_query(
    build_table_query('tabela'), conn
)

DB = 'database3.db'
TB = 'tabela2'

create_db(DB)
create_table(DB, TB, 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , idade INTEGER')

insert_one_row(
            DB, 
            TB, 
            'idade',
            28)

from functions.delete_rows import delete_rows

delete_rows('database3.db', 'tabela', 'nome = "AAA"')

### JOIN

