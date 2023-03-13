from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/116.html'), 'html.parser')

data = [[result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='entry-content')]

pd.DataFrame(data).to_csv('scraped-csv/116.csv', index=False)