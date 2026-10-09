from fastapi import FastAPI, HTTPException
from schema import ITEM

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

@app.get("/items/{item_id}")
async def read_item(item_id: int, show_price: bool = True):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found or not exists.")
    product = dict(ITEMS[item_id])
    if not show_price:
        del product["price"]
    return {"item": product}

@app.put("/items/{item_id}", response_model=ITEM)
async def update_item(item_id: int, item: ITEM):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found or not exists.")
    ITEMS[item_id] = item.model_dump()
    return ITEMS[item_id]