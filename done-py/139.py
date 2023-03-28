from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/139.html'), 'html.parser')

data = [[result.find('td', class_='company-name').text.replace('\t','').strip() if result.find('td', class_='company-name') else '',
         result.find_all('span')[1].text.split("						")[-1].strip() if result.find_all('span') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('tr', class_='more')]

pd.DataFrame(data).to_csv('scraped-csv/139.csv')