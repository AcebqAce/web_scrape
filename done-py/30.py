from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/30.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='portfolio-item w-dyn-item')
data = []

for result in results:
    name_element = result.find('div', class_='portfolio-item-title')
    name = name_element.text if name_element else ''

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/30.csv', index=False)