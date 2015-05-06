#this file does not do anything
#TLDR: use csv because you probably won't know how to handle
#fields with commas in them
import csv

with open('tab_delimited_stock_prices.txt','rb') as f:
	reader = csv.reader(f,delimiter='\t')
	for row in reader:
		data = row[0]
		symbol = row[1]
		closing_price = float(row[2])
		#process(date,symbol,closing_price)


with open('colon_delimited_stock_prices.txt','rb') as f:
	reader = csv.DictReader(f,delimiter=':')
	for row  in reader:
		date = row["date"]
		symbol = row["symbol"]
		closing_price = float(row["closing_price"])
		#do some sort of processing

today_prices = {'AAPL:90.91','MSFT':41.68,'FB':64.5}

with open('comma_delimited_stock_prices.txt','wb') as f:
	writer = csv.writer(f,delimiter = ',')
	for stock, price in today_prices.items():
		writer.writerow([stock,price])

