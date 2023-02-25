import pydantic
from datetime import datetime


class Seller(pydantic.BaseModel):
    id: int
    name: str
    date_of_hire = datetime


class Buyer(pydantic.BaseModel):
    id: str
    name: str


class Buy(pydantic.BaseModel):
    id: int
    date_of_order: datetime
    sum_of_order: float
    buyer: 'Buyer'
    seller: 'Seller'
    goods: dict


class Good(pydantic.BaseModel):
    id: int
    stuff: str
    amount: int
    price: float


class UpdateBuyer(pydantic.BaseModel):
    id: int
    name: str


Seller.update_forward_refs()
Buyer.update_forward_refs()
Buy.update_forward_refs()
Good.update_forward_refs()
UpdateBuyer.update_forward_refs()