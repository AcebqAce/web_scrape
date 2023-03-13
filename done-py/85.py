from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/85.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='description')
data = []

for result in results:
    location_element = result.find('span', class_='views-field views-field-field-region')
    location = location_element.text if location_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    data.append([location, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/85.csv', index=False)