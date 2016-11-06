import requests
from bs4 import BeautifulSoup


def spider():
    for num in range(1, 19):
        print(num)
        url = "http://resultados.as.com/resultados/futbol/colombia_i/2016/jornada/regular_a_"+str(num)+"/"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.findAll('a', {'class': 'resultado resul_post'}):
            result = link.string
            print(result)
            link = link.get('href')
            print(link)
            try:
                spider_match_info(link + "estadisticas")
            except :
                print("No possession available")
                input()
            num += 1


def spider_match_info(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    home_team = soup.findAll('span', {'class': 'nombre-equipo local s-left'})
    away_team = soup.findAll('span', {'class': 'nombre-equipo visitante s-right'})

    pos = soup.findAll('span', {'class': 'porcentaje-posesion'})
    home_possesion = pos[0].string
    away_possesion = pos[1].string

    print(home_team[0].string + " " + home_possesion)

    print(away_team[0].string + " " + away_possesion)


spider()
