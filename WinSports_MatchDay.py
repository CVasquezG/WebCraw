import requests
from bs4 import BeautifulSoup


def spider():
    url = "http://www.winsports.co/estadisticas/calendario/liga-aguila-2015-ii"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for (home, away, shome, saway) in zip(soup.findAll('div', {'class': 'local short'}),
                                          soup.findAll('div', {'class': 'visit short'}),
                                          soup.findAll('div', {'class': 'lo'}),
                                          soup.findAll('div', {'class': 'vi'})):
        hname = home.find('img').get('title')
        aname = away.find('img').get('title')
        print(hname + " " + shome.string + " vs " + saway.string + " " + aname)


spider()
