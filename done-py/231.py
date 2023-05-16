from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/231.html'), 'html.parser')

data = [[result.find('h2').text if result.find('h2') else '',
         result['href']]
        for result in soup.find_all('a', class_='lightbox')]

pd.DataFrame(data).to_csv('scraped-csv/231.csv', index=False)
