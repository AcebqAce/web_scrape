from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/250.html'), 'html.parser')

data = [[result.find('h4').text if result.find('h4') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='company-box')]

pd.DataFrame(data).to_csv('scraped-csv/250.csv', index=False)
