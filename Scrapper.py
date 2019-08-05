import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://www.holidify.com/places/shimla/mall-road-shimla-sightseeing-350.html')

soup = BeautifulSoup(res.text, 'lxml')

name = soup.find_all('div', class_='col-md-12 col-xs-12 nopadding sectionBorder desktopFlex')

# To get the Tourist place of the Page.
def touristPlace():
    for i in name:
        print(i.h1.text)

#touristPlace()

# Fetching the Timing for the Page

def timings():
    timing = soup.find_all('span', class_="objText")
    for i in timing:
        print(i.text)

timings()

# About

about = soup.find_all('div',class_="col-md-8 col-xs-12 paddingSet")
'''
for i in aboutMore:
    print(i.p.text)
'''
def aboutData():
    for i in about:
        data = i.find_all('div', class_='readMoreText')
        for i in data:
            print(i.p.text)

#aboutData()

# More About

for i in about:
    data = i.find_all('div', class_='readMoreText')
    print(data)

# Time Required

'''
timeReq = soup.find_all('p', class_="objText")

for i in timeReq:
    data = i.text
    print(data)
'''