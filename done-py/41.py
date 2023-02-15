from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/41.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('li')
data = []

for result in results:
    name_element = result.find('a')
    if name_element:
        name = name_element.get('aria-label', '')

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/41.csv', index=False)