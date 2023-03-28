from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/133.html'), 'html.parser')

data = [[result.find('h5').text if result.find('h5') else '',
         result.find('div', {'fs-cmsfilter-field': 'location'}).text if result.find('div', {'fs-cmsfilter-field': 'location'}) else '',
         result.find('a')['href'] if result.find('a') else '']
         for result in soup.find_all('div', class_='blog34_item')]

pd.DataFrame(data).to_csv('scraped-csv/133.csv', index=False)