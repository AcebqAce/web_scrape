from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/137.html'), 'html.parser')

data = [[result.find('div', class_='speaker-name').text if result.find('div', class_='speaker-name') else '',
         result.find('div', class_='d-none d-lg-block speaker-title').text if result.find('div', class_='d-none d-lg-block speaker-title') else '',
         result.find('div', class_='d-none d-lg-block speaker-company').text if result.find('div', class_='d-none d-lg-block speaker-company') else '']
         for result in soup.find_all('div', class_='speaker-info-container')]

pd.DataFrame(data).to_csv('scraped-csv/137.csv', index=False)