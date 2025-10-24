### Para instalar o flask no ambiente:
    ### comando para criar um ambiente virtual para o python (isolar dependencias e bibliotecas instaladas do ambiente host)

    python -m venv venv

    ### comando para habilitar/usar esse ambiente virtual (no linux)

    source venv/bin/activate

    ### comando para instalar o flask

    pip install flask

    ### comando para iniciar a aplicação flask (troque app.py pelo nome do seu aplicativo flask)

    python app.py

## Exercício
### Objetivo

Desenvolver uma aplicação web utilizando Flask e conceitos de Programação Orientada a Objetos (POO), aplicando Model, Controller e View/API, para gerenciar tarefas de forma organizada e interativa.

### Contexto

Você foi contratado para criar um sistema simples de lista de tarefas. Cada usuário poderá adicionar, visualizar, marcar como concluída e remover tarefas. O objetivo da atividade é organizar o código de forma orientada a objetos, separando responsabilidades em camadas e mantendo o projeto modular.

### Requisitos da aplicação

#### Model (camada de dados)

Criar uma classe Tarefa com atributos:

- id (identificador da tarefa)
- descricao (texto da tarefa)
- concluida (boolean, padrão False)

#### Implementar métodos para:

- Marcar como concluída
- Atualizar descrição
- Controller (camada de regras)
- Criar uma classe TarefaController para gerenciar uma lista de tarefas.

#### Métodos obrigatórios:

- adicionar_tarefa(descricao)
- listar_tarefas()
- remover_tarefa(id)
- concluir_tarefa(id)

#### API / View (camada de apresentação)

- Criar uma pasta routes com um arquivo tarefa_routes.py.
- Utilizar Blueprints do Flask para organizar as rotas.

#### Rotas obrigatórias:

- / → lista todas as tarefas (render_template com HTML)
- /adicionar → adiciona uma nova tarefa (POST)
- /remover/<id> → remove uma tarefa (POST ou GET)
- /concluir/<id> → marca uma tarefa como concluída (POST ou GET)

#### Templates

- Criar uma pasta templates com arquivos HTML:
- Exibir todas as tarefas em uma lista.
- Permitir adicionar novas tarefas através de um formulário.
- Permitir marcar tarefas como concluídas e remover tarefas com botões.
- Funcionalidades adicionais (opcional, para bônus)
- Ordenar tarefas concluídas e não concluídas separadamente.
- Adicionar filtros por status (todas, pendentes, concluídas).
- Utilizar CSS básico para melhorar a visualização.

### Requisitos técnicos

- Separar o projeto em camadas: Model, Controller, Routes/View.

- Utilizar POO para representar tarefas e controladores.

- Aplicar render_template para exibir informações em HTML.

- Aplicar Blueprints para organizar as rotas.

- Rodar o projeto localmente com python app.py ou flask run.