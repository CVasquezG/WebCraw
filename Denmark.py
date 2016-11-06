import requests
from bs4 import BeautifulSoup


def spider():
    url = "http://www.kmdvalg.dk/main"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    for link in soup.findAll('div', {'class': 'LetterGroup'}):
        anc = link.find('a')
        href = anc.get('href')

        print(anc.getText())
        print(href)
        # spider2(href) call a second function from here that is similar to this one(making url = to herf)
        spider2(href)
        print("\n")


def spider2(linktofollow):
    url = linktofollow
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    for link in soup.findAll('tr', {'class': 'tableRowPrimary'}):
        anc = link.find('td')

        print(anc.getText())
    print("\n")


spider()
