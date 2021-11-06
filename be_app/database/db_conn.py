from pymongo import MongoClient
import os

client = MongoClient("mongodb+srv://admin_user:" + os.environ['DATABASE_ADMIN_PASSWORD'] +"@intelistyle.nn16b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['intelistyle']
