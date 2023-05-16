from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/236.html'), 'html.parser')

data = [[result.find('div', class_='portfolio-item-status').text.replace('\t', '').strip() if result.find('div', class_='portfolio-item-status') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='portfolio-grid-item-back')]

pd.DataFrame(data).to_csv('scraped-csv/236.csv', index=False)
