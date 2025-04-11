import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8449e133a39291bdde8a01b5d4a5e95a'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_put = {
    "pokemon_id": "286061",
    "name": "BORZ",
    "photo_id": 2
}

body_addPokeball = {
    "pokemon_id": "286061"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_NewName = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_NewName.text)'''

response_addPokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_put)
print(response_addPokeball.text)

