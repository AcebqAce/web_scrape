from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/253.html'), 'html.parser')

data = [[result.find('a').text if result.find('a') else '',
         result.find('a')['href'] if result.find('a') else '',
         result.find('span').text if result.find('span') else '']
        for result in soup.find_all('div', class_='elementor-image-box-content')]

pd.DataFrame(data).to_csv('scraped-csv/253.csv', index=False)
