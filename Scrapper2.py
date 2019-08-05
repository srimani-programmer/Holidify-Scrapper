import requests
import csv
import re
from bs4 import BeautifulSoup

res = requests.get('https://www.holidify.com/places/shimla/mall-road-shimla-sightseeing-3502.html')

soup = BeautifulSoup(res.text, 'lxml')

placeName = soup.find_all('div', class_="col-md-12 col-xs-12 nopadding sectionBorder desktopFlex")

# Getting the Place Name
def getPlaceName():
    for i in placeName:
        print(i.h1.text)

#getPlaceName()

about = soup.find_all('div',class_="col-md-8 col-xs-12 paddingSet")

# getting the About Data
def getAboutData():
    for i in about:
        data = i.find_all('div', class_='readMoreText')
        for i in data:
            print(i.p.text)

#getAboutData()

def getAboutMoreData():
    for i in about:
        data = i.find_all('p',attrs={'class':'textColor infoSpace'})
        print(str(data[1])[32:len(data)-6])
