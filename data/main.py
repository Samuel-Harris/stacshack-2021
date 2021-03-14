import requests
from bs4 import BeautifulSoup
import csv

urls = ["https://pickupline.net/food-pick-up-lines/chipotle-pick-up-lines/", "https://pickupline.net/food-pick-up-lines/subway-pick-up-lines/", "https://pickupline.net/character-based-pick-lines/superheroes-villains-pick-up-lines/"]
url_base = "https://pickupline.net/"
category = "food-pick-up-lines/"
topics = ["chipotle-pick-up-lines/", "subway-pick-up-lines/", "in-n-out-pick-up-lines/"]

row = []

for topic in topics:
    url = url_base + category + topic
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    texts = soup.find_all('td', class_='column-1')
    for item in texts:
        print(item.get_text())
        text = item.get_text()
        row.append(item.get_text().replace('"', "'"))
    print()

with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(row)

