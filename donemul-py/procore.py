from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

base_url = "https://marketplace.procore.com/apps/"
page_paths = ['36zero', 'aciex', 'acuite']

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

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
    results = soup.find_all('div', class_='sc-bjUoiL NQZgi')

    for result in results:
        name_element = result.find_all('a', class_='sc-bZkfAO cJJSDQ sc-fWIMVQ pWOOa')
        name = name_element[1].text if name_element else ''

        web_element = result.find('a', class_='sc-bZkfAO cJJSDQ sc-fWIMVQ pWOOa')
        web = web_element[1]('href') if web_element else ''

        data.append([name, web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {name}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/procore.csv', index=False)

end_time = time.time()

elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')