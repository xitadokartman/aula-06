import time

def medir_tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        print(f"Executando {funcao.__name__} com args={args}, kwargs={kwargs}")
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Função {funcao.__name__} executou em {fim - inicio:.4f} segundos\n")
        return resultado
    return wrapper

@medir_tempo
def tarefa_demorada(a, b, **kwargs):
    print(kwargs['mensagem'])
    time.sleep(a + b)
    print("Tarefa concluída!")

tarefa_demorada(1, 2, mensagem="Executando tarefa com *args e **kwargs*")

