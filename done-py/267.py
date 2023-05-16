from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/267.html'), 'html.parser')

data = [[result.find('div', class_='cmaMaZaQ').get('title').replace('[center]', '').replace('[b]', '').replace('[/b]', '').replace('[/center]', '').strip() if result.find('div', class_='cmaMaZaQ') else '',
         result.find('div', class_='cmaMaZaR').get('title').replace('[center]', '').replace('[/center]', '').strip() if result.find('div', class_='cmaMaZaR') else '',
         result.find('div', class_='cmaMaZaI').get('title') if result.find('div', class_='cmaMaZaI') else '',
         result.find('div', class_='cmaMaZaL').get('title') if result.find('div', class_='cmaMaZaL') else '',
         result.find('div', class_='cmaMaZaN').get('title') if result.find('div', class_='cmaMaZaN') else '']
        for result in soup.find_all('div', class_='cmaQoaV')]

pd.DataFrame(data).to_csv('scraped-csv/267.csv', index=False)