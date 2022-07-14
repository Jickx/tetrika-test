from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from typing import Union


URL_BASE = 'https://ru.wikipedia.org/'


def download_page(url: str) -> str:
    return urlopen(url).read()


def get_animal_list(html: str) -> list:
    animals_list = []
    soup = bs(html, 'html.parser')
    animals = soup.find("div", {"class": "mw-category"}).find_all('li')
    for animal in animals:
        animals_list.append(animal.text)
    return animals_list


def get_next_url(html: str) -> Union[str, None]:
    soup = bs(html, 'html.parser')
    link = soup.find('a', text='Следующая страница')
    if link:
        return urljoin(URL_BASE, link['href'])
    else:
        return None


def get_animal_count(animal_names: list[str]):
    letters =\
        'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'\
        + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    animals_count = {i: 0 for i in letters}
    for animal in animal_names:
        animals_count[animal[0].upper()] += 1
    return animals_count


def main():
    url_suffix = '/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%'\
        '80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%'\
        'BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%'\
        'D0%90&filefrom=%D0%90&subcatuntil=%D0%90#mw-subcategories'
    animals_names = []
    ctr = 0
    next_url = urljoin(URL_BASE, url_suffix)
    while True:
        page_html = download_page(next_url)
        animals = get_animal_list(page_html)
        animals_names.extend(animals)
        ctr += 1
        next_url = get_next_url(page_html)
        print(f'========  Добавлено страниц: {ctr:3}  ========')
        if not next_url:
            break
    animals_count = get_animal_count(animals_names)
    print(animals_count)
    with open('file.csv', 'w') as file:
        file.write(str(animals_names))


if __name__ == '__main__':
    main()
