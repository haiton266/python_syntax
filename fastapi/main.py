from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Points to the FastAPI app instance in main.py
        host="0.0.0.0",  # Exposes the server to external connections
        port=8080,  # Specifies the port number
        workers=4,  # Number of worker processes
        reload=True,  # Enable auto-reload for development
    )
