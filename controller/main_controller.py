import fastapi
from Database.db import init_db
from service.user_service import UserService

# uvicorn controller.main_controller:api --reload


init_db()
print("i am here")
api = fastapi.FastAPI()

user_service = UserService()


# TODO Доделать упрощение эндпоинтов


@api.post('/user')
def create_user(attributes: dict = fastapi.Body()):
    return user_service.create_user(attributes)


@api.get('/user/{user_id:int}')
def get_info_about_user_by_id(user_id: int):
    return user_service.get_info_about_user_by_id(user_id)


@api.delete('/user/{user_id}')
def delete_user(user_id: int = fastapi.Path()):
    return user_service.delete_user(user_id)


#
#
# @api.get('/user')
# def get_all_users():
#     return crud.get_all_users()
#
#
# @api.put('/user/{user_id:int}')
# def update_user(user_id: int = fastapi.Path(), create_stuff=fastapi.Body()):
#     # crud.update_user(user_id, create_stuff['create_stuff'])
#     print("update_user")
#     return True
#
#

#
#
# @api.post('/buy')
# def create_buy(buy: dict = fastapi.Body()):
#     buying = crud.create_deal(buy)
#     crud.get_deal(1)
#     return {
#         'date_of_order': buying.date_of_order,
#         'sum_deal': buying.sum_of_order,
#     }
#
#
# @api.get('/goods?id={good_id}')
# def get_all_goods():
#     return crud.get_all_goods()
#
#
# @api.get('/get_all_buyers')
# def get_all_buyers():
#     return crud.get_all_buyers()
#
#
# @api.get('/user/history/{user_id:int}')
# def get_buyer_buys(user_id: int = fastapi.Path()):
#     return crud.get_buyer_buys(user_id)
#
#
# @api.put('/stuff/{user_id:int}')
# def update_stuff(user_id: int = fastapi.Path(), stuff: dict = fastapi.Body()):
#     crud.update_stuff(user_id, stuff['stuff'], stuff['amount'], stuff['price'])
#     return True
#
#
# @api.get('/get_info_about_stuff/{stuff_id:int}')
# def get_info_about_stuff(stuff_id: int = fastapi.Path()):
#     return crud.get_good_info_by_id(stuff_id)
#
#
# @api.post('/stuff/{user_id:int}')
# def create_stuff(user_id: int, stuff: dict = fastapi.Body()):
#     stuff = crud.create_stuff(user_id, stuff['stuff'], stuff['amount'], stuff['price'])
#     return stuff

# @api.delete('/stuff/{stuff_id:int}')
# 
# def delete_stuff(stuff_id: int = fastapi.Path()):
#     crud.get_good_by_id(stuff_id).delete()
#     return True
