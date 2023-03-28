from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/135.html'), 'html.parser')

data = [[result.find('strong').text if result.find('strong') else '',
         result.find('a')['href'] if result.find('a') else '']
         for result in soup.find_all('div', class_='cc-m-hgrid-column')]

pd.DataFrame(data).to_csv('scraped-csv/135.csv', index=False)