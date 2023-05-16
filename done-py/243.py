from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/243.html'), 'html.parser')

data = [[result.find('span').text if result.find('span') else '',
         result['href']]
        for result in soup.find_all('a', class_='open-in')]

pd.DataFrame(data).to_csv('scraped-csv/243.csv', index=False)
