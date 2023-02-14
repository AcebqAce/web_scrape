from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/8.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('tr')
columns = ['Company', 'Website','Country', 'Other marketplace investments', 'Preferred Round']
data = []

for result in results:
    name_elements = result.find_all('td')
    name = name_elements[0].text if name_elements else ''

    website_elements = result.find_all('a', href=True)
    website = website_elements[0].get('href') if website_elements else ''

    country_elements = result.find_all('td')
    country = country_elements[1].text if country_elements else ''

    invest_elements = result.find_all('td')
    invest = invest_elements[2].text if invest_elements else ''

    preround_elements = result.find_all('td')
    preround = preround_elements[3].text if preround_elements else ''

    data.append([name, website, country, invest, preround])

df = pd.DataFrame(data, columns=columns)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/8.csv', index=False)