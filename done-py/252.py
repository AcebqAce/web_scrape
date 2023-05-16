from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/252.html'), 'html.parser')

data = [[result.find('h3').text if result.find('h3') else '',
         result.find('a', class_='pushed')['href'] if result.find('a', class_='pushed') else '']
        for result in soup.find_all('div', class_='t-entry-visual-cont')]

pd.DataFrame(data).to_csv('scraped-csv/252.csv', index=False)

