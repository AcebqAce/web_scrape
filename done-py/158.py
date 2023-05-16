from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/158.html'), 'html.parser')

data = [[result.text.replace('\t', '').strip(),
         result.get('data-firm_id')]
        for result in soup.find_all('a', class_='btn btn-light add_tooltip')]

pd.DataFrame(data).to_csv('scraped-csv/158.csv', index=False)
