from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D'\
      '0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%'\
      '8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%8'\
      '3&pagefrom=%D0%90&filefrom=%D0%90&subcatuntil=%D0%90#mw-subcategories'


def get_animal_list(url):
    animals_list = []
    html = urlopen(url)
    url = get_animals(animals_list)
    soup = bs(html, 'html.parser')
    div = soup.find_all("div", {"class": "mw-category-group"})
    for animal in div:
        animals_list.append(animal.text)
    return animals_list


def get_animals(animals_list):
    pass


animals_list = get_animal_list(url)
print(animals_list)
