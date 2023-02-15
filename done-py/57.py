from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/57.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='pf_item-wrapper w-dyn-item')
data = []

for result in results:
    country_element = result.find_all('div', class_='fitler_label_search')
    country = country_element[1].text if country_element else ''

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    status_element = result.find_all('div', class_='fitler_label_search')
    status = status_element[2].text if status_element else ''

    data.append([country, web, status])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/57.csv', index=False)