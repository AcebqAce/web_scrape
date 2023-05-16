from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/261.html'), 'html.parser')

data = [[result.find('h4').text if result.find('h4') else '',
         result.find('h5').text if result.find('h5') else '',
         result.find('h6').text if result.find('h6') else '']
        for result in soup.find_all('div', class_='figcaption text-black')]

pd.DataFrame(data).to_csv('scraped-csv/261.csv', index=False)
