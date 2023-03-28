from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open('downloaded-html/134.html'), 'html.parser')

data = [[result.find('h3').text if result.find('h3') else '',
         result.find('a', class_='elementor-button')['href'] if result.find('a') else '']
         for result in soup.find_all('div', class_='jet-animated-box__content')]

pd.DataFrame(data).to_csv('scraped-csv/134.csv', index=False)