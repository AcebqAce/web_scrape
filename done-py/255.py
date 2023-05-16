from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/255.html'), 'html.parser')

data = [[result.find('p', class_='c-speaker-block__name').text.replace('\t', '').strip() if result.find('p', class_='c-speaker-block__name') else '',
         result.find('p', class_='c-speaker-block__job').text if result.find('p', class_='c-speaker-block__job') else '',
         result.find('p', class_='c-speaker-block__company').text if result.find('p', class_='c-speaker-block__company') else '']
        for result in soup.find_all('div', class_='c-speaker-block__content')]

pd.DataFrame(data).to_csv('scraped-csv/255.csv', index=False)
