from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/132.html'), 'html.parser')

data = [[result.find('p').text if result.find('p') else '',
         result['href']]
         for result in soup.find_all('a', class_='g-grid__item')]

pd.DataFrame(data).to_csv('scraped-csv/132.csv', index=False)