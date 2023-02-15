from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/45.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('li', class_='company')
data = []

for result in results:
    name_element = result.find('img')
    if name_element:
        name = name_element.get('alt', '')

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/45.csv', index=False)