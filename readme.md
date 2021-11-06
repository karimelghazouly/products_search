## Project Strucutre
- `be_app` has the backend project
- `fe_app` has the frontend project
- I used mongo [Mongodb Atlas](https://www.mongodb.com/atlas/database) because i had no space to install mongodb :D 
- The tests are for the backend on the tests folder

## Approach
- I used [inverted index algorithm](https://en.wikipedia.org/wiki/Inverted_index) for searching.  
- I used very simple algorithm for this task:  
  1- Mainly I fetch all products in the begging of the server run  
  2- For every product I split the description and title to words, you can see the logic for this in `split_words`  
  3- Then I convert each word into singular using `inflect` library and save it to a dictionary with the object id of the product, so it the dictionary will look like this
  ```
  {
    'black': [ObjectID(123), ObjectID(11)],
    'hat': [ObjectID(11)]
    ...
  }
  ```
  4- When i get new sentence for search i split it again using `split_words` then i search for each word in the dictionary.  
  5- I merge all of these results and then query the DB with these object IDs


## Improvments
This can be improved in several ways, for example I am not doing ranking right now, i just get all results.  
also we can convert all nouns with same meaning to abstract word for example: shade and shadow 
there is alot more into techniques for improving search results.



## How To Run
For backend:
```
python3 -m venv intelistyle_env
source intelistyle_env/bin/activate
cd be_app
pip install -r requirements.txt
DATABASE_ADMIN_PASSWORD=admin_user_123123 flask run --host=0.0.0.0 --port=5010
```
for test run
```
DATABASE_ADMIN_PASSWORD=admin_user_123123 pytest -s
```

For frontend:
```
cd fe_app
npm install
npm start
```