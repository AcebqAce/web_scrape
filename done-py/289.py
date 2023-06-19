from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/289.html'), 'html.parser')

data = [[result.find('span', class_='name').text if result.find('span', class_='name') else '',
         result.find_all('a')[-1]['href'] if result.find_all('a') else ''] 
        for result in soup.find_all('div', class_='slick-slide')]

pd.DataFrame(data).to_csv('scraped-csv/289.csv', index=False)