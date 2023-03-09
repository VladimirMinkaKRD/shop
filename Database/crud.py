import datetime

from pony.orm import db_session, select

from Database.models import User, Good, Buy


#TODO Реализовать связи многие ко многи и одни ко многим

class Repository:
    @db_session
    def create_user(self, name, create_stuff=False, date_of_hire=None):
        self.name = name
        self.create_stuff = create_stuff
        self.date_of_hire = date_of_hire
        if not create_stuff:
            user = User(name=self.name, create_stuff=create_stuff)
            return {'name': user.name}
        else:
            user = User(name=self.name, create_stuff=self.create_stuff, date_of_hire=datetime.datetime.now())
            return {'name': user.name, 'create_stuff': user.create_stuff, "date_of_hire": user.date_of_hire}

    @db_session
    def create_stuff(self, id: int, stuff: str, amount: int, price: float):
        self.id = id
        self.stuff = stuff
        self.amount = amount
        self.price = price
        create_stuff = select(u.create_stuff for u in User if u.id == id)[:][0]
        if create_stuff:
            Good(stuff=self.stuff, amount=self.amount, price=self.price)
            return True
        else:
            return f'You can not to create stuff'

    @db_session
    def remove_from_store(self, stuff: str, amount: int):
        id = select(g.id for g in Good if g.stuff == stuff)[:][0]
        stuff_to_update = Good[id]
        new_amount = stuff_to_update.amount - amount
        stuff_to_update.amount = new_amount
        return stuff_to_update

    @db_session
    def create_deal(self, kwargs: dict):
        sum_of_order = 0
        set_of_goods: set = set()

        for good_dict in kwargs['goods']:
            good_obj=Good.select(id=good_dict["id"])[:]._items[0] #TODO Селать одним запросом
            sum_of_order += good_obj.price
            set_of_goods.add(good_obj)

        # for stuff, amount in kwargs.items():
        #     query = select(g for g in Good if g.stuff == stuff)[:]
        #     total_price = amount * query[0].price
        #     sum_of_order += total_price
        #     self.remove_from_store(stuff, amount)
        buyer = User.select(id=kwargs["user_id"])[:]
        deal = Buy(
            sum_of_order=sum_of_order,
            date_of_order=datetime.datetime.now(),
            buyer=buyer._items[0].id,
            goods=set_of_goods)
        print(deal)
        return deal

    @db_session
    def get_deal(self, id):
        buy_obj=Buy.select(id=id)[:]._items[0]
        for good in buy_obj.goods:
            print(good.price)
            print(good.id)
            print(good.stuff)




    @db_session
    def get_buyer_buys(self, id):
        self.id = id
        buys_info = []
        buyer = User[id]
        buys = select((b.id, b.date_of_order, b.sum_of_order, b.seller, b.good) for b in Buy if b.buyer == buyer.id)[:]
        for buy in buys:
            buy_dict = {'id': (buy[0],), 'date_of_order': (buy[1],), 'sum_of_order': (buy[2],), 'seller': buy[3]}
            buys_info.append(buy_dict)
        return buys_info

    @db_session
    def update_stuff(self, id, position: str, quantity: int, new_price: float):
        self.id = id
        self.position = position
        self.quantity = quantity
        self.new_price = new_price
        update_stuff = select(u.create_stuff for u in User if u.id == id)[:][0]
        if update_stuff:
            id = select(g.id for g in Good if g.stuff == position)[:][0]
            stuff_to_update = Good[id]
            stuff_to_update.amount = self.quantity
            stuff_to_update.price = self.new_price
            return stuff_to_update
        else:
            return f'You can not to update stuff'

    @db_session
    def get_user_by_id(self, id: int):
        return User[id]


    @db_session
    def get_all_goods(self):
        store = {}
        goods = select(g for g in Good)[:]
        for good in goods:
            store[good.stuff] = good.amount
        return store


    @db_session
    def create_user(self, name=None):
        User(name=name, create_stuff=False, date_of_hire=datetime.datetime.now())





    @db_session
    def get_all_buyers(self):
        lst_buyers = []
        buyers = select((u.id, u.name) for u in User if u.create_stuff == 0)[:]
        for buyer in buyers:
            buyer_dict = {}
            buyer_dict[buyer[0]] = buyer[1]
            lst_buyers.append(buyer_dict)
        return lst_buyers


    @db_session
    def get_buy_by_id(self, id: int):
        return Buy[id]


    @db_session
    def get_user_info(self, user: User):
        if user.create_stuff:
            return {'id': user.id, 'name': user.name, 'is_seller': user.create_stuff,
                    'date_of_hire': str(user.date_of_hire)}
        else:
            return {'id': user.id, 'name': user.name}


    @db_session
    def get_buy_info(self, buy: Buy):
        return {
            'id': buy.id,
            'date_of_order': str(buy.date_of_order),
            'sum_of_order': buy.sum_of_order,
            'seller': buy.seller,
            'buyer': buy.buyer,
            'goods': buy.good
        }


    @db_session
    def update_user(self, id: int, create_stuff: bool = False):
        user_to_update = User[id]
        if create_stuff:
            user_to_update.create_stuff = create_stuff
            user_to_update.date_of_hire = datetime.now()
            return user_to_update
        elif not create_stuff:
            user_to_update.create_stuff = create_stuff
            user_to_update.date_of_hire = None
            return user_to_update


    @db_session
    def get_good_by_id(self, id: int):
        return Good[id]


    @db_session
    def get_good_info_by_id(self, id: int):
        good = Good[id]
        return {'stuff': good.stuff, 'amount': good.amount, 'price': good.price}


    @db_session
    def get_all_users(self):
        lst_buyers: list = []
        buyers = User.select()[:]
        lst_buyers.extend(buyers)
        print(type(buyers))
        return lst_buyers