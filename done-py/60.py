from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/60.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='list-item-content')
data = []

for result in results:
    name_element = result.find('strong')
    name = name_element.text if name_element else ''

    desc_element = result.find('p')
    desc = desc_element.text.strip().split(' – ')[-1] if desc_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    data.append([name, desc, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/60.csv', index=False)