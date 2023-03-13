from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/107.html'), 'html.parser')

results = soup.find_all('div', class_='contentdiv')
data = []

for result in results:
    name_element = result.find('h2')
    name = name_element.text if name_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/107.csv', index=False)