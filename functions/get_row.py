import sqlite3

def get_vehicle(database:str, table:str, placa:str):
    conn = sqlite3.connect("veiculos.db")
    cursor = conn.cursor()

    cursor.execute(f"""
                SELECT * FROM veiculos WHERE placa = '{placa}'
               """)

    for item in cursor.fetchall():
        print(f"Resultado da busca: {item[4]} {item[3]} {item[6]}, {item[7]}cv, Ano {item[5]} - R${item[8]}")