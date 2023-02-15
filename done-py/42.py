from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/42-2.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a')
data = []

for result in results:
    web = result.get('href')
    
    country_element = result.find('div', class_='text-block-16')
    country = country_element.text if country_element else ''

    data.append([web, country])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/42(2).csv', index=False)