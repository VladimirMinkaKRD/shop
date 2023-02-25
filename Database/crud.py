import datetime

import pydantic_models
from Database.db import *
import random


class Repository: # TODO 1. Убрать инит метод, в каждый метод отдавать необх параметр(name), создавать только 1 раз


    @db_session
    def create_user(self):
        buyer = Buyer(name=self.name)
        flush()
        return {'id': buyer.id, 'name': buyer.name}

    @db_session
    def create_deal(self, kwargs: dict):
        sum_of_order = 0
        for stuff, amount in kwargs.items():
            query = select(g for g in Good if g.stuff == stuff)[:]
            total_price = amount * query[0].price
            sum_of_order += total_price
            remove_from_store(stuff, amount)
        seller = random.choice(select(s for s in Seller)[:])
        buyer = select(b for b in Buyer if b.name == self.name)[:][0]
        deal = Buy(date_of_order=datetime.now(), sum_of_order=sum_of_order, buyer=buyer, seller=seller)
        flush()
        return deal

    @db_session
    def get_buyer_buys(self):
        buys_info = []
        buyer_id = select(b.id for b in Buyer if b.name == self.name)[:][0]
        buyer = Buyer[buyer_id]
        buys = select((b.id, b.date_of_order, b.sum_of_order, b.seller) for b in Buy if b.buyer == buyer)[:]
        for buy in buys:
            buy_dict = {'id': (buy[0],), 'date_of_order': (buy[1],), 'sum_of_order': (buy[2],), 'seller': buy[3].name}
            buys_info.append(buy_dict)
        return buys_info


class Salesman:
    def __init__(self, name):
        self.name = name

    @db_session
    def create_seller(self, date_of_hire=datetime.now()):
        self.date_of_hire = date_of_hire
        seller = Seller(name=self.name, date_of_hire=self.date_of_hire)
        flush()
        return seller

    @db_session
    def create_stuff(self, stuff: str, amount: int, price: float):
        self.stuff = stuff
        self.amount = amount
        self.price = price
        good = Good(stuff=self.stuff, amount=self.amount, price=self.price)
        flush()
        return good

    @db_session
    def update_stuff(self, position: str, quantity: int, new_price: float):
        self.position = position
        self.quantity = quantity
        self.new_price = new_price
        id = select(g.id for g in Good if g.stuff == position)[:][0]
        stuff_to_update = Good[id]
        stuff_to_update.amount = self.quantity
        stuff_to_update.price = self.new_price
        return stuff_to_update


@db_session
def get_all_goods():
    store = {}
    goods = select(g for g in Good)[:]
    for good in goods:
        store[good.stuff] = good.amount
    return store


@db_session
def get_buyer_by_id(id: int):
    return Buyer[id]


@db_session
def get_all_buyers():
    lst_buyers = []
    buyers = select((b.id, b.name) for b in Buyer)[:]
    for buyer in buyers:
        buyer_dict = {}
        buyer_dict[buyer[0]] = buyer[1]
        lst_buyers.append(buyer_dict)
    return lst_buyers


@db_session
def get_seller_by_id(id: int):
    return Seller[id]


@db_session
def get_buy_by_id(id: int):
    return Buy[id]


@db_session
def get_buyer_info(buyer: pydantic_models.Buyer):
    return {'id': buyer.id, 'name': buyer.name}


@db_session
def get_seller_info(seller: pydantic_models.Seller):
    return {'id': seller.id, 'name': seller.name, 'date_of_hire': seller.date_of_hire}


@db_session
def get_buy_info(buy: pydantic_models.Buy):
    return {
        'id': buy.id,
        'date_of_order': buy.date_of_order,
        'seller': buy.seller,
        'buyer': buy.buyer
    }


@db_session
def update_buyer(id: int, name: str):
    buyer_to_update = Buyer[id]
    buyer_to_update.name = name
    return buyer_to_update


@db_session
def remove_from_store(stuff: str, amount: int):
    id = select(g.id for g in Good if g.stuff == stuff)[:][0]
    stuff_to_update = Good[id]
    new_amount = stuff_to_update.amount - amount
    stuff_to_update.amount = new_amount
    return stuff_to_update


@db_session
def get_good_by_id(id: int):
    return Good[id]


@db_session
def get_good_info_by_id(id: int):
    good = Good[id]
    return {'stuff': good.stuff, 'amount': good.amount, 'price': good.price}
