from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/157.html'), 'html.parser')

data = [[result.find('h3').text if result.find('h3') else '',
         result['href']]
    for result in soup.find_all('a', class_='company')
]

pd.DataFrame(data).to_csv('scraped-csv/157.csv', index=False)