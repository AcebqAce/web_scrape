from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/246.html'), 'html.parser')

data = [[result.find('span').text if result.find('span') else '',
         result.find_all('a')[1]['href'] if len(result.find_all('a')) > 1 else '',
         result.find_all('a')[2]['href'] if len(result.find_all('a')) > 2 else '',
         result.find_all('a')[3]['href'] if len(result.find_all('a')) > 3 else '',
         result.find_all('a')[4]['href'] if len(result.find_all('a')) > 4 else '']
for result in soup.find_all('div', class_='wp-block-cover__inner-container')]

pd.DataFrame(data).to_csv('scraped-csv/246.csv', index=False)


