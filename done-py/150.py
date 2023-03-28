from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/150.html'), 'html.parser')

data = [[result.find('b').text if result.find('b') else '',
         result.find_all('td')[-1].text.split(", ")[-1].strip() if result.find_all('td') else'',
         result.find('a')['href'] if result.find('a') else '']
    for result in soup.find_all('tr')
]

pd.DataFrame(data).to_csv('scraped-csv/150.csv', index=False)