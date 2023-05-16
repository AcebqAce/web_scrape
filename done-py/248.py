from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/248.html'), 'html.parser')

data = [[result.find('a').text.replace('\t', '').strip() if result.find('a') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='col-md-6')]

pd.DataFrame(data).to_csv('scraped-csv/248.csv', index=False)

