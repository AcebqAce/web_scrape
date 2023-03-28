from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/142.html'), 'html.parser')

data = [[result.find('h2').text if result.find('h2') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='list-item-content__text-wrapper')]

pd.DataFrame(data).to_csv('scraped-csv/142.csv', index=False)