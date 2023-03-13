from bs4 import BeautifulSoup
import pandas as pd

with open ('downloaded-html/92.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='fusion-link-wrapper')
data = []

for result in results:
    name = result.get('aria-label', '')

    web = result['href']

    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/92.csv', index=False)