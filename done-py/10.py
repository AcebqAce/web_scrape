from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/10.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('p')
columns = ['Company', 'Summary']
data = []

for result in results:
    company_elements = result.find('strong')
    company = company_elements.text if company_elements else ''

    summary = result.text.strip().replace(company, "").strip()
    summary = summary.replace("\n", "")
    summary = summary[:-1]

    data.append([company, summary])

df = pd.DataFrame(data, columns=columns)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/10.csv', index=False)