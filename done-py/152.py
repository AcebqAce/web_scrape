from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/152.html'), 'html.parser')

data = [[result.find('div', class_='hidden-text-op').text if result.find('div', class_='hidden-text-op') else '',
         result.find('a', class_='portfolio-item-site-link-wrapper')['href'] if result.find('a', class_='portfolio-item-site-link-wrapper') else '']
    for result in soup.find_all('div', class_='portfolio-collection-item')
]

pd.DataFrame(data).to_csv('scraped-csv/152.csv', index=False)