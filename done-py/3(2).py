from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/3.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

result = soup.find('table', id='wpdtSimpleTable-72')

data = []

for row in result.find_all("tr"):
    cells = [cell.text.strip() for cell in row.find_all("td") if cell.text.strip()]
    if cells:
        data.append(cells)

df = pd.DataFrame(data, columns=['1','2','3','4'])
df.to_csv('scraped-csv/3.csv', index=False)
