from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/292.html'), 'html.parser')

data = [[result.find('h2', class_='my-name').text if result.find('h2', class_='my-name') else '',
         result.find('a', class_='my-link')['href'] if result.find('a', class_='my-link') else '']
        for result in soup.find_all('div', class_='column is-4')]

pd.DataFrame(data).to_csv('scraped-csv/292.csv', index=False)