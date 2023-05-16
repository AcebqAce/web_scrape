from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/238.html'), 'html.parser')

data = [[result.find('span', class_='notion-semantic-string').text if result.find('span', class_='notion-semantic-string') else '',
         result.find('a', class_='notion-semantic-string')['href'] if result.find('a', class_='notion-semantic-string') else '',
         result.find(]
        for result in soup.find_all('tr')]

pd.DataFrame(data).to_csv('scraped-csv/238.csv', index=False)
