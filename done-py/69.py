from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/69.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('p')
data = []
for result in results:
    name_element = result.find('a')
    name = name_element.text if name_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    desc = result.text

    data.append([name, web, desc])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/69.csv', index=False)