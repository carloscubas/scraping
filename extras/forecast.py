import requests
import pprint
from bs4 import BeautifulSoup

# https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3

url = 'http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")

forecast_items = seven_day.find_all(class_="tombstone-container")

for forecast_item in seven_day.find_all(class_="tombstone-container"):
	period = forecast_item.find(class_="period-name").get_text()
	short_desc = forecast_item.find(class_="short-desc").get_text()
	temp = forecast_item.find(class_="temp").get_text()

	print(period)
	print(short_desc)
	print(temp)
	print("------------")