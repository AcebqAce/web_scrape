from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/145.html'), 'html.parser')

data = [[result['href']]
        for result in soup.find_all('a', class_='portfolio-element-wrapper')]

pd.DataFrame(data).to_csv('scraped-csv/145.csv', index=False)