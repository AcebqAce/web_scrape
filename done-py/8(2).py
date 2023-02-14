from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/8.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('p')
columns = ['Investor', 'Summary', 'Website']
data = []

for result in results:
    investor_elements = result.find('strong')
    if not investor_elements:
        continue
    investor = investor_elements.text if investor_elements else ''

    summary = result.text.strip().split(" | ")[-1]
    
    website_elements = result.find_all('a', href=True)
    if len(website_elements) >= 3:
        website = website_elements[2].get('href')
    else:
        website = ''

    data.append([investor, summary, website])

df = pd.DataFrame(data, columns=columns)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/8.csv', index=False)