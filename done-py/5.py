from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/5.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('p')
columns = ['Company', 'Summary']
data = []

for result in results:
    company_elements = result.find_all('a')
    if not company_elements:
        continue
    company = company_elements[0].text if company_elements[0].text else company_elements[1].text

    summary = result.text.strip().split(" | ")[-1]

    data.append([company, summary])

df = pd.DataFrame(data, columns=columns)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/5.csv', index=False)