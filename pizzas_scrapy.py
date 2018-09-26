import requests
from bs4 import BeautifulSoup
import csv


page = requests.get('https://vituccio.com')
soup = BeautifulSoup(page.content, 'html.parser')
itens = soup.find_all("ul", {"class": "pizza-flavers"})

file = csv.writer(open("pizzas.csv", "w"))
file.writerow(["Name", "Description", "Price", "Image"])  # Write column headers as the first line

for item in itens:
    detalhes = item.find_all("li")
    for item_detalhe in detalhes:
        name = item_detalhe.find("h5")
        description = item_detalhe.find("span")
        price = item_detalhe.find("div", {"class": "pizza-price"})
        image = item_detalhe.find("div", {"class": "menu-img"})
        print(name.text)
        print(description.text)
        print(price.text)
        if image:
            print(image.contents[0].attrs['src'])
            file.writerow((name.text, description.text, price.text, image.contents[0].attrs['src']))
        else:
            print("no image")
            file.writerow((name.text, description.text, price.text, image))