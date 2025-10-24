class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome       # atributo
        self.idade = idade     # atributo

    def falar(self):           # método
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# criando um objeto
p1 = Pessoa("Guilherme", 25)
p1.falar()
