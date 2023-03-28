from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/155.html'), 'html.parser')

data = [[result['href']]
    for result in soup.find_all('a', class_='eg-invisiblebutton')
]

pd.DataFrame(data).to_csv('scraped-csv/155.csv', index=False)