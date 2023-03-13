from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/76.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a')

for result in results:
    web = result['href']

    print(web)