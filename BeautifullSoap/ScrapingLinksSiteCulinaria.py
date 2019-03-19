#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:31:34 2019

@author: cubas
"""

import requests
from bs4 import BeautifulSoup

url = 'https://guiadacozinha.com.br/category/almoco-de-domingo/'
page = requests.get(url)
recipe = BeautifulSoup(page.text, 'html.parser')

for card in recipe.find_all("div", {'class':'recipe-card'}):
    print(card.find('a')['href'])
