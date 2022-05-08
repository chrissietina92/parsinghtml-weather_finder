import bs4
import requests


# find the up to date weather of multiple places 

weatherdict = {
    "London" : "https://www.bbc.com/weather/2643743",
    "Queenstown" : "https://www.bbc.com/weather/963516",
    "Wellington" : "https://www.bbc.com/weather/2634575"}


def getWeather(weatherUrl):
    res = requests.get(weatherUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#daylink-0 > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div.wr-day-temperature__high > span.wr-day-temperature__high-value > span > span.wr-value--temperature--c')
    return elems[0].text.strip()

def getDescrip(weatherUrl):
    res = requests.get(weatherUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#daylink-0 > div.wr-day__body > div.wr-day__weather-type-description-container > div')
    return elems[0].text.strip()

#daylink-0 > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div > span.wr-day-temperature__low-value > span > span.wr-value--temperature--c


for i in weatherdict:
    temp = getWeather(weatherdict[i])
    des = getDescrip(weatherdict[i])
    print( i + ' is ' + temp + 'C right now with ' + des)
