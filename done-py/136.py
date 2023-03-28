from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/136.html'), 'html.parser')

data = [[result.text]
        for result in soup.find_all('div', class_='title')]

pd.DataFrame(data).to_csv('scraped-csv/136.csv', index=False)