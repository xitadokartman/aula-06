class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo
        # `__` (dois underlines) é um mecanismo chamado name mangling (ofuscação de nome), é uma forma de proteger atributos internos da classe, evitando acessos acidentais fora dela

    def ver_saldo(self):
        print(f"O saldo é {self.__saldo}")
        return self.__saldo

minha_conta = Conta(500)
minha_conta.ver_saldo()



