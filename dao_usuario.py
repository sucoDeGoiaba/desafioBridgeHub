class DaoUsuario:
    def __init__(self, db):
        self.db = db

    # Retorna Query para Model
    def show_users(self):
        rows = self.db.execute("SELECT * FROM usuarios")
        return rows