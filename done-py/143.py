from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/143.html'), 'html.parser')

data = [[result.find('h3').text if result.find('h3') else '',
         result['href']]
        for result in soup.find_all('a', class_='companies-module--item--yECXE')]

pd.DataFrame(data).to_csv('scraped-csv/143.csv', index=False)