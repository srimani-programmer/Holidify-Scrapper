import requests
import csv
import re
from bs4 import BeautifulSoup

count = 1001

while True:
    res = requests.get('https://www.holidify.com/places/shimla/mall-road-shimla-sightseeing-{}.html'.format(count))

    soup = BeautifulSoup(res.text, 'lxml')

    resultArray = list()

    placeName = soup.find_all('div', class_="col-md-12 col-xs-12 nopadding sectionBorder desktopFlex")

    # Getting the Place Name
    def getPlaceName():
        for i in placeName:
            resultArray.append(i.h1.text)

    getPlaceName()

    cityData = soup.find_all('a', class_="smallerText")

    for i in cityData:
        resultArray.append(i.text)

    about = soup.find_all('div',class_="col-md-8 col-xs-12 paddingSet")

    # getting the About Data
    def getAboutData():
        data = None
        aboutData = ""
        try:
            for i in about:
                data = i.find_all('div', class_='readMoreText')
                for i in data:
                    aboutData += i.p.text

            resultArray.append(aboutData)
        except Exception as e:
            resultArray.append('Data Not Available')
        #print(temp)

    getAboutData()

    def getAboutMoreData():
        data = None
        try:
            for i in about:
                data = i.find_all('p',attrs={'class':'textColor infoSpace'})
                #print(data[1])
            resultArray.append(str(data[1])[32:len(data)-6])
        except Exception as e:
            resultArray.append('Data Not available')


    getAboutMoreData()

    resultArray.append('Null')

    timeRequired = soup.find_all('div', class_="col-md-12 col-xs-12 nopadding atfMarginBottomMobile")

    def getTimeRequired():
        for i in timeRequired:
            paragraphData = i.find_all('p', class_="objText")
            try:
                data = str(paragraphData[1])
                data = re.findall("[0-9].* hours", data)
                resultArray.append(data[0].strip())
            except Exception as e:
                resultArray.append('Null')

    getTimeRequired()

    def timings():
        data = ""
        timing = soup.find_all('span', class_="objText")
        for i in timing:
            data += i.text
        data = data.strip()
        if('AM' in data or 'PM' in data):
            resultArray.append(data)
        else:
            resultArray.append('Null')
    timings()

    # print(resultArray)

    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(resultArray)
    
    print('{} City Data Added to File Sucessfully...!😇😎'.format(count))
    count +=1
    if(count == 3400):
        break
        
