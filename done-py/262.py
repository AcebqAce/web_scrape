from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/262.html'), 'html.parser')

data = [[result.find('div', class_='').text.replace('\n', '').replace('  ', ' ').strip() if result.find('div', class_='') else '',
         result.find_all('div', class_='')[1].text.replace('\n', '').strip() if len(result.find_all('div', class_='')) > 1 else '',
         result.find_all('div', class_='')[2].text.replace('\n', '').strip() if len(result.find_all('div', class_='')) > 2 else '']
        for result in soup.find_all('div', class_='SpeakersStyles__speakerInfo___jO_tO')]

pd.DataFrame(data).to_csv('scraped-csv/262.csv', index=False)