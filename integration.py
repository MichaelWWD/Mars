import requests

BASE_URL = 'https://swapi.dev/api'

def get_all_people():
    response = requests.get(url=f'{BASE_URL}/people/')
    return response.json()

def get_star_ships_schema():
    return requests.get(url=f'{BASE_URL}/starships/schema').json

def get_first_star_ship():
    return requests.get(url=f'{BASE_URL}/starships/1').json()


def add_function(num):
    return num**2


result = add_function(13)
print(result)