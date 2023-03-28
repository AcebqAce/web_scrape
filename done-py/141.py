from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/141.html'), 'html.parser')

data = [[result.find('div', class_='investment-title').text if result.find('div', class_='investment-title') else '',
         result.find('div', class_='investment-location').text.split(", ")[-1].strip() if result.find('div', class_='investment-location') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='back-side')]

pd.DataFrame(data).to_csv('scraped-csv/141.csv', index=False)