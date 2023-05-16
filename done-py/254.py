from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/254.html'), 'html.parser')

data = [[result.text, result['href']]
        for result in soup.find_all('a')]

pd.DataFrame(data).to_csv('scraped-csv/254.csv', index=False)
