from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/80.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='profilelink')
data = []

for result in results:
    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    print(web)