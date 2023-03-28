from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/151.html'), 'html.parser')

data = [[result.find('div', class_='headline-05').text if result.find('div', class_='headline-05') else '',
         result.find('a')['href'] if result.find('a') else '']
    for result in soup.find_all('div', class_='portfolio-collection-list-wrapper')
]

pd.DataFrame(data).to_csv('scraped-csv/151.csv', index=False)