from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/51.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='venture-grid_item__2w5dT')
data = []

for result in results:
    name_element = result.find('h2')
    name = name_element.text if name_element else ''

    status_element = result.find('p', class_='venture-tile_status__3F-Dx')
    status = status_element.text if status_element else ''

    data.append([name, status])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/51.csv', index=False)