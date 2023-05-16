from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://www.helvetica-capital.ch/en/investment/"
page_paths = ['polygena/', 'schulthess-maschinen/', 'skycell/', 'fotokite/', 'wingtra/', 'num-industry-alliance/', 'nexxiot/', 'specpage/', 'nezasa/', 'copytrend/', 'neo-medical/', 'ava/', 'nuessli/', 'ilag/', 'scantrust/', 'sphinx-tools/', 'asic-robotics/', 'mesa-imaging/', 'creative-electronic-systems/']

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
    results = soup.find_all('ul', class_='ProductFacts')

    for  result in results:
        name_element = result.find_all('span', class_='ProductFacts__fact')
        name = name_element[0].text if len(name_element) >= 1 else ''

        locat_element = result.find_all('span', class_='ProductFacts__fact')
        locat = locat_element[3].text.split(' | ')[0].strip() if len(locat_element) >= 4 else ''

        web_element = result.find('a', class_='ProductFacts__fact')
        web = web_element['href'] if web_element else ''

        data.append([name, locat, web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {name}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/helvetica.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
