from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/64.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', style='text-align: center;')

for result in results:
    name_element = result.find_all('div')
    name = name_element[0].text if name_element else ''

    print(name)