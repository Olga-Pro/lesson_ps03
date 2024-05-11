# материал урока ps03
from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"  # сайт с цитататами
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")  # поиск всех ссылок на сайте ("a" - тэг ссылки - абсолютной и относительной)
for link in links:
    print(link.get("href"))  # выбрать ссылки с тэгом "href"

text = soup.find("span", class_="text")  # поиск класса text в тэге span
print(text)

texts = soup.find_all("span", class_="text")  # поиск всех классов text в тэге span
print(texts)

authors = soup.find_all("small", class_="author")  # поиск всех авторов
print(authors)

for i in range(len(texts)):
    print(f"Цитата номер {i+1}:")
    print(texts[i].text)
    print(f"Автор цитаты - {authors[i].text}\n")
