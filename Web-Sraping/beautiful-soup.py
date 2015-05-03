from bs4 import BeautifulSoup
import requests
from time import sleep

base_url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page="

NUM_PAGES = 31

for page_num in range(1,NUM_PAGES + 1):
	print "souping page",page_num,',',len(books)
	url = base_url + str(page_num)
	soup = BeautifulSoup(requests.get(url).text,'html5lib')

# Do some sort of processing
# for td in soup('td','thumbtext'):
# 	if not is_video(td):
# 		books.append(book_info(td))

sleep(30)