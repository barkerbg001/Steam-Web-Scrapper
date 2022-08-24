from bs4 import BeautifulSoup
import requests
import pandas as pd

table = []
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for letter in letters:
    result = requests.get("https://store.steampowered.com/search/?term=" + letter)
    doc = BeautifulSoup(result.content, "html.parser")
    divswithids = doc.find(id='search_result_container')
    data = divswithids.find_all(class_='responsive_search_name_combined')
    print("=========================================")


    for a in data:
        head = a.find(class_='title')
        priceheader = a.find(class_='col search_price_discount_combined responsive_secondrow')
        price = priceheader.find(class_='col search_price responsive_secondrow')
        try:
            row= [head.string, price.string.strip()]
            print(row)
            table.append(row)
        except:
            row= [head.string, "Discount"]
            print(row)
            table.append(row)

df = pd.DataFrame(table,columns=['a', 'b'])
df.to_excel('steam.xlsx', index=False, header=False)