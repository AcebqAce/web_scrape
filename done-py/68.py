from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/68.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h6')
data = []
for result in results:
    name = result.text

    website_element = result.find_next('a')
    website = website_element['href'] if website_element else ''

    data.append([name, website])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/68.csv', index=False)