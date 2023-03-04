from datetime import datetime
from pony.orm import *

db = Database()


class Good(db.Entity):  # TODO доработать класс User и создать классы наследники Buyer и Seller со своим функционалом
    id = PrimaryKey(int, auto=True)
    stuff = Required(str)
    amount = Optional(int, default=0)
    price = Optional(float)


class Buy(db.Entity):
    id = PrimaryKey(int, auto=True)
    date_of_order = Optional(datetime)
    sum_of_order = Required(float)
    buyer = Required(int)
    seller = Required(int)
    good = Required(Json)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 20)
    create_stuff = Required(bool, default=False)
    date_of_hire = Optional(datetime)

# class Seller(db.Entity):
#     id = PrimaryKey(int, auto=True)
#     name = Required(str, 20)
#     date_of_hire = Required(datetime)
#     purchases = Set('Buy')
#
#
# class Buyer(db.Entity):
#     id = PrimaryKey(int, auto=True)
#     name = Optional(str, 20)
#     purchases = Set('Buy')
