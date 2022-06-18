import sqlite3

def db_conexao():
    con = None
    try:
        con = sqlite3.connect('usuarios.db')
    except sqlite3.error as e:
        print(e)
    return con