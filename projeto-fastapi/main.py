from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

ITEMS = {
    1: {
        "name": "Book",
        "price": 30,
        "avaiable": True
    },
    
    2: {
        "name": "Notebook",
        "price": 20,
        "avaiable": True
    }
}

@app.get("/items/{item_id}")
async def read_item(item_id: int, show_price: bool = True):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    product = dict(ITEMS[item_id])
    if not show_price:
        del product["price"]
    return {"item": product}