from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/39.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('li', class_='ListItem')
data = []

for result in results:
    name_element = result.find('h4')
    name = name_element.text if name_element else ''

    web_element = result.find('a', href=True)
    web = web_element['href'] if web_element else ''
    
    data.append([name, web])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/39.csv', index=False)