from pydantic import BaseModel, Field

class ITEM(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Item name")
    description: str | None = Field(max_length=300, description="Description of a product")
    price: int = Field(gt=0, description="Item price")
    avaible: bool = Field(default=True, description="Item avaiable")