#TODO: Create Product Model with id, name, price, in_stock
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float 
    in_stock: bool = True