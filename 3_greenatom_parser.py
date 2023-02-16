from bs4 import BeautifulSoup as BS
from urllib.request import Request, urlopen
from typing import Tuple


def read_url(url: str) -> str:
    """Запрашивает переданный url и возвращает html-код страницы"""
    request = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request) as page:
        bytes = page.read()
        html_page = bytes.decode("utf-8")
        return html_page

def parse_html(html_page: str) -> Tuple[int, int]:
    """Подсчитывает и возвращает количество тегов и количество тегов с атрибутами"""
    soup = BS(html_page, features='html.parser')
    html = soup.find_all()
    tags = len([line.name for line in html])
    tags_with_attrs = len([line.attrs for line in html if line.attrs])
    return tags, tags_with_attrs

def main():
    """Выводит количество тегов и количество тегов с атрибутами"""
    html_page = read_url('https://greenatom.ru/')
    tags, tags_with_attrs = parse_html(html_page)
    print(tags, tags_with_attrs)

if __name__ == '__main__':
    main()
