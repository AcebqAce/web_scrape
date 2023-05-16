from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/277.html'), 'html.parser')

data = [[result.find('a').text if result.find('a') else '',
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='capital_list_items')]

pd.DataFrame(data).to_csv('scraped-csv/277.csv', index=False)