from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Inventory API")


class ItemCreate(BaseModel):
    name: str
    description: str = ""


class Item(ItemCreate):
    id: int


items: list[Item] = []


# Tarefa 1: implemente GET /health.

# Tarefa 2: adicione um item de exemplo e implemente GET /items e
# GET /items/{item_id}. Responda com HTTP 404 para IDs inexistentes.

# Tarefa 3: implemente POST /items. Gere o ID no servidor e responda
# com HTTP 201 ao criar o item.

# Tarefa 4: implemente PUT /items/{item_id} e DELETE /items/{item_id}.
# Responda com HTTP 404 para IDs inexistentes e HTTP 204 ao remover.