from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/115.html'), 'html.parser')

data = [[result.find('div', class_='jsx-1163860717 name').text if result.find('div', class_='jsx-1163860717 name') else '',
         result.find('a', class_='jsx-3941957848 container')['href'] if result.find('a', class_='jsx-3941957848 container') else '']
         for result in soup.find_all('div', class_='jsx-3941957848')]

pd.DataFrame(data).to_csv('scraped-csv/115.csv', index=False)