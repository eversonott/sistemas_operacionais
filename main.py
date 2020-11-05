import time
from concurrent.futures.thread import ThreadPoolExecutor

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from TomatoesDTO import TomatoesDTO
import csv

# Main
genre = int(input("""Menu:
               1 - Ação
               2 - Animação
               3 - Arte e Estrangeiro
               4 - Clássicos
               5 - Comédia
               6 - Documentário
               7 - Drama
               8 - Terror
               9 - Crianças e Familia
               10 - Mistério
               11 - Romance
               12 - Sci-fi e Fantasia
               13 - Todos os gêneros
               Escolha o gênero do filme: """))


def genre_number_switcher(x):
    switcher = {
        1: "1",
        2: "2",
        3: "4",
        4: "5",
        5: "6",
        6: "8",
        7: "9",
        8: "10",
        9: "11",
        10: "13",
        11: "18",
        12: "14",
        13: "1;2;4;5;6;8;9;10;11;13;18;14"
    }
    return switcher.get(x, "1;2;4;5;6;8;9;10;11;13;18;14")


def write_csv(rotten_tomatoes_list):
    with open('lista_filmes.csv', 'w', newline='') as csv_file:
        fieldnames = ['Nome filme', 'audiência']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for movie in rotten_tomatoes_list:
            writer.writerow({movie.name, movie.audiencescore})


url = 'https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=100' \
      '&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=' \
      + str(genre_number_switcher(genre)) + '&sortBy=release'
driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)

# Busca na pagina principal todos os links dos filmes
listMovie = driver.find_elements_by_tag_name("a")
links = [link.get_attribute('href') for link in listMovie]

# Cria uma lista com urls distintas
movieList = set()
for movieLink in links:
    if movieLink is not None:
        if "/m/" in movieLink:
            movieList.add(movieLink)

# Cria uma lista de objetos e faz o scrapping dos atributos da pagina do filme
tomatoesList = []
# def scrapping_movie_page(movieUrl):
for movieUrl in movieList:
    driver.get(movieUrl)
    time.sleep(2)
    try:
        name = driver.find_element_by_css_selector("h1[data-qa='score-panel-movie-title']").text
        percentage = driver.find_elements_by_class_name("mop-ratings-wrap__percentage").__getitem__(1).text
    except IndexError:
        percentage = "Ainda não possui nota da audiência"
    tomatoesList.append(TomatoesDTO(name, percentage))

#tomatoes_list_sort_by_score = sorted(tomatoesList, key=lambda tomatoes: tomatoesList.audiencescore)
write_csv(tomatoesList)

# with ThreadPoolExecutor() as executor:
#    futures = []
#    for url in movieList:
#       executor.submit(scrapping_movie_page, url)
