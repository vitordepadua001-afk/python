from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

ITEMS = {
    1: {
        "name": "Book",
        "description": "A book to read",
        "price": 30,
        "avaiable": True
    },
    
    2: {
        "name": "Notebook",
        "description": "",
        "price": 20,
        "avaiable": True
    }
}

class ITEM(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Item name")
    description: str | None = Field(max_length=300, description="Description of product")
    price: int = Field(gt=0, description="Item price")
    avaiable: bool = Field(default=True, description="Item avaiable")

@app.get("/items/{item_id}")
async def read_item(item_id: int, show_price: bool = True):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    product = dict(ITEMS[item_id])
    if not show_price:
        del product["price"]
    return {"item": product}

@app.put("/items/{item_id}", response_model=ITEM)
async def change_item(item_id: int, item: ITEM)