from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/125.html'), 'html.parser')

data = [[result.find('span').text if result.find('span') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('span', class_='field-content')]

pd.DataFrame(data).to_csv('scraped-csv/125.csv', index=False)