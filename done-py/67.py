from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/67-3.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h3')
data = []
for result in results:
    name_element = result.find('a')
    name = name_element.text if name_element else ''

    website_element = result.find_next('a')
    website = website_element['href'] if website_element else ''

    data.append([name, website])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/67(3).csv', index=False)