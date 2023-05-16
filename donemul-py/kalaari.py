from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://www.kalaari.com/portfolio/"
page_paths = ['aastey/', 'affordplan/', 'agnext/', 'agrim/', 'atirath/', 'baaz-bikes/', 'bluestone/', 'bombay-play/', 'cashkaro/', 'chara/', 'clean-electric/', 'climes/', 'connectedh/', 'convin/', 'creative-galileo/', 'creditvidya/', 'curefit/', 'deconstruct/', 'deftouch/', 'digantara/', 'dream11/', 'dubverse/', 'edgenetworks/', 'elasticrun/', 'elevar-sports/', 'eloelo/', 'guardian/', 'healthplix/', 'hiver/', 'industry-buying/', 'instamojo/', 'jumbotail/', 'kindlife/', 'koo/', 'magzter/', 'mall91/', 'mozark/', 'muzigal/', 'myglamm/', 'nanoheal/', 'outscal/', 'peer-robotics/', 'phable/', 'portl/', 'power2sme/', 'samosa-party/', 'shopalyst/', 'signzy/', 'simplicontract/', 'skit-ai/', 'stanplus/', 'studio-sirah/', 'swift/', 'threedots/', 'toffee-insurance/', 'tring/', 'vakilsearch/', 'vyome/', 'werize/', 'winzo/', 'yourstory/', 'zluri/', 'zocket/']

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
    results = soup.find_all('a', class_='vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-square vc_btn3-style-outline-custom vc_btn3-icon-right')

    for result in results:
        web = result['href']

        data.append([web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('/home/ace/web_scrape/web_scrape/scraped-csv/kalaari.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time

