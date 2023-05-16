from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/249.html'), 'html.parser')

data = [[result.find('span', class_='investor__name').text if result.find('span', class_='investor__name') else '',
         result.find('a')['href'] if result.find('a') else '',
         result.find_all('a')[1]['href'] if len(result.find_all('a')) > 2 else '',
         result.find_all('a')[2]['href'] if len(result.find_all('a')) > 3 else '']
        for result in soup.find_all('div', class_='investor')]

pd.DataFrame(data).to_csv('scraped-csv/249.csv', index=False)
