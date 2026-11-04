# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar itens usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e respostas apropriadas para recursos existentes ou não encontrados.

## 📝 Tarefas

### 🛠️ Criar a aplicação e um endpoint de saúde

#### Descrição
Configure e execute uma aplicação FastAPI que confirme quando a API está disponível.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi uvicorn`.
- Criar uma aplicação FastAPI no arquivo `main.py`.
- Implementar `GET /health`, retornando um JSON com `{"status": "ok"}`.
- Permitir iniciar a aplicação com `python -m uvicorn main:app --reload`.
- Exibir a documentação interativa em `/docs`.

### 🛠️ Listar e consultar itens

#### Descrição
Defina o formato dos itens e implemente rotas para listar os itens cadastrados e consultar um item pelo identificador.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic para os dados de um item, com `name` obrigatório e `description` opcional.
- Manter os itens em uma lista em memória e iniciar com pelo menos um item de exemplo.
- Implementar `GET /items` para retornar todos os itens.
- Implementar `GET /items/{item_id}` para retornar o item correspondente.
- Responder com HTTP 404 quando o identificador solicitado não existir.

### 🛠️ Criar itens com validação

#### Descrição
Adicione uma rota para cadastrar itens. A API deve validar os dados recebidos e gerar o identificador no servidor.

#### Requisitos
O programa concluído deve:

- Implementar `POST /items` recebendo os dados do item em JSON.
- Usar o modelo Pydantic para validar a requisição.
- Gerar um identificador único para o novo item sem solicitá-lo ao cliente.
- Armazenar o item e retornar o recurso criado com status HTTP 201.
- Retornar os erros de validação do FastAPI quando os dados forem inválidos.

### 🛠️ Atualizar e remover itens

#### Descrição
Complete as operações da API implementando a substituição e a remoção de um item existente.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /items/{item_id}` para substituir os dados de um item existente.
- Implementar `DELETE /items/{item_id}` para remover um item existente.
- Responder com HTTP 404 ao tentar atualizar ou remover um identificador inexistente.
- Retornar o item atualizado na resposta de `PUT`.
- Retornar HTTP 204 ao remover um item com sucesso.