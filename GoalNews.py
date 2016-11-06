import requests
from bs4 import BeautifulSoup


def spider(search, max_page):
    page = 1
    number = 0
    while page <= max_page:
        url = "http://www.goal.com/en/news/archive/"+str(page)+"?ICID=OP"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # print(page)
        for found in soup.findAll('div', {'class': 'articleInfo'}):
            link = found.find('a')
            href = "http://www.goal.com" + link.get('href')
            text = link.string

            if search in text:
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


spider("", 1)
