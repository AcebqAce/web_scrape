from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/86.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='company-name-link')
data = []

for result in results:
    name = result.text

    web = result['href']

    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/86.csv', index=False)