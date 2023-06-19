from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/281.html'), 'html.parser')

data = [[result.find('a').get('href', '')] 
        for result in soup.find_all('div', class_='box box-logo')]


pd.DataFrame(data).to_csv('scraped-csv/281.csv', index=False)