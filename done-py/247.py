from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/247.html'), 'html.parser')

data = [[result.get('alt').split('logo for ')[-1].strip()]
        for result in soup.find_all('img', class_='logo')]

pd.DataFrame(data).to_csv('scraped-csv/247.csv', index=False)

