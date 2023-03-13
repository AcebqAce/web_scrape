from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/113.html'), 'html.parser')

data = [[result.find('h5').text if result.find('h5') else '',
         result.find('a')['href'] if result.find('a') else '']
         for result in soup.find_all('div', class_='property-location-details-row_property__EJOEz')]

pd.DataFrame(data).to_csv('scraped-csv/113.csv', index=False)
