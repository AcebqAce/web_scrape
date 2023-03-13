from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/102.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='portfolio')
data = []

for result in results:
    name_element = result.find('p')
    name = name_element.text.strip().split(': ')[0] if name_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/102.csv', index=False)