class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        print("Algum som genérico...")

class Cachorro(Animal):
    def som(self):
        print(f"{self.nome}: Au au!")

class Gato(Animal):
    def som(self):
        print(f"{self.nome}: Miau!")

animais = [  # Lista de animais (instâncias de classes diferentes)
    Cachorro("Pluto"),
    Gato("Garfield"),
]

for animal in animais:  # Mesma chamada para todos
    animal.som()


