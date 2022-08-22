from bs4 import BeautifulSoup
import requests
import numpy

url = "https://store.steampowered.com/search/?term=Minecraft+Dungeons"
result = requests.get(url)
doc = BeautifulSoup(result.content, "html.parser")
divswithids = doc.find(id='search_result_container')
data = divswithids.find_all(class_='responsive_search_name_combined')
print("=========================================")
for a in data:
    head = a.find(class_='title')
    price = a.find(class_='col search_price_discount_combined responsive_secondrow').find(class_='col search_price responsive_secondrow')
    print(head.string)
    print(price.string.strip())