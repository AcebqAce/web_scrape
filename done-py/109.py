from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/109.html'), 'html.parser')

data = [[result.find('p').text if result.find('p') else '', result.find('a')['href'] if result.find('a') else '']
        for result in  soup.find_all('div', class_='portfolio-box')]

pd.DataFrame(data).to_csv('scraped-csv/109.csv', index=False)