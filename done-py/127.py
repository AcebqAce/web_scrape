from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/127.html'), 'html.parser')

data = [[result.find('h3').text if result.find('h3') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='sc-7db659da-5')]

pd.DataFrame(data).to_csv('scraped-csv/127.csv', index=False)