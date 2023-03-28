from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/146.html'), 'html.parser')

data = [[result.find('h2').text if result.find('h2') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='et_pb_text_inner')]

pd.DataFrame(data).to_csv('scraped-csv/146.csv', index=False)