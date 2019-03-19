#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:11:24 2019

@author: cubas
"""
import requests
from bs4 import BeautifulSoup

url = "http://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []
for tr in soup.findAll('table')[2].findAll('tr'):
    cols = tr.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    
print(data)