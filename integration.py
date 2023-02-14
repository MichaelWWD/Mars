import requests

BASE_URL = 'https://swapi.dev/api'

all_people_response = requests.get(url=f'{BASE_URL}/people/').json()
print(all_people_response)

star_ships_schema = requests.get(url=f'{BASE_URL}/starships/schema').json()
print(star_ships_schema)

first_star_ship = requests.get(url=f'{BASE_URL}/starships/1').json()
print(first_star_ship)
