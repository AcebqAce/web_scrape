from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/5.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='col-md-10')

print(results)