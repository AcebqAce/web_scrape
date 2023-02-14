from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/37.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a')
data = []

for result in results:
    name = result.text
    web = result.get('href')
    
    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/37.csv', index=False)