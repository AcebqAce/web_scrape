from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/131.html'), 'html.parser')

data = [[result.find('p').text.strip().split(' is ')[0] if 'is' in result.find('p').text.strip() else 
         result.find('p').text.strip().split(' delivers ')[0] if 'delivers' in result.find('p').text.strip() else '',
         result.find('a')['href'] if result.find('a') else '']
         for result in soup.find_all('li', class_='portfolio-grid__card')]


pd.DataFrame(data).to_csv('scraped-csv/131.csv', index=False)