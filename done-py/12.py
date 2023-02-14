from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/12.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='col-12 col-md-12')
columns = ['Company', 'Website']
data = []

for result in results:
    company_element = result.find('h5')
    company = company_element.text if company_element else ''
    company = company.replace("\n", '')
    company = company.replace(" ", '')

    website_element = result.find('a', href=True)
    website = website_element['href'] if website_element else ''

    data.append([company, website])

df  = pd.DataFrame(data, columns=columns)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/12.csv', index=False)