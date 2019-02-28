import requests
import pprint
from bs4 import BeautifulSoup
import re
import logging
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# pip install elasticsearch (https://elasticsearch-py.readthedocs.io/en/master/)

url = 'https://guiadacozinha.com.br/category/almoco-de-domingo/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
cards = soup.find_all(class_='recipe-card')

for card in cards:
	url_recipe = card.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
	page_recipes = requests.get(url_recipe)
	recipe = BeautifulSoup(page_recipes.text, 'html.parser')
	body = recipe.find("article", {'class':'content-body'})
	title = body.find('h1').text
	details = recipe.find("div", {'class':'entry-content'})
	ingredients = []
	for li in details.find('ul').find_all('li'):
		ingredients.append(li.text)

	preparations = []
	for p in details.find_all('p'):
		preparations.append(p.text)

	print(title)
	print(ingredients)
	print(' '.join(preparations))