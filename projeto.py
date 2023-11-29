import sqlite3
from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_row import insert_many_rows, insert_one_row
from functions.delete_rows import delete_rows
from functions.get_table import get_table

DB = 'veiculos.db'
TB = 'veiculos'

def menu():

    create_db(DB)

    create_table(DB, TB, ("id INTEGER PRIMARY KEY , placa VARCHAR(8) UNIQUE, tipo INTEGER, modelo VARCHAR(60), fabricante VARCHAR(60), ano VARCHAR(10), cor VARCHAR(60), potencia INTEGER, preco INTEGER"))
    print("1 - Registrar novo veículo")
    print("2 - Pesquisar veículos")
    print("3 - Deletar veículo")
    print("4 - Atualizar registro")
    print("5 - Sair")
    op = input(">>> ")
    return int(op)

def tipo_veiculo():
    print("### Tipo do veiculo ###")
    print("1 - Carro")
    print("2 - Motocicleta")
    print("3 - Caminhão")
    print("4 - Ônibus")
    tipo = input("Tipo do veículo: ")
    return tipo

print("#### SISTEMA DE GERENCIAMENTO DE VEÍCULOS ####")

while True:
    op = menu()
    if (op == 5):
        break

    if(op == 1):
        print("### Inserir novo veículo ###")
        tipo = tipo_veiculo()
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        fabricante = input("Marca: ")
        ano = input("Ano de fabricação: ")
        cor = input("Cor: ")
        potencia = input("Potencia: ")
        preco = input("Preço: ")
        insert_one_row(DB, TB, "tipo, placa, modelo, fabricante, ano, cor, potencia, preco", f"{tipo}, '{placa}', '{modelo}', '{fabricante}', '{ano}', '{cor}', {potencia}, {preco}")

    elif(op == 2):
        print("### BUSCAR REGISTRO DE VEÍCULO ###")
        placa = input("Placa: ")
    

    elif(op == 3):
        pass
    elif(op == 4):
        pass
    else:
        print("Finalizando o programa...")
