from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/282.html'), 'html.parser')

data = [[result.get('alt')] 
        for result in soup.find_all('img', class_='d-block w-100 p-4')]

pd.DataFrame(data).to_csv('scraped-csv/282.csv', index=False)