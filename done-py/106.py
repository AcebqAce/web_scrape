from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/106.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('li', class_='company')
data = []

for result in results:
    name = result.text.strip().split(', ')[0]

    web = result.get('data-url')

    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/106.csv', index=False)