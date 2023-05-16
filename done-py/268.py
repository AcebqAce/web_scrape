from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/268.html'), 'html.parser')

data = [[result.find('a', class_='card-click-overlay')['href'] if result.find('a') else '']
        for result in soup.find_all('div', class_='js-list-item')]

pd.DataFrame(data).to_csv('scraped-csv/268.csv', index=False)