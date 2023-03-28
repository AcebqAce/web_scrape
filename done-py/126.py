from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/126.html'), 'html.parser')

data = [[result.find('a').text if result.find('a') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('h2', class_='uagb-post__title')]

pd.DataFrame(data).to_csv('scraped-csv/126.csv', index=False)