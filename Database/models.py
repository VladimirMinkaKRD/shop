from datetime import datetime
from pony.orm import *


db = Database()


class Seller(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 20)
    date_of_hire = Required(datetime)
    purchases = Set('Buy')


class Buyer(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str, 20)
    purchases = Set('Buy')


class Good(db.Entity):
    id = PrimaryKey(int, auto=True)
    stuff = Required(str)
    amount = Optional(int, default=0)
    price = Optional(float)
    purchases = Set('Buy')


class Buy(db.Entity):
    id = PrimaryKey(int, auto=True)
    date_of_order = Optional(datetime)
    sum_of_order = Required(float)
    buyer = Required(Buyer)
    seller = Required(Seller)
    goods = Set(Good)

