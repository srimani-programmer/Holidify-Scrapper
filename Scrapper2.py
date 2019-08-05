import requests
import csv
import re
from bs4 import BeautifulSoup

res = requests.get('https://www.holidify.com/places/shimla/mall-road-shimla-sightseeing-3502.html')

soup = BeautifulSoup(res.text, 'lxml')

placeName = soup.find_all('div', class_="col-md-12 col-xs-12 nopadding sectionBorder desktopFlex")

def getPlaceName():
    for i in placeName:
        print(i.h1.text)

getPlaceName()