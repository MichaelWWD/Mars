import requests
from bs4 import BeautifulSoup

url = 'https://www.carsguide.com.au/car-reviews/fastest-selling-cars-in-australia-10534'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

cars = soup.find_all('div', class_='gallery-item-info')

for car in cars:
    model = car.find('h3', class_='title').text.strip()
    price = car.find('div', class_='price').text.strip()
    year = car.find('div', class_='item-details').text.strip().split('\n')[0]
    image = car.find('img')['src']

    print('Model:', model)
    print('Price:', price)
    print('Year:', year)
    print('Image URL:', image)
    print('\n')
# In the above code, we first find all the divs with class 'gallery-item-info'.
#  Then, we loop through each div and extract the model, price, year, and image URL using their respective HTML tags and class names. Finally, we print out the extracted data for each car.