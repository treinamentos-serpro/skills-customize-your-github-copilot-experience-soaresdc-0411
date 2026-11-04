from contextlib import asynccontextmanager, contextmanager
from pathlib import Path
import sqlite3
from typing import Iterator

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

DATABASE_PATH = Path(__file__).with_name("items.db")


class ItemData(BaseModel):
    name: str
    description: str = ""


class Item(ItemData):
    id: int


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database() -> None:
    # Tarefa 1: crie a tabela items sem apagar registros existentes.
    pass


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(title="Inventory API", lifespan=lifespan)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
    # Tarefa 2: consulte e retorne todos os itens do SQLite.
    raise NotImplementedError


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    # Tarefa 2: consulte um item e responda com HTTP 404 se não existir.
    raise NotImplementedError


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item_data: ItemData) -> Item:
    # Tarefa 3: insira o item e retorne o registro criado.
    raise NotImplementedError


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: ItemData) -> Item:
    # Tarefa 3: atualize o item ou responda com HTTP 404.
    raise NotImplementedError


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> Response:
    # Tarefa 4: remova o item ou responda com HTTP 404.
    raise NotImplementedError