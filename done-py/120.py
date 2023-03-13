from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/120.html'), 'html.parser')

data = [[result.find('div', class_='button white-button').text if result.find('div', class_='button white-button') else '',
         result.find('a')['href'] if result.find('a') else '']
         for result in soup.find_all('div', class_='work-v2 w-dyn-item')]

pd.DataFrame(data).to_csv('scraped-csv/120.csv', index=False)