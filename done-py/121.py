from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/121.html'), 'html.parser')

data = [[result.find('a').text if result.find('a') else '',
         result.find('a', href=True)['href'] if result.find('a', href=True) else '']
         for result in soup.find_all('div', class_='portfolio-item')]

pd.DataFrame(data).to_csv('scraped-csv/121.csv', index=False)