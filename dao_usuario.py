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

    def add_user(self, nome, email, telefone):
        self.db.execute('INSERT INTO usuarios (nome, email, telefone) VALUES (?, ?, ?)', (nome, email, telefone))
        self.db.commit()
        return 'Usuário adicionado!'

    def edit_user(self, id, nome, email, telefone):
        self.db.execute('UPDATE usuarios SET nome = ?, email = ?, telefone = ? WHERE id = ?', (nome, email, telefone, id))
        self.db.commit()
        return 'Usuário editado!'