from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/114.html'), 'html.parser')

data = [[r.find('div',class_='table-value company-name').text.strip() if r.find('div',class_='table-value company-name') else '', 
         r.find_all('div',class_='table-value')[3].text.strip()] 
         for r in soup.find_all('div',class_='grid table-row')]

pd.DataFrame(data).to_csv('scraped-csv/114.csv', index=False)
