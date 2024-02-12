import requests 
import bs4 
import fake_useragent

user_agent = fake_useragent.UserAgent().random
headers = {
    'user-agent': user_agent
}
url = 'https://www.gismeteo.ru/weather-moscow-4368/'
response = requests.get(url, headers=headers)
html = bs4.BeautifulSoup(response.text, 'html.parser')

temperature_element = html.select_one('.unit.unit_temperature_c').text 
print(temperature_element)
