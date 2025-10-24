from models.user import User

class UserController:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome, email):
        novo_user = User(nome, email)
        self.usuarios.append(novo_user)

    def listar_usuarios(self):
        return self.usuarios
