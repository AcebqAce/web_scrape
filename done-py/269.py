from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/269.html'), 'html.parser')

data = [[result.text]
        for result in soup.find_all('b')]

pd.DataFrame(data).to_csv('scraped-csv/269.csv', index=False)