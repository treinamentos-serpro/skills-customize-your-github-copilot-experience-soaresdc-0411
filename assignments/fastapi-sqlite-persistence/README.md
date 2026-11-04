# 📘 Atividade: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Evolua uma API FastAPI para armazenar seus itens em um banco SQLite, em vez de mantê-los apenas na memória. Você praticará comandos SQL, integração com rotas HTTP e persistência de dados entre execuções.

## 📝 Tarefas

### 🛠️ Criar o banco e a tabela de itens

#### Descrição
Configure o banco SQLite usado pela aplicação e crie a tabela necessária para armazenar os itens da API.

#### Requisitos
O programa concluído deve:

- Usar o módulo `sqlite3`, incluído na biblioteca padrão do Python.
- Criar o arquivo `items.db` na pasta da assignment.
- Criar uma tabela `items` com `id` como chave primária, `name` obrigatório e `description` opcional.
- Criar a tabela automaticamente quando a aplicação iniciar, sem apagar dados existentes.
- Usar uma conexão que seja fechada corretamente após cada operação no banco.

### 🛠️ Consultar itens no banco de dados

#### Descrição
Implemente as rotas de leitura para que elas consultem o SQLite, em vez de uma lista em memória.

#### Requisitos
O programa concluído deve:

- Implementar `GET /items` para retornar todos os registros da tabela.
- Implementar `GET /items/{item_id}` para retornar um registro pelo identificador.
- Converter os resultados do banco para o modelo de resposta Pydantic da API.
- Responder com HTTP 404 quando o identificador não existir.

### 🛠️ Criar e atualizar itens

#### Descrição
Conecte as rotas de escrita ao banco SQLite e use os dados validados pela API para inserir ou atualizar registros.

#### Requisitos
O programa concluído deve:

- Implementar `POST /items` para inserir um item e retornar o registro criado com HTTP 201.
- Obter o identificador do novo item a partir do banco de dados.
- Implementar `PUT /items/{item_id}` para atualizar o nome e a descrição de um item existente.
- Responder com HTTP 404 ao tentar atualizar um identificador inexistente.
- Manter os dados recebidos sujeitos à validação do modelo Pydantic.

### 🛠️ Remover itens e verificar a persistência

#### Descrição
Finalize as operações CRUD e confirme que os dados continuam disponíveis depois que a aplicação for encerrada e iniciada novamente.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /items/{item_id}` para remover um registro existente.
- Responder com HTTP 204 ao remover o registro e HTTP 404 quando ele não existir.
- Usar o banco SQLite como fonte dos dados, sem depender de uma lista em memória.
- Permitir verificar as rotas pela documentação interativa em `/docs`.
- Preservar os itens cadastrados após reiniciar a aplicação.