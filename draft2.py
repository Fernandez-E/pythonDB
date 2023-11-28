import sqlite3
from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_row import insert_one_row, insert_many_rows
from queries.build_entire_tabel_query import build_table_query
import pandas as pd

from functions.get_table import get_table

DB = 'db.db'
TB = 'tabela'

create_db(DB)

create_table(DB, TB, 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , nome VARCHAR(255), idade INTEGER')

insert_many_rows(
    DB, 
    TB, 
    'id, nome, idade', 
    [(1261, 'srydfg', 33), (1266, 'afdfgfds', 333)])