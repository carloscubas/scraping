import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)

url = 'https://www.infomoney.com.br/cryptos/cotacoes'
driver = webdriver.Firefox(executable_path = '/Users/cubas/Downloads/geckodriver')
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('table', attrs={'class':'display border-t-brown-3'})

data = []
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	data.append([ele for ele in cols if ele])
	info = [ele for ele in cols if ele]
	post = {
			"index" : info[0],
			"name" : info[1],
			"marketvalue" : info[2],
			"pricers" : info[3],
			"pricebtc" : info[4],
			"total" : info[5],
			"variation" : info[6]
	}

	id_coin = client.cubas.moedas.insert(post)
	print(id_coin)
	print("---------------")

#print(data)

driver.close()
client.close
