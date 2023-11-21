from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_row import insert_many_rows

DB = 'join.db'

create_db('join.db')

create_table(
    'join.db',
    'nome',
    'id_nome INTEGER PRIMARY KEY, nome VARCHAR(255) NOT NULL, id_idade INT'
)

create_table(
    'join.db',
    'idade',
    'id_idade INTEGER PRIMARY KEY, idade INTEGER NOT NULL, data DATE'
)

insert_many_rows(
    DB,
    'nome',
    'id_nome, nome, id_idade',
    [
        (1, "Eric", 7),
        (2, "Nathália", 16)
    ]
)

insert_many_rows(
    DB,
    'idade',
    'id_idade, idade, data',
    [
        (1, 28, '2000-01-01'),
        (7, 20, '1999-09-04')
    ]
)