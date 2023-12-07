import requests
import bs4

url="http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm"
saturs=requests.get(url)

if saturs.status_code==200:
    lapa=bs4.BeautifulSoup(saturs.content, "html.parser")
    #print(lapa)
    h1_virsraksti=lapa.find_all("h1")
    print(h1_virsraksti[0].string)