from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/56.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='main-grid-container')
data = []

for result in results:
    name_element = result.find('h1')
    name = name_element.text if name_element else ''

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/56.csv', index=False)