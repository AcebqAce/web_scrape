from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

base_url = "https://ecapital.vc/portfolio/"
page_paths = ['liefergruen/', 'dryad/', 'numbat/', '1komma5/', 'tenzir/', 'exein/', 'jedox-2/', 'build38/', 'papershift/', 'iot-inspector/', 'kendaxa/', 'countercraft/', 'am-polymers/', 'envelio/', 'open-xchange/', 'jedox/', 'saperatec/', 'temicon/', 'theva/', 'prolupin/', 'ultrasoc/', 'troy/', 'embold/', 'vmray/', 'iplytics/', 'creapaper/', 'blueid/', 'brighter-ai/', 'videantis/', 'nyris/', 'sweepatic/', '4jet-technologies/', 'perora/', 'sonnen/', 'novaled/', 'milk-the-sun/', 'smarthouse/', 'greenergetic/', 'geo-en/', 'gollmann/', 'appcon/', 'sikom/', 'nicetec/', 'lumics/', 'freshnails/', 'pyramid-computer/', 'divolution/', 'epigab-optronic/', 'impact/', 'ferroelectric-memory/', 'heliatek/', 'rhebo/', 'rips-technologies/', 'evodos/', 'omnitron/', 'anycom/', 'ccs-cad-cam/', 'reproline-medical/', 'calory-coach/', 'pace/', 'cnm-technologies/', 'svh24-de/', 'inmatec/', 'variowell/', 'brandmaker/', 'smart-hydro-power/', 'subitec/', 'cysal/']

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
    results = soup.find_all('dl', class_='c-list c-list--def c-list--horizontal c-intro__meta')

    for result in results:
        web_element = result.find('a')
        web = web_element['href'] if web_element else ''

        locat_element = result.find_all('dd')
        locat = locat_element[1].text if len(locat_element) >= 2 else ''

        stat_element = result.find_all('dd')
        stat = stat_element[2].text if len(stat_element) >= 3 else ''

        data.append([web, locat, stat])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/ecapital.csv', index=False)

end_time = time.time()

elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
