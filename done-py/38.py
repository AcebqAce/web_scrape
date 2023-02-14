from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/38.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='collection-item w-dyn-item')
data = []

for result in results:
    name_element = result.find('a')
    name = name_element.text if name_element else ''

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    country_element = result.find('div', {'fs-cmsfilter-field': 'Geography'})
    country = country_element.text if country_element else ''

    status_element = result.find('div', class_='tag w-condition-invisible')
    status = status_element.text if status_element else ''
    
    data.append([name, web, country, status])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/38.csv', index=False)