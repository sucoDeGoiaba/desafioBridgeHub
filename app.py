from flask import Flask, jsonify, request
import sqlite3
from model_usuario import Usuario
from db_con import db_conexao

app = Flask(__name__)


@app.route('/users/', methods=['GET'])
def users():
    # Instancia com a model
    inst = Usuario(db_conexao())
    return jsonify(inst.show_users())


@app.route('/user/<id>', methods=['GET'])
def user_id(id):
    inst = Usuario(db_conexao())
    return jsonify(inst.show_users_by_id(id))
    

@app.route('/add_user/', methods=['POST'])
def add_user():
    inst = Usuario(db_conexao())
    nome = request.json['nome']
    email = request.json["email"]
    telefone = request.json["telefone"]
    return jsonify(inst.add_user(nome, email, telefone))


@app.route('/edit_user/<id>', methods=['PUT'])
def edit_user(id):
    con = db_conexao()
    nome = request.json['nome']
    email = request.json["email"]
    telefone = request.json["telefone"]
    query = con.execute('UPDATE usuarios SET nome = ?, email = ?, telefone = ? WHERE id = ?', (nome, email, telefone, id))
    con.commit()
    return jsonify(query.lastrowid)


@app.route('/delete_user/', methods=['DELETE'])
def delete_user():
    con = db_conexao()
    id = str(request.json['id'])
    query = con.execute('DELETE FROM usuarios WHERE ID = ?', id)
    con.commit()
    return jsonify(query.lastrowid)


if __name__ == '__main__':
    app.run(debug=True)