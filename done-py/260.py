from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/260.html'), 'html.parser')

data = [[result.find('h4').text if result.find('h4') else '',
         result.find('h5').text if result.find('h5') else '',
         result.find('h5', class_='wedc').text if result.find('h5', class_='wedc') else '']
        for result in soup.find_all('div', class_='img-text2')]

pd.DataFrame(data).to_csv('scraped-csv/260.csv', index=False)
