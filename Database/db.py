from Database.models import db
def init_db():

    db.bind(provider='mysql', host='127.0.0.1', user='user', passwd='user', database='mydb', port=3306)
    db.generate_mapping(create_tables=True)