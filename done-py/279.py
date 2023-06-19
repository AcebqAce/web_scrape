from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/279.html'), 'html.parser')

data = [[result.text.split(' is')[0]]
        for result in soup.find_all('div', class_='back-desc')]

pd.DataFrame(data).to_csv('scraped-csv/279.csv', index=False)