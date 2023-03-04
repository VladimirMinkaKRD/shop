import fastapi
from Database import crud
from Database.crud import Repository

api = fastapi.FastAPI()


@api.post('/user')
@crud.db_session
def create_user(attributes: dict = fastapi.Body()):
    name = attributes['name']
    create_stuff = attributes['create_stuff']
    return crud.Repository().create_user(name, create_stuff)


@api.put('/user/{user_id:int}')
@crud.db_session
def update_user(user_id: int = fastapi.Path(), create_stuff=fastapi.Body()):
    crud.update_user(user_id, create_stuff['create_stuff'])
    return True


@api.get('/get_info_by_user_id/{user_id:int}')
@crud.db_session
def get_info_about_user_by_id(user_id: int):
    return crud.get_user_info(crud.User[user_id])


@api.delete('/user/{user_id}')
@crud.db_session
def delete_user(user_id: int = fastapi.Path()):
    crud.get_user_by_id(user_id).delete()
    return True


@api.post('/create_buy/{user_id:int}')
@crud.db_session
def create_buy(user_id: int = fastapi.Path(), buy: dict = fastapi.Body()):
    id = crud.get_user_by_id(user_id).id
    buying = crud.Repository().create_deal(id, buy)
    return {
        'date_of_order': buying.date_of_order,
        'sum_deal': buying.sum_of_order,
        'seller': buying.seller
    }


@api.get('/get_all_goods')
@crud.db_session
def get_all_goods():
    return crud.get_all_goods()


@api.get('/get_all_buyers')
@crud.db_session
def get_all_buyers():
    return crud.get_all_buyers()


@api.get('/user/history/{user_id:int}')
@crud.db_session
def get_buyer_buys(user_id: int = fastapi.Path()):
    return crud.Repository().get_buyer_buys(user_id)


@api.put('/stuff/{user_id:int}')
@crud.db_session
def update_stuff(user_id: int = fastapi.Path(), stuff: dict = fastapi.Body()):
    crud.Repository().update_stuff(user_id, stuff['stuff'], stuff['amount'], stuff['price'])
    return True


@api.get('/get_info_about_stuff/{stuff_id:int}')
@crud.db_session
def get_info_about_stuff(stuff_id: int = fastapi.Path()):
    return crud.get_good_info_by_id(stuff_id)


@api.post('/stuff/{user_id:int}')
@crud.db_session
def create_stuff(user_id: int, stuff: dict = fastapi.Body()):
    stuff = crud.Repository().create_stuff(user_id, stuff['stuff'], stuff['amount'], stuff['price'])
    return stuff


@api.delete('/stuff/{stuff_id:int}')
@crud.db_session
def delete_stuff(stuff_id: int = fastapi.Path()):
    crud.get_good_by_id(stuff_id).delete()
    return True
