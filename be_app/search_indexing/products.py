from database.db_conn import db
from .main import add_list_to_index

def index_products():
  print("----------------------------------------------------- Indexing products started -----------------------------------------------------")
  for product in db['products'].find():
    add_list_to_index([product['product_description'].lower()], product['_id'])
    add_list_to_index([product['product_title'].lower()], product['_id'])

  print("----------------------------------------------------- Indexing products finished -----------------------------------------------------")
