from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/35.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='portfolio-item')
data = []

for result in results:
    name_element = result.find('div', class_='portfolio-title')
    name = name_element.text if name_element else ''

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    status_element = result.find('div', class_='tooltiptext')
    status = status_element.text if status_element else ''

    data.append([name, web, status])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/35.csv', index=False)