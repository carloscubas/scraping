import requests
import pprint
from bs4 import BeautifulSoup

# https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3

url = 'https://weather.com/weather/tenday/l/BRSP3446:1:BR'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

data = []
table = soup.find('table', attrs={'class':'twc-table'})
print(table.prettify())

table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

print(data)