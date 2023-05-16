from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/251.html'), 'html.parser')

data = [[result.find('a').text if result.find('a') else '',
         result.find('input', class_='members_link').get('value') if result.find('input', class_='members_link') else '']
        for result in soup.find_all('li', class_='')]

pd.DataFrame(data).to_csv('scraped-csv/251.csv', index=False)
