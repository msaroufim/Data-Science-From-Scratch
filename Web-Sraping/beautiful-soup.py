from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.google.com").text
soup = BeautifulSoup(html,'html5lib')

print soup.find('p')

url = "http://show.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text,'html5lib') 