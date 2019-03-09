import requests
import pprint
from bs4 import BeautifulSoup
import re
import logging
from elasticsearch import Elasticsearch
import json
from time import sleep

def connect_elasticsearch():
	_es = None
	_es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
	if _es.ping():
		print('Connected')
	else:
		print('Could not connect!')
	return _es

def create_index(es_object, index_name):
	created = False
    # index settings
	settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "food": {
                "dynamic": "strict",
                "properties": {
                    "title": {
                        "type": "text",
                        "analyser" : "portugues_analyser_custom"
                    },
                    "description": {
                        "type": "text",
                        "analyser" : "portugues_analyser_custom"
                    },
                    "ingredients": {
                        "type": "nested",
                        "properties": {
                            "step": {
                            	"type": "text",
                        		"analyser" : "portugues_analyser_custom"
                        	}
                        }
                    },
                }
            }
        }
	}

	try:
		if not es_object.indices.exists(index_name):
			# Ignore 400 means to ignore "Index Already Exist" error.
			es_object.indices.create(index=index_name, ignore=400, body=settings)
			print('Created Index')
		created = True
	except Exception as ex:
		print(str(ex))
	finally:
		return created

def parse_result(card):
	url_recipe = card.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
	page_recipes = requests.get(url_recipe)
	recipe = BeautifulSoup(page_recipes.text, 'html.parser')
	body = recipe.find("article", {'class':'content-body'})
	title = body.find('h1').text
	details = recipe.find("div", {'class':'entry-content'})
				
	ingredients = []
	for li in details.find('ul').find_all('li'):
		ingredients.append({'step': li.text.strip()})

	preparations = []
	for p in details.find_all('p'):
		preparations.append(p.text)

	rec = {'title': title, 'ingredients': ingredients, 'description': ' '.join(preparations)}

	return json.dumps(rec)

def store_record(elastic_object, index_name, record):
	is_stored = True
	try:
		outcome = elastic_object.index(index=index_name, doc_type='food', body=record)
		print(outcome)
	except Exception as ex:
		print('Error in indexing data')
		print(str(ex))
		is_stored = False
	finally:
		return is_stored

if __name__ == '__main__':
	logging.basicConfig(level=logging.ERROR)

	url = 'https://guiadacozinha.com.br/category/almoco-de-domingo/'
	page = requests.get(url)

	if page.status_code == 200:
		soup = BeautifulSoup(page.text, 'html.parser')
		cards = soup.find_all(class_='recipe-card')

		if len(cards) > 0:

			es = connect_elasticsearch()

			for card in cards:
				sleep(2)
				result = parse_result(card)
				if es is not None:
					if create_index(es, 'recipes'):
						out = store_record(es, 'recipes', result)
						print('Successfully')