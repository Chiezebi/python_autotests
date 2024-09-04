import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '964652dfcca8febdcccfa67346395f79'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
TRAINER_ID = 4912

def test_status_code():
    response = requests.get(url = f'{URL}/trainers',)
    assert response.status_code == 200

def test_trainer_id():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '4912'