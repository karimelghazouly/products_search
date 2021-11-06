import pytest
import json

from app import app

@pytest.fixture
def client():
  with app.test_client() as client:
    yield client


def test_searching_valid_word(client):
  resp = client.get('/search_products?search_sentence=hats')
  data = json.loads(resp.data)
  assert len(data['data']) != 0
  assert resp.status_code == 200



def test_searching_invalid_word(client):
  resp = client.get("/search_products?search_sentence=''")
  data = json.loads(resp.data)
  assert resp.status_code == 200
  assert data['data'] == []
