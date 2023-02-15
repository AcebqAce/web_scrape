from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/59-3.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a')
data = []

for result in results:
    web = result.get('href')

    name = result.text

    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/59(3).csv', index=False)