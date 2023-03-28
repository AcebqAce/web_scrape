from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/138.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

data = [[result.text.split(") ")[-1].strip(),
         result.find_next('p').text if result.find_next('p') else '',
         result.find_next('a')['href'] if result.find_next('a') else '',
         next((li.text.split('Started in: ')[-1].strip() for li in result.find_all_next('li') if 'Started in: ' in li.text), ''),
         next((li.text.split('Founders: ')[-1].strip() for li in result.find_all_next('li') if 'Founders: ' in li.text), ''),
         next((li.text.split('Industries: ')[-1].strip() for li in result.find_all_next('li') if 'Industires: ' in li.text), ''),
         next((li.text.split('Funds raised: ')[-1].strip() for li in result.find_all_next('li') if 'Funds raised: ' in li.text), ''),
         next((li.text.split('3 remarkable investments: ')[-1].strip() for li in result.find_all_next('li') if '3 remarkable investments: ' in li.text), '')]
         for result in soup.find_all('h3')]

pd.DataFrame(data).to_csv('scraped-csv/138.csv', index=False)
