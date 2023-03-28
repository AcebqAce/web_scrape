from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/153.html'), 'html.parser')

data = [[result.find('img', class_='company-row-logo').get('alt') if result.find('img', class_='company-row-logo') else '',
         result.find('a', id='w-node-_88a8ff0e-dae1-2e1b-65d1-479f12cbc627-0d5848c6')['href'] if result.find('a', id='w-node-_88a8ff0e-dae1-2e1b-65d1-479f12cbc627-0d5848c6') else '']
    for result in soup.find_all('div', class_='company-row')
]

pd.DataFrame(data).to_csv('scraped-csv/153.csv', index=False)