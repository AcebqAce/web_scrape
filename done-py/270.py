from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/270.html'), 'html.parser')

data = [[result.find('div', class_='styles__name_rbClw').text if result.find('div', class_='styles__name_rbClw') else '',
         result.find('div', class_='styles__type_YatsV').text if result.find('div', class_='styles__type_YatsV') else '']
        for result in soup.find_all('div', class_='')]

pd.DataFrame(data).to_csv('scraped-csv/270.csv', index=False)