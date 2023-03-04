import pydantic
from datetime import datetime


class User(pydantic.BaseModel):
    id: int
    name: str
    create_stuff: bool = False


class Buy(pydantic.BaseModel):
    id: int
    date_of_order: datetime
    sum_of_order: float
    buyer: 'User'
    seller: 'User'
    good: dict


class Good(pydantic.BaseModel):
    id: int
    stuff: str
    amount: int
    price: float


User.update_forward_refs()
Buy.update_forward_refs()
Good.update_forward_refs()
