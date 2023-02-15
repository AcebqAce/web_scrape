from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/58.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a')
data = []

for result in results:
    web = result.get('href')

    name_element = result.find('p')
    name = name_element.text.strip().split(" is ")[0] if name_element else ''
    name = name.replace('  ', '')
    name = name.replace('\n', '')

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/58.csv', index=False)