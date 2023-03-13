from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/111.html'), 'html.parser')

data = [[result.find('h3').text if result.find('h3') else '', 
         result.find('a', class_='site-link a-div has-link isAbsolute')['href'] if result.find('a', class_='site-link a-div has-link isAbsolute') else '',
         result.find('span', class_='filter').text if result.find('span', class_='filter') else '']
        for result in  soup.find_all('div', class_='single-company')]

pd.DataFrame(data).to_csv('scraped-csv/111.csv', index=False)