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

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])
df.to_excel('pandas_to_excel_no_index_header.xlsx', index=False, header=False)
for a in data:
    head = a.find(class_='title')
    priceheader = a.find(class_='col search_price_discount_combined responsive_secondrow')
    price = priceheader.find(class_='col search_price responsive_secondrow')
    try:
        print(head.string)
        print(price.string.strip())
    except:
        print("Woops")