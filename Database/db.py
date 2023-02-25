from Database.models import *

db.bind(provider='mysql', host='127.0.0.1', user='root', passwd='1111', database='shop')

db.generate_mapping(create_tables=True)