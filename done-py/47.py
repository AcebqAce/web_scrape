from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/47.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='rolladexitem')
data = []

for result in results:
    name_element = result.find('div', class_='headlinesmall')
    name = name_element.text if name_element else ''

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/47.csv', index=False)