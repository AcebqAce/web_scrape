from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/88.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='page-link')
data = []

for result in results:
    name = result.get('title', '')
    web = result['href']

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/88.csv', index=False)