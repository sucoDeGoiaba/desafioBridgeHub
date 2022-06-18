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