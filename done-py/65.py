from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/65.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h3')
data = []

for result in results:
    name = result.text.strip().split('. ')[-1]

    summary_element = result.find_next('p')
    if summary_element:
        summary = summary_element.text
    else:
        summary = ''

    web_element = summary_element.find_next('p') if summary_element else None
    if web_element:
        web = web_element.text.split("Website:")[-1].strip()
    else:
        web = ''

    founded_element = web_element.find_next('p') if web_element else None
    if founded_element:
        founded = founded_element.text.split("Founded:")[-1].strip()
    else:
        founded = ''

    fund_element = founded_element.find_next('p') if founded_element else None
    if fund_element:
        fund = fund_element.text.split("Total fund size:")[-1].strip()
    else:
        fund = ''

    data.append([name, web, summary, founded, fund])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/65.csv', index=False)