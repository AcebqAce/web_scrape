from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/70.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='speaker-text')
data = []

for result in results:
    name_element = result.find('div', class_='atom-fullname')
    name = name_element.text if name_element else ''
    name = name.replace("  ", " ")

    title_element = result.find('div', class_='atom-text1')
    title = title_element.text if title_element else ''

    company_element = result.find('div', class_='atom-text2')
    company = company_element.text if company_element else ''

    data.append([name, title, company])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/70.csv', index=False)