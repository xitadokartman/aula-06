from flask import Flask
from routes.user_routes import user_routes  # importando o Blueprint

app = Flask(__name__)

# Registrando o Blueprint no app principal
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(debug=True)
