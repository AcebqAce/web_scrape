from bs4 import BeautifulSoup
import pandas as pd

with open ('downloaded-html/110.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h6', class_='font_6')
data = []

for result in results:
    name_element = result.find('span', style='font-weight:bold; letter-spacing:0.02em;')
    name = name_element.text if name_element else ''

    web_element = result.find('span', style='text-decoration:underline;')
    web = web_element.text if web_element else ''

    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/110.csv', index=False)