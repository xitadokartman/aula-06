from flask import Blueprint, render_template, request, jsonify
from controllers.user_controller import UserController

# Criando um Blueprint para organizar as rotas de usuário
user_routes = Blueprint('user_routes', __name__)

# Instanciando o controller
controller = UserController()

@user_routes.route('/')
def index():
    usuarios = controller.listar_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

@user_routes.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    email = request.form['email']
    controller.adicionar_usuario(nome, email)
    return jsonify({'mensagem': 'Usuário adicionado com sucesso!'})
