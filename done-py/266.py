from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/266.html'), 'html.parser')

data = [[result.text.replace('\n', '').replace('                                                                                ', ' ').strip(), result['href']]
        for result in soup.find_all('a', class_='af im')]

pd.DataFrame(data).to_csv('scraped-csv/266.csv', index=False)