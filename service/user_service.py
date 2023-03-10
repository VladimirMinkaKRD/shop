from Database.crud import Repository

crud = Repository()


class UserService:
    def create_user(self, kwargs):
        name = kwargs['name']
        create_stuff = kwargs['create_stuff']
        user = Repository().create_user(name, create_stuff)
        return user.to_dict()

    def get_info_about_user_by_id(self, id):
        return crud.get_user_by_id(id).to_dict()

    def delete_user(self, user_id):
        return crud.delete_user(user_id)