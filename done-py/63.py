from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/63.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h1', class_='jo')
data = []

for result in results:
    name_element = result.find('a')
    name = name_element.text if name_element else ''

    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    summary_element = result.find_all_next('p')
    summary = summary_element[0].text if summary_element else ''

    fund_element = result.find_next('strong', text='Fund size:')
    fund = fund_element.next_sibling.strip() if fund_element else ''

    location_element = result.find_next('strong', text='Geographical focus:')
    location = location_element.next_sibling.strip() if location_element else ''

    focus_element = result.find_next('strong', text='Focus:')
    focus = focus_element.next_sibling.strip() if focus_element else ''

    stage_element = result.find_next('strong', text='Stage:')
    stage = stage_element.next_sibling.strip() if stage_element else ''

    data.append([name, web, summary, fund, location, focus, stage])

df = pd.DataFrame(data)
df.to_csv('scraped-csv/63.csv', index=False)