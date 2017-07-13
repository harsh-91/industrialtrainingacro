import CSV 
import requests
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


url = "https://www.sulekha.com/coaching-tuitions/indore?tp=getquotes"
r = requests.get(url)

soup = BeautifulSoup(r.content , "html5lib")

links = soup.find_all("a")

for link in links:

    print "<a href='%s'>%s</a" %(link.get("href"), link.text)
	
g_data = soup.find_all("div", {"class": "tabindex"})

for item in g_data:
   print item.contents[0].find_all("a" , {"class": "head"})[0].text
   print item.contents[1].text
   
