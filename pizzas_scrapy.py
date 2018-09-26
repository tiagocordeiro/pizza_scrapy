import requests
from bs4 import BeautifulSoup
import csv


page = requests.get('https://vituccio.com')
soup = BeautifulSoup(page.content, 'html.parser')
pizzas = soup.find_all("ul", {"class": "pizza-flavers"})

file = csv.writer(open("pizzas.csv", "w"))
file.writerow(["Name", "Description", "Price", "Image"])  # Write column headers as the first line

for pizza in pizzas:
    details = pizza.find_all("li")
    for item_details in details:
        name = item_details.find("h5")
        description = item_details.find("span")
        price = item_details.find("div", {"class": "pizza-price"})
        image = item_details.find("div", {"class": "menu-img"})
        print(name.text)
        print(description.text)
        print(price.text)
        if image:
            print(image.contents[0].attrs['src'])
            file.writerow((name.text, description.text, price.text, image.contents[0].attrs['src']))
        else:
            print("[NO IMAGE]")
            file.writerow((name.text, description.text, price.text, image))