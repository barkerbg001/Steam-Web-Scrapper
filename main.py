from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

url = "https://store.steampowered.com/search/?term=Minecraft+Dungeons"
result = requests.get(url)
doc = BeautifulSoup(result.content, "html.parser")
divswithids = doc.find(id='search_result_container')
data = divswithids.find_all(class_='responsive_search_name_combined')
print("=========================================")

table = []

for a in data:
    head = a.find(class_='title')
    priceheader = a.find(class_='col search_price_discount_combined responsive_secondrow')
    price = priceheader.find(class_='col search_price responsive_secondrow')
    try:
        row= [head.string, price.string.strip()]
        print(row)
        table.append(row)
    except:
        print("Woops")

df = pd.DataFrame(table,columns=['a', 'b'])
df.to_excel('steam.xlsx', index=False, header=False)