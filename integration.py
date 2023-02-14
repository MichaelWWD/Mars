import requests

BASE_URL = 'https://swapi.dev/api'

all_people_response = requests.get(url=f'{BASE_URL}/people/').json()
print(all_people_response)
