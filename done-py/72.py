from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/72.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='sqs-block-image-link')

for result in results:
    name = result['href']

    print(name)