from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/149.html'), 'html.parser')

data = [[result.find('a').text if result.find('a') else '',
         result.find('a')['href'] if result.find('a') else '']
    for result in soup.find_all('h3', class_='et_pb_module_header')
]

pd.DataFrame(data).to_csv('scraped-csv/149.csv', index=False)