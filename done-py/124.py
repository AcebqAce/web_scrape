from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/124.html'), 'html.parser')

data = [[result['href'] if result['href'] else '']
        for result in soup.find_all('a', class_='item half desk-third flex dir-col center')]

pd.DataFrame(data).to_csv('scraped-csv/124.csv', index=False)