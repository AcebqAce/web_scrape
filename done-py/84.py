from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/84.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('p', class_='work-name')

for result in results:
    name = result.text

    print(name)