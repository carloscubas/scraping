import requests
import pprint
from bs4 import BeautifulSoup

# https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.find_all(class_='chorus'))