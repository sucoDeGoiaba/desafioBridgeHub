class DaoUsuario:
    def __init__(self, db):
        self.db = db

    # Retorna Query para Model
    def show_users(self):
        rows = self.db.execute("SELECT * FROM usuarios")
        return rows
    
    def show_users_by_id(self, id):
        row = self.db.execute('SELECT * FROM usuarios WHERE id = ?', id)
        return row
