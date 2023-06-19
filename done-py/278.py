from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/278.html'), 'html.parser')

data = [[result.find('a').get('title') if result.find('a') else '',
         result.find_all('dd')[1].text.split(', ')[-1] if result.find_all('dd') else '',
         result.find_all('span')[-1].text if result.find_all('span') else '']
         for result in soup.find_all('li', class_='css-bjn8wh')]

pd.DataFrame(data).to_csv('scraped-csv/278.csv', index=False)