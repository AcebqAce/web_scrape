from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/50.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='land-collection-item')
data = []

for result in results:
    name_element = result.find('div', class_='list-text')
    name = name_element.text if name_element else ''

    country_element = result.find('div', class_='list-text company-country')
    country = country_element.text if country_element else ''

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    data.append([name, country, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/50.csv', index=False)