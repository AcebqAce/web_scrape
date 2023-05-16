from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

base_url = "https://emerald.vc/portfolio/"
page_paths = ['actnano/', 'aganova/', 'agraquest/', 'alphaics/', 'future-meat-technologies/', 'cellex-power/', 'energya-wind-technologies/', 'enocean/', 'enspired/', 'eologix/', 'evergreen-solar/', 'fido/', 'geodigital/', 'hydropoint/', 'hyradix/', 'imagindairy/', 'inge/', 'librestream/', 'lucintech/', 'meeat-foodtech-oy/', 'metgen/', 'nanograf/', 'open-mineral/', 'optimatics/', 'ormecon/', 'p97-networks/', 'pemeas/', 'phase-change-solutions/', 'powerhouse-dynamics/', 'pure-technologies/', 'rhombus-energy-solutions/', 'ruggedcom/', 'schmack-biogas/', 'securitymatters/', 'senscient/', 'sewerai/', 'sofi-filtration/', 'spear-power-systems/', 'takadu/', 'tropic-biosciences/', 'urgently/', 'ushr/', 'visedo/', 'xfarm/']

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
    results = soup.find_all('div', class_='portfolio-about-wrap')

    for result in results:
        name_element = result.find('h1')
        name = name_element.text if name_element else ''

        web_element = result.find('a', class_='website')
        web = web_element['href'] if web_element else ''

        data.append([name, web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {name}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('/home/ace/web_scrape/web_scrape/scraped-csv/emerald.csv', index=False)

end_time = time.time()

elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
