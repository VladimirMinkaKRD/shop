
import fastapi
from Database import crud
from Database.crud import Repository
from Database.db import init_db

init_db()
print("i am here")
api = fastapi.FastAPI()

crud = Repository()


#TODO Доделать упрощение эндпоинтов



@api.post('/user')
@crud.db_session
def create_user(attributes: dict = fastapi.Body()):
    name = attributes['name']
    create_stuff = attributes['create_stuff']
    print(f"{name} {create_stuff}")
    # return crud.create_user(name, create_stuff)
    return True

@api.get('/user/{user_id:int}')
@crud.db_session
def get_info_about_user_by_id(user_id: int):
    return crud.get_user_info(crud.User[user_id])

@api.get('/user')
@crud.db_session
def get_all_users():
    return crud.get_all_users()



@api.put('/user/{user_id:int}')
@crud.db_session
def update_user(user_id: int = fastapi.Path(), create_stuff=fastapi.Body()):
    # crud.update_user(user_id, create_stuff['create_stuff'])
    print("update_user")
    return True





@api.delete('/user/{user_id}')
@crud.db_session
def delete_user(user_id: int = fastapi.Path()):
    crud.get_user_by_id(user_id).delete()
    print("asd")
    return True


@api.post('/buy')
@crud.db_session
def create_buy(buy: dict = fastapi.Body()):

    buying = crud.create_deal(buy)
    crud.get_deal(1)
    return {
        'date_of_order': buying.date_of_order,
        'sum_deal': buying.sum_of_order,
    }


@api.get('/goods?id={good_id}')
@crud.db_session()
def get_all_goods():
    return crud.get_all_goods()


@api.get('/get_all_buyers')
@crud.db_session
def get_all_buyers():
    return crud.get_all_buyers()


@api.get('/user/history/{user_id:int}')
@crud.db_session
def get_buyer_buys(user_id: int = fastapi.Path()):
    return crud.get_buyer_buys(user_id)


@api.put('/stuff/{user_id:int}')
@crud.db_session
def update_stuff(user_id: int = fastapi.Path(), stuff: dict = fastapi.Body()):
    crud.update_stuff(user_id, stuff['stuff'], stuff['amount'], stuff['price'])
    return True


@api.get('/get_info_about_stuff/{stuff_id:int}')
@crud.db_session
def get_info_about_stuff(stuff_id: int = fastapi.Path()):
    return crud.get_good_info_by_id(stuff_id)


@api.post('/stuff/{user_id:int}')
@crud.db_session
def create_stuff(user_id: int, stuff: dict = fastapi.Body()):
    stuff = crud.create_stuff(user_id, stuff['stuff'], stuff['amount'], stuff['price'])
    return stuff


@api.delete('/stuff/{stuff_id:int}')
@crud.db_session
def delete_stuff(stuff_id: int = fastapi.Path()):
    crud.get_good_by_id(stuff_id).delete()
    return True
