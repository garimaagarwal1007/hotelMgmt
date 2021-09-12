from typing import Optional, List
import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    item_id: int = Field(..., description="item id")
    description: Optional[str] = Field(..., description="desc")
    is_active: bool = Field(True, description="is active")


class ItemList(BaseModel):
    data: List[Item] = Field(..., description="orders")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/orders")
def item_list(items: ItemList):
    return items


@app.post("/items")
def read_item(item: Item):
    return {"item_id": item.item_id, "desc": item.description}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5732)
