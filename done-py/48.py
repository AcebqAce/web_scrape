from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/48.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h3')
data = []

for result in results:
    name = result.text

    print(name)