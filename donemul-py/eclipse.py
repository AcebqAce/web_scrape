from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

base_url = "https://eclipse.vc/company/"
page_paths = ['6-river-systems/', 'arc/', 'augury/', 'axlehire/', 'bright-machines/', 'brightinsight/', 'canoa/', 'cellares/', 'cerebras-systems/', 'cheetah/', 'chord/', 'circular-co/', 'clearmetal/', 'clearpath-robotics/', 'tortuga-logic/', 'datapelago/', 'metrolink/', 'decentriq/', 'dutch-pets/', 'enovix/', 'flex-logix-technologies/', 'intrepid-homes/', 'forsight-robotics/', 'foxglove/', 'fulfil/', 'gravity/', 'hosta-labs/', 'insidepacket/', 'instrumental/', 'invicta-medical/', 'june-life/', 'kindred/', 'kinema-systems/', 'lucira-health/', 'nucleus/', 'owlet-baby-care/', 'oxide-2/', 'quantum-source-labs/', 'reliable-robotics/', '851-2/', 'rune-labs/', 'safely-you/', 'skyryse/', 'swift-navigation/', 'syng-2/', 'tenstorrent/', 'third-wave-automation/', '455-2/', 'vehicle-software/', 'voxel/', 'vulcanforms/', 'watchmaker/', 'wayve/']

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
    results = soup.find_all('div', class_='Columns_Columns__YArLe Columns_columns-2__GZbde')

    for result in results:
        name_element = result.find('h2', class_='wp-block-post-title')
        name = name_element.text if name_element else ''

        web_element = result.find('a')
        web = web_element['href'] if web_element else ''

        data.append([name, web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {name}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('/home/ace/web_scrape/web_scrape/scraped-csv/eclipse.csv', index=False)

end_time = time.time()

elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
