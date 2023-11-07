import sqlite3
from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_row import insert_one_row

DB = 'database3.db'
TB = 'tabela'

create_db(DB)
create_table(DB, TB, 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , nome VARCHAR(255), idade INTEGER')

insert_one_row(
            DB, 
            TB, 
            'nome, idade',
            '"Eric", 28')