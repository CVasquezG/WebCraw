import requests
from bs4 import BeautifulSoup


def spider(max_page):
    page = 1
    while page <= max_page:
        url = "http://www.goal.com/en/rumours/last/72?page="+str(page)+"&ICID=OP"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('h3', {'class': 'column'}):
            rumours = link.string
            if "Chelsea" in rumours:
                print(rumours)

        page += 1

spider(3)
