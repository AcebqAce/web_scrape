from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://frogcapital.com/company/"
page_paths = ['housfy/', 'genasys/', 'clue-software/', 'caspar/', 'winningtemp/', 'evotix/', 'sofatutor/', 'mcmakler/', 'modulr/', 'vulog/', 'azimo/', 'sellics/', 'opensignal/', 'skimlinks/', 'rated-people/', 'mediatonic/', 'edited/', 'gb-group/', 'dealflo/']

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
    results = soup.find_all('div', class_='post--intro__content')

    for result in results:
        web_element = result.find('a')
        web = web_element['href'] if web_element else ''

        data.append([web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/frogcap.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
