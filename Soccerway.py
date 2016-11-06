import requests
import unicodedata
from bs4 import BeautifulSoup


def spider(teamname, name):
    url = "http://www.scoresway.com/?sport=soccer&page=competition&id=91"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    num = 1
    for link in soup.findAll('td', {'class': 'text team large-link'}):
        team = link.string
        anc = link.find('a')
        href = "http://www.scoresway.com/" + anc.get('href')
        # print(link)
        if teamname in team:
            print(team)
            print(href)
            spiderplayer(href, name)
            print("\n")
            num += 1
        if num > 20:
            break


def spiderplayer(url, name):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    name = remove_accents(name)
    for link in soup.findAll('span', {'class': 'name large-link'}):
        link2 = link.find('a')
        if name in remove_accents(link2.string):
            print(link2.string)
            spiderinfo("http://www.scoresway.com/" + link2.get('href'))


def spiderinfo(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for (link, link2) in zip(soup.findAll('dt'), soup.findAll('dd')):
        print("\t" + link.string + ": " + link2.string)
    input("Continue?")


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

teaminput = input("Enter name of team: ")
player = input("Enter last name of player: ")


spider(teaminput, player)
# input("Done. press enter to close")
