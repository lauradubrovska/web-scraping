import requests
import bs4

url="https://en.wikipedia.org/wiki/Frank_Ocean"
saturs=requests.get(url)

if saturs.status_code==200:
    saturs=bs4.BeautifulSoup(saturs.content,"html.parser")
    valodas=saturs.find_all(class_="interlanguage-link")
    #print(valodas[5])
    res=[]
    for a in valodas:
        row = a.findChild("a")
        #print(row)
        res.append(row)
    dati=[]
    for words in res:
         row=[]
         language=words.attrs['title']
         short=words.attrs['lang']
         row.append(language)
         row.append(short)
         dati.append(row)

print(dati)

