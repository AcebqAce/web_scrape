from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/79.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('ul')
data = []

for result in results:
    name_element = result.find('li', class_='caption')
    name = name_element.text if name_element else ''

    location_element = result.find('li', class_='location')
    location = location_element.text if location_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    data.append([name, location, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/79.csv', index=False)