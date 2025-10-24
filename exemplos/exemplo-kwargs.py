def mostrar_info(**kwargs):
    print(kwargs)
    print(f"Nome: {kwargs['nome']}")

mostrar_info(nome="Guilherme", idade=32, curso="Sistemas de Informação")


