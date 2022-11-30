from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl as xls

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html5lib")

col = doc.tbody
row = col.contents

prices = {}

for tr in row[:10]:
	name, price = tr.contents[2:4]
	fixed_name = name.p.string
	fixed_price = price.a.string

	prices[fixed_name] = fixed_price

print(prices)



