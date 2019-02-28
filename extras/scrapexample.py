import requests
import pprint
from bs4 import BeautifulSoup

# pip install requests
# pip install beautifulsoup4

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.find_all(class_='chorus'))