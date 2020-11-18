import csv
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from concurrent.futures.thread import ThreadPoolExecutor

from TomatoesDTO import TomatoesDTO
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

# Main
from selenium.webdriver.support.wait import WebDriverWait

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

print("Isso pode demorar um poquinho... Aproveite esse tempo para buscar um cafézinho!")


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

url = 'https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=100' \
      '&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=' \
      + str(genre_number_switcher(genre)) + '&sortBy=release'
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(url)
time.sleep(10)


def write_csv(rotten_tomatoes_list):
    with open('lista_filmes.csv', 'w', newline='') as csv_file:
        fieldnames = ['Nome filme', 'Nota audiencia']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        try:
            for movie in rotten_tomatoes_list:
                writer.writerow({'Nome filme': movie.name, 'Nota audiencia': movie.audiencescore})
        except Exception:
            print("Algo deu errado na geração do arquivo. Contate os desenvolvedores!")
    print("Arquivo gerado com sucesso!")


#Clica no botão show more até acabar de carregar todos os filmes
#wait = WebDriverWait(driver, 40)
flag = True
while flag:
    try:
        button = driver.find_element_by_xpath('//*[@id="show-more-btn"]/button')
        button.click()
        time.sleep(5)
    except NoSuchElementException:
        flag = False

# Busca na pagina principal todos os links dos filmes
listMovie = driver.find_elements_by_tag_name("a")
links = [link.get_attribute('href') for link in listMovie]

# Cria uma lista com urls distintas
print("Start")
movieList = set()
for movieLink in links:
    if movieLink is not None:
        if "/m/" in movieLink:
            if not "null" in movieLink:
                movieList.add(movieLink)

# Cria uma lista de objetos e faz o scrapping dos atributos da pagina do filme
tomatoesList = []
def scrapping_movie_page(movieUrl):
    #for movieUrl in movieList:
    driver.get(movieUrl)
    time.sleep(2)
    try:
        name = driver.find_element_by_css_selector("h1[data-qa='score-panel-movie-title']").text
        percentage = driver.find_elements_by_class_name("mop-ratings-wrap__percentage").__getitem__(1).text
    except IndexError or NoSuchElementException:
        percentage = "Ainda não possui nota da audiência"
        try:
            name = driver.find_element_by_css_selector("h1[data-qa='score-panel-movie-title']").text
        except NoSuchElementException:
            print("Parece que deu problema em algum filme")

    tomatoesList.append(TomatoesDTO(name, percentage))
    return tomatoesList

#tomatoes_list_sort_by_score = sorted(tomatoesList, key=lambda tomatoes: tomatoesList.audiencescore)

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(scrapping_movie_page, url) for url in movieList]
    results = []
    for result in futures:
        results.append(result)


write_csv(tomatoesList)




