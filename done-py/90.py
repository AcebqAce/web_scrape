from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/90.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='investments-item')
data = []

for result in results:
    name_element = result.find('div', class_='small-600')
    name = name_element.text if name_element else ''

    web = result['href']

    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/90.csv', index=False)
