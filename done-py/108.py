from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/108.html'), 'html.parser')

data = [[result.find('p').text if result.find('p') else '', result.find('a')['href'] if result.find('a') else '']
        for result in  soup.find_all('figure')]

pd.DataFrame(data).to_csv('scraped-csv/108.csv', index=False)