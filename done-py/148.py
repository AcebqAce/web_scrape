from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/148.html'), 'html.parser')

data = [[result.find('b', class_='font-title').text if result.find('b', class_='font-title') else '',
         result.find('span', title='Location').text.replace('\n','').split(", ")[-1].strip() if result.find('span', title='Location') else '',
         result.find('a')['href'] if result.find('a') else '']
    for result in soup.find_all('li')
]

pd.DataFrame(data).to_csv('scraped-csv/148.csv', index=False)