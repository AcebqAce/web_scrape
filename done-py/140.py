from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/140.html'), 'html.parser')

data = [[result.find('a').text if result.find('a') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='opacity')]

pd.DataFrame(data).to_csv('scraped-csv/140.csv', index=False)