from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/126-2.html'), 'html.parser')

data = [[result.find('a')['href'] if result.find('a') else '',
         result.find_all('strong')[1].text if result.find('strong') else '']
        for result in soup.find_all('div', class_='uagb-columns__inner-wrap')]

pd.DataFrame(data).to_csv('scraped-csv/126-2.csv', index=False)