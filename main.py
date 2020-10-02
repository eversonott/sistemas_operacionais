import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.rottentomatoes.com/top/bestofrt/')
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)