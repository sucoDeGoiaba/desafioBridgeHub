import sqlite3

con = sqlite3.connect("usuarios.db")

cur = con.cursor()
# Dados do usuário: nome, email, telefone
setup_query = """ CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)"""

cur.execute(setup_query)