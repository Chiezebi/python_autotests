import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '964652dfcca8febdcccfa67346395f79'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }

BODY_CREATE = {
    "name": "Гриша",
    "photo_id": 78
}
BODY_RENAME = {
    "pokemon_id": "67479",
    "name": "Захар",
    "photo_id": 78
}
BODY_CATCH = {
    "pokemon_id": "67479"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(response_create.json)

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_RENAME)
print(response_rename.json)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_CATCH)
print(response_catch.json)