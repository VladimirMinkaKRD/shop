from datetime import datetime
from pony.orm import Database, PrimaryKey, Required, Optional, Json, Set

db = Database()


class Buy(db.Entity):
    id = PrimaryKey(int, auto=True)
    date_of_order = Optional(datetime)
    sum_of_order = Required(float)
    buyer = Required(int)
    goods = Set("Good")


class Good(db.Entity):
    id = PrimaryKey(int, auto=True)
    stuff = Required(str)
    amount = Optional(int, default=0)
    price = Optional(float)
    orders = Set('Buy')


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
