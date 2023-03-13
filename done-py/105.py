from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/105.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='notion-link')
data = []

for result in results:
    name = result.text
    link = result['href']

    data.append([name, link])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/105.csv', index=False)