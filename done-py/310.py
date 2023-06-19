from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/310.html'), 'html.parser')

data = [[result.text.split(" |")[0],
         result.text.split("| ")[-1].replace('\n', '').replace('            ', ' ').strip(),
         result.find('a')['href'] if result.find('a') else '']
        for result in soup.find_all('p')]

pd.DataFrame(data).to_csv('scraped-csv/310.csv', index=False)
