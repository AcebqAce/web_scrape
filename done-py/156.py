from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/156.html'), 'html.parser')

data = [[result.find('a')['href'] if result.find('a') else '']
    for result in soup.find_all('div', class_='col-xs-6')
]

pd.DataFrame(data).to_csv('scraped-csv/156.csv', index=False)