from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/235.html'), 'html.parser')

data = [[result.find('p', class_='verticals').text if result.find('p', class_='verticals') else '',
         result.find('p', class_='location').text if result.find('p', class_='location') else '']
        for result in soup.find_all('div', class_='company-card')]

pd.DataFrame(data).to_csv('scraped-csv/235.csv', index=False)
