from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/46.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('ul', class_='grid-item--accordion-meta')
data = []

for result in results:
    country_element = result.find_all('span')
    country = country_element[1].text if country_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    data.append([country, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/46.csv', index=False)