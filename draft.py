import sqlite3
from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_row import insert_one_row


create_db('teste2.db')
create_table('teste2.db', 'teste', 'nome')

insert_one_row('teste2.db', 'teste', 'nome', 'EricFernandez')

