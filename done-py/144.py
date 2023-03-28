from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/144.html'), 'html.parser')

data = [[result.find('span', class_='tab_box_title').text if result.find('span', class_='tab_box_title') else '',
         result.find('span', class_='tab_box_big_title').text if result.find('span', class_='tab_box_big_title') else '']
        for result in soup.find_all('div', class_='tab_box_text')]

pd.DataFrame(data).to_csv('scraped-csv/144.csv', index=False)