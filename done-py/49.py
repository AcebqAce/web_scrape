from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/49.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a')
data = []

for result in results:
    name_element = result.find('h4')
    name = name_element.text if name_element else ''

    web = result.get('href')

    status = result.get('data-status', '')

    print(status)

    data.append([name, web, status])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/49.csv', index=False)