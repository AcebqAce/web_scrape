from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/128.html'), 'html.parser')

data = [[result['href']]
         for result in soup.find_all('a', class_='j7pOnl')]

pd.DataFrame(data).to_csv('scraped-csv/128.csv', index=False)