from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/308.html'), 'html.parser')

data = [[result.find('div', class_='text-dark-aa font-normal text-md mt-1').text.replace('\n', '').replace('                                ', ' ').strip() if result.find('div', class_='text-dark-aa font-normal text-md mt-1') else '']
        for result in soup.find_all('header', class_='text-dark-aaaa')]

pd.DataFrame(data).to_csv('scraped-csv/308.csv', index=False)