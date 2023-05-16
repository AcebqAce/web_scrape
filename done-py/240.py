from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/240.html'), 'html.parser')

data = [[result.find('h5').text if result.find('h5') else '',
         result['href']]
        for result in soup.find_all('a', class_='company-card relative my-4 w-full no-underline focus:outline-none')]

pd.DataFrame(data).to_csv('scraped-csv/240.csv', index=False)
