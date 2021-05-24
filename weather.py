#using open weather api and requests library
import requests
from pprint import pprint
API_Key = '70ab16a21dcd24974f611450e7c2ef92'
city = input('Enter a city: ')
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)