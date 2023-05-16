from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://lowercarboncapital.com/company/"
page_paths = ['lilac/', 'solugen/', 'antora/', 'heartaerospace/', 'commonwealthfusion/', 'runningtide/', 'sublime-systems/', 'mosameat/', 'charm/', 'remora/', 'mill/', 'kulabio/', 'zeroacre/', 'floodbase/', 'zapenergy/', 'crusoe/', 'avalanche/', 'electra/', 'epoch/', 'pachama/', 'formo/', 'highersteaks/', 'crux/', 'livingcarbon/', 'genomines/', 'nitricity/', 'verdox/', 'heirloom/', 'soilcarbonco/', 'minus/', 'airloom/', 'supercritical-solutions/', 'entocycle/', 'coda/', 'zanskar/', 'solarsquare/', 'musa/', 'lemon/', 'linearlabs/', 'kettle/', 'macro-oceans/', 'river/', 'arc-boats/', 'carbonengineering/', 'dendra/', 'carbonchain/', 'tomorrowfarms/', 'holy-grail/', 'truecircle/', 'enode/', 'noya/', 'tender/', 'pledge/', 'frostmethane/', 'twelve/', 'flair-systems/', 'boundarylayer/', 'mootral/', 'microbyre/', 'yard-stick/', 'cervest/', 'stealth/', 'carbon180/', 'silverlining/', 'carbonplan/', 'harvardsgrp/', 'mcbp/']

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

robots_txt = requests.get(base_url + '/robots.txt', headers=HEADERS)
if robots_txt.status_code == 200 and 'Disallow' in robots_txt.text:
    print('Website is not scrapable')
    exit()

data = []
start_time = time.time()

for page_path in page_paths:
    url = base_url + page_path
    page = requests.get(url, headers=HEADERS)
    if not page.ok:
        print(f'Error: {page.status_code} - {page.reason}')
        continue
    
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='wp-block-columns is-style-centered is-layout-flex wp-container-5 wp-block-columns-is-layout-flex')

    for result in results:
        locat_element = result.find_all('p')
        locat = locat_element[2].text.split('HQ: ')[-1].strip() if len(locat_element) >= 3 else ''

        web_element = result.find('a')
        web = web_element['href'] if web_element else ''

        data.append([locat, web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/lowercarboncap.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time

