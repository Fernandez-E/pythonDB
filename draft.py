import sqlite3
from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_row import insert_one_row, insert_many_rows


DB = 'database3.db'
TB = 'tabela'

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

insert_many_rows(DB, TB, 'nome, idade', [('srydfg', 22), ('dfjgur', 55)])
















DB = 'database3.db'
TB = 'tabela'

create_db(DB)
create_table(DB, TB, 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , nome VARCHAR(255), idade INTEGER')

insert_one_row(
            DB, 
            TB, 
            'nome, idade',
            '"Eric", 28')