from flask import Flask, request
from search_indexing.products import index_products
from search_indexing.main import search_index
from database.db_conn import db
import json


index_products()
app = Flask(__name__)

@app.after_request # 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/search_products", methods=['GET'])
def search_garments():
  try:
    search_sentence = request.args.get('search_sentence', '')
    matches_ids = search_index(search_sentence)
    matches = db['products'].find({'_id':{
      '$in': list(matches_ids)
    }}, {'product_title': 1, 'product_description': 1})
    
    matches_list = [json.dumps(match, default=str) for match in matches]
    return {'data': matches_list}
  except:
    return {'message': "Could not perform search right now."}, 500