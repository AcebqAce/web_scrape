from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/234.html'), 'html.parser')

data = [[''.join(result.text.split()), result['href']]
        for result in soup.find_all('a', class_='companies__relationships__list__item__link')]

pd.DataFrame(data).to_csv('scraped-csv/234.csv', index=False)
