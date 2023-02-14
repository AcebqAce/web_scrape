from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/40.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='portfolio-button')
data = []

for result in results:
    name_element = result.find('p')
    name = name_element.text if name_element else ''
    name = name.replace('\n', '')
    name = name.replace('		', '')

    web = result.get('href')
    
    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/40.csv', index=False)