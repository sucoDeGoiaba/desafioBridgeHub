from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def db_conexao():
    con = None
    try:
        con = sqlite3.connect('usuarios.db')
    except sqlite3.error as e:
        print(e)
    return con

@app.route('/users/', methods=['GET'])
def users():
    con = db_conexao()
    rows = con.execute("SELECT * FROM usuarios")
    usuarios = [
        dict(id=row[0], nome=row[1], email=row[2], telefone=row[3])
        for row in rows.fetchall()
    ]
    return jsonify(usuarios)


@app.route('/user/<id>', methods=['GET'])
def user_id(id):
    con = db_conexao()
    query = con.execute('SELECT * FROM usuarios WHERE id = ?', id)
    usuario = [
        dict(id=row[0], nome=row[1], email=row[2], telefone=row[3])
        for row in query.fetchall()
    ]
    return jsonify(usuario)
    

@app.route('/add_user/', methods=['POST'])
def add_user():
    con = db_conexao()
    nome = request.json['nome']
    email = request.json["email"]
    telefone = request.json["telefone"]

    query = con.execute('INSERT INTO usuarios (nome, email, telefone) VALUES (?, ?, ?)', (nome, email, telefone))
    con.commit()
    return jsonify(query.lastrowid)


@app.route('/edit_user/<id>', methods=['PUT'])
def edit_user(id):
    con = db_conexao()
    nome = request.json['nome']
    email = request.json["email"]
    telefone = request.json["telefone"]
    query = con.execute('UPDATE usuarios SET nome = ?, email = ?, telefone = ? WHERE id = ?', (nome, email, telefone, id))
    con.commit()
    return jsonify(query.lastrowid)
    

if __name__ == '__main__':
    app.run(debug=True)