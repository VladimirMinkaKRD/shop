import fastapi
import pydantic_models
from Database import crud

api = fastapi.FastAPI()


@api.post('/create_buyer')
@crud.db_session
def create_buyer(name: dict = fastapi.Body()):
    new_name = name['name']
    return crud.Visitor(new_name).create_user()


@api.put('/buyer/{buyer_id}')
@crud.db_session
def update_buyer(buyer_id: int = fastapi.Path(), name=fastapi.Body()):
    crud.update_buyer(buyer_id, name['name'])
    return True


@api.get('/get_info_by_buyer_id/{buyer_id:int}')
@crud.db_session
def get_info_about_buyer_by_id(buyer_id: int):
    return crud.get_buyer_info(crud.Buyer[buyer_id])


@api.delete('/buyer/{buyer_id}')
@crud.db_session
def delete_buyer(buyer_id: int = fastapi.Path()):
    crud.get_buyer_by_id(buyer_id).delete()
    return True


@api.post('/create_buy/{buyer_id:int}')
@crud.db_session
def create_buy(buyer_id: int = fastapi.Path(), buy: dict = fastapi.Body()):
    name = crud.get_buyer_by_id(buyer_id).name
    buying = crud.Visitor(name).create_deal(buy)
    return {
        'id': buying.id,
        'date_of_order': buying.date_of_order,
        'sum_deal': buying.sum_of_order,
        'seller': buying.seller.name
    }


@api.get('/get_all_goods')
@crud.db_session
def get_all_goods():
    return crud.get_all_goods()


@api.get('/get_all_buyers')
@crud.db_session
def get_all_buyers():
    return crud.get_all_buyers()


@api.get('/buyer/my_history/{buyer_id:int}')
@crud.db_session
def get_buyer_buys(buyer_id: int = fastapi.Path()):
    name = crud.get_buyer_by_id(buyer_id).name
    return crud.Visitor(name).get_buyer_buys()


@api.post('/hire_seller')
@crud.db_session
def create_seller(name: dict = fastapi.Body()):
    seller_name = name['name']
    crud.Salesman(seller_name).create_seller()
    return True


@api.put('/update_stuff/{seller_id:int}')
@crud.db_session
def update_stuff(seller_id: int = fastapi.Path(), stuff: dict = fastapi.Body()):
    seller_name = crud.get_seller_by_id(seller_id).name
    crud.Salesman(seller_name).update_stuff(stuff['stuff'], stuff['amount'], stuff['price'])
    return True


@api.get('/get_info_about_stuff/{stuff_id:int}')
@crud.db_session
def get_info_about_stuff(stuff_id: int = fastapi.Path()):
    return crud.get_good_info_by_id(stuff_id)


@api.post('/create_stuff/{seller_id:int}')
@crud.db_session
def create_stuff(seller_id: int, stuff: dict = fastapi.Body()):
    seller_name = crud.get_seller_by_id(seller_id).name
    crud.Salesman(seller_name).create_stuff(stuff['stuff'], stuff['amount'], stuff['price'])
    return True


@api.delete('/stuff/{stuff_id:int}')
@crud.db_session
def delete_stuff(stuff_id: int = fastapi.Path()):
    crud.get_good_by_id(stuff_id).delete()
    return True
