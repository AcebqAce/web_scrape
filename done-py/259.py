from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/259.html'), 'html.parser')

data = [[result.text.replace('\t', '').replace('\r\n', '').strip(), result.find('span').text if result.find('span') else '']
        for result in soup.find_all('h3', class_='rpc_title')]

pd.DataFrame(data).to_csv('scraped-csv/259.csv', index=False)
