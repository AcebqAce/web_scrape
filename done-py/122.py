from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/122.html'), 'html.parser')

data = [[result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='company__thumbnail company__thumbnail-link')]

pd.DataFrame(data).to_csv('scraped-csv/122.csv', index=False)