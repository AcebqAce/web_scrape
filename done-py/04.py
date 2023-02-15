from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/4.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('p')
columns = ['Name', 'Company']
data = []

for result in results:
    name_elements = result.find_all('a')
    if not name_elements:
        continue
    name = name_elements[0].text if name_elements[0].text else name_elements[1].text

    company_elements = result.find_all('b')
    if not company_elements:
        continue
    company = company_elements[0].text if company_elements[0].text else company_elements[1].text

    data.append([name, company])

df  = pd.DataFrame(data, columns=columns)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/4.csv', index=False)
