import sqlite3
from schema_usuario import SchemaUsuario
from dao_usuario import DaoUsuario


class Usuario:
    def __init__(self, db):
        self.dao = DaoUsuario(db)

    def show_users(self):
        res = self.dao.show_users()
        # Trata dados recebidos
        usuarios = [
            dict(id=res[0], nome=res[1], email=res[2], telefone=res[3])
            for res in res.fetchall()
        ]
        # E retorna para a controller (app)
        return usuarios

    def show_users_by_id(self, id):
        res = self.dao.show_users_by_id(id)
        usuario = [
        dict(id=res[0], nome=res[1], email=res[2], telefone=res[3])
            for res in res.fetchall()
        ]
        return usuario
        
    def add_user(self, nome, email, telefone):
        res = self.dao.add_user(nome, email, telefone)
        return res

    def edit_user(self, id, nome, email, telefone):
        res = self.dao.edit_user(id, nome, email, telefone)
        return res