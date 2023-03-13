from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/100.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('p', class_='card-text')
data = []

for result in results:
    name_element = result.find('a')
    name = name_element.text if name_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/100.csv', index=False)