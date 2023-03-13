from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/77.html') as file:
    soup = BeautifulSoup(file, 'html.parser')
    
results = soup.find_all('div', class_='logotip-item')
data = []

for result in results:
    name_element = result.find('div', class_='logotip-title')
    name = name_element.text if name_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    # stat_element = result.find('div', class_='w-dyn-item')
    # stat = stat_element.text.strip() if stat_element else ''
    
    # if 'EXITS' in stat:
    #     print('EXITS')
    # elif stat:
    #     pass
    # else:
    #     pass

    # print(name, web, 'EXITS')

    data.append([name, web])
df = pd.DataFrame(data)
df.to_csv('scraped-csv/77.csv', index=False)