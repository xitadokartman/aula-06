def meu_decorator(minha_funcao):
    def envolver():
        print("Executa algo antes da função")
        minha_funcao()
        print("Executa algo depois da função")

    return envolver()

@meu_decorator
def ola():
    print("Olá mundo")

