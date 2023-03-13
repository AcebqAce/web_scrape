from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/119.html'), 'html.parser')

data = [[result.find('div', class_='portfolio-item__title').text if result.find('div', class_='portfolio-item__title').text else '',
         result.find('a')['href'] if result.find('a') else '']
         for result in soup.find_all('div', class_='portfolio-item__wrap')]

pd.DataFrame(data).to_csv('scraped-csv/119.csv', index=False)