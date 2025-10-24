from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)

# Define uma rota principal ("/")
@app.route("/")
def home():
    return "Olá! Este é o meu primeiro app Flask"

# Executa o servidor
if __name__ == "__main__":
    app.run()


