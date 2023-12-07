import requests

url="http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm"
saturs=requests.get(url)
#print(saturs.text)

f=open("result.txt","w")
f.write(saturs.text)
f.close