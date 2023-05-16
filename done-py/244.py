from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/244.html'), 'html.parser')

data = [[result['href']]
        for result in soup.find_all('a')]

pd.DataFrame(data).to_csv('scraped-csv/244.csv', index=False)

