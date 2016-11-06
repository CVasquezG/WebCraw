import requests
import unicodedata
from bs4 import BeautifulSoup


def spider(search, max_page):
    page = 1
    number = 0
    while page <= max_page:
        url = "http://www.goal.com/es-co/news/archive/"+str(page)+"?ICID=OP"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # print(page)
        search = remove_accents(search)
        for found in soup.findAll('div', {'class': 'articleInfo'}):
            link = found.find('a')
            href = "http://www.goal.com" + link.get('href')
            text = link.string

            if search in remove_accents(text):
                print(text)
                print(href)
                spiderinside(href)
                print('\n')

        page += 1


def spiderinside(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    author = soup.find('h2', {'class', 'author'})
    try:
        print(author.string)
    except AttributeError:
        print("not found")


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


spider("OFICIAL", 76)
