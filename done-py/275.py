from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/275.html'), 'html.parser')

data = [[result.find('a').text if result.find('a') else '',
         result.find('span', class_='fundWebsite').text if result.find('span', class_='fundWebsite') else '',
         result.find('p').text.replace('\t', '').replace('View Details', '').strip() if result.find('p') else ''] 
        for result in soup.find_all('div', class_='fund')]

pd.DataFrame(data).to_csv('scraped-csv/275.csv', index=False)