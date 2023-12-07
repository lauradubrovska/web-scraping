import requests
import bs4

url="https://en.wikipedia.org/wiki/Frank_Ocean"
saturs=requests.get(url)

if saturs.status_code==200:
    saturs=bs4.BeautifulSoup(saturs.content,"html.parser")
    virsraksti=saturs.find_all(class_="mw-headline") #class atrod caur inspect un select txt
    #print(find)
    for a in virsraksti:
        print(a.string)