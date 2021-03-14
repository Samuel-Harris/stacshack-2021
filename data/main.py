import requests
from bs4 import BeautifulSoup
import csv

# urls = ["https://pickupline.net/food-pick-up-lines/chipotle-pick-up-lines/", "https://pickupline.net/food-pick-up-lines/subway-pick-up-lines/", "https://pickupline.net/character-based-pick-lines/superheroes-villains-pick-up-lines/"]
url_base = "https://pickupline.net/"
category = "character-based-pick-lines/"
topics = ["snake-pick-up-lines/","peanuts-pick-up-lines-charlie-brown-and-snoopy/","cow-pick-up-lines/","jurassic-dinosaur-and-prehistoric-caveman-pick-up-lines/",
          "insect-and-bug-pick-up-lines/","vapire-pick-up-lines/","alien-pick-up-lines/","cat-pick-up-lines/",
          "animal-pick-up-lines/","superheroes-villains-pick-up-lines/","pirate-pick-up-lines/","elf-pick-up-lines/"]

row = []

for topic in topics:
    url = url_base + category + topic
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    texts = soup.find_all('td', class_='column-1')
    for item in texts:
        text = item.get_text().replace('"', "'")
        print(text)
        row.append(text)
    print()

filename = category.replace('/', '.csv')
print(filename)
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(row)
