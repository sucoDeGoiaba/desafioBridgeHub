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
    

if __name__ == '__main__':
    app.run(debug=True)