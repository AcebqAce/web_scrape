from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/61-2.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='m-speakers-list__items__item__header')
data = []

for result in results:
    name_element = result.find('a')
    name = name_element.text if name_element else ''

    title_element = result.find('span', class_='m-speakers-list__items__item__header__meta__position')
    title = title_element.text if title_element else ''
    title = title.replace(', ', '')

    company_element = result.find('span', class_='m-speakers-list__items__item__header__meta__company')
    company = company_element.text if company_element else ''

    data.append([name, title, company])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/61(2).csv', index=False)