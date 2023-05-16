from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/272.html'), 'html.parser')

data = [[result.find('a', class_='js-list-item-button')['href'] if result.find('a', class_='js-list-item-button') else '',
         result.find('div', class_='sw-pre-text-container align-center').text.replace('\t', '').strip() if result.find('div', class_='sw-pre-text-container align-center') else '',
         result.find_all('div')[8].text.replace('\n', '').replace('          ', '').strip() if len(result.find_all('div')) > 8 else '',
         result.find_all('div', class_='sw-pre-text-container align-center')[1].text.replace('\t', '').strip() if len(result.find_all('div', class_='sw-pre-text-container align-center')) > 1 else '']
        for result in soup.find_all('div', class_='ag-row-no-focus')]

pd.DataFrame(data).to_csv('scraped-csv/272.csv', index=False)