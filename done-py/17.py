from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/17.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='speaker')
data = []

for result in results:
    name_element = result.find('div', class_='speaker-name text-left text-lg-center')
    name = name_element.text if name_element else ''

    title_element = result.find('div', class_='d-none d-lg-block speaker-title')
    title = title_element.text if title_element else ''

    company_element = result.find('div', class_='d-none d-lg-block speaker-company')
    company = company_element.text if company_element else ''

    data.append([name, title, company])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/17.csv', index=False)