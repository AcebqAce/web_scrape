from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/66.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('td', {'data-label': 'Investor name'})
data = []
for result in results:
    name_element = result.find('a')
    name = name_element.text if name_element else ''

    website_element = result.find_next('a')
    website = website_element['href'] if website_element else ''

    data.append([name, website])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/66.csv', index=False)