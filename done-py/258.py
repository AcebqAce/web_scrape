from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/258.html'), 'html.parser')

data = [[result.find('h3').text if result.find('h3') else '',
         result.find('p').text if result.find('p') else '']
        for result in soup.find_all('div', class_='spk-info')]

pd.DataFrame(data).to_csv('scraped-csv/258.csv', index=False)
