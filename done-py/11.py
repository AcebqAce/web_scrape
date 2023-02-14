from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/11.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

h3_elements = soup.find_all('h3')
columns = ['Company', 'Website','Country', 'Fund size', 'Investment stage', 'Summary']
data = []

for h3_element in h3_elements:
    name = h3_element.text

    website_element = h3_element.find('a', href=True)
    website = website_element['href'] if website_element else ''

    headquarter_element = h3_element.find_next('p')
    if headquarter_element:
        headquarter = headquarter_element.text.split("Headquarter:")[-1].strip()
    else:
        headquarter = ''

    fund_element = headquarter_element.find_next('p') if headquarter_element else None
    if fund_element:
        fund = fund_element.text.split("Fund size:")[-1].strip()
    else:
        fund = ''

    investment_element = fund_element.find_next('p') if fund_element else None
    if investment_element:
        investment = investment_element.text.split("Investment stages:")[-1].strip()
    else:
        investment = ''

    describe_element = investment_element.find_next('p') if investment_element else None
    if describe_element:
        describe = describe_element.text.strip()
    else:
        describe = ''

    data.append([name, website, headquarter, fund, investment, describe])

df  = pd.DataFrame(data, columns=columns)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/11.csv', index=False)