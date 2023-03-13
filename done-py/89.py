from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/89.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('li')
data = []

for result in results:
    name_element = result.find('div', class_='companies-v2-list-title')
    name = name_element.text if name_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    print(web)
