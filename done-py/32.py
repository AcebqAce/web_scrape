from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/32.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('li', class_='company')
data = []

for result in results:
    name = result.get('data-name')
    web = result.get('data-website')

    data.append([name, web])

df  = pd.DataFrame(data)
df.to_csv('scraped-csv/32.csv', index=False)