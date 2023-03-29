import requests
from bs4 import BeautifulSoup


# product_code = input("Podaj kod produktu: ")
product_code = "114861667"
url= f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
opinions = page.select("div.js_product-review")
print(len(opinions))
print(type(opinions))
for opinion in opinions:
    print(opinion["data-entry-id"])