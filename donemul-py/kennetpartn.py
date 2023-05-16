from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://kennet.com/portfolio/"
page_paths = ['provar/', 'scoro/', 'grip-events/', 'nudge-global/', 'loyaltylion/', 'estoremedia/', 'filecloud/', 'redicasystems/', 'onfleet/', 'codility/', 'eloomi/', 'socialsurvey/', 'spatial-networks/', 'crossborder-solutions/', 'rimilia/', 'nuxeo/', 'aba-english/', 'receipt-bank/', 'impartner/', 'realitymine/', 'thinkhr/', 'rivo-software/', 'conversica/', 'adikteev/', 'kemp-technologies/', 'sermo/', 'nextperf/', 'prolexic-technologies/', 'revolution-prep/', 'buyvip/', 'goviral/', 'spreadshirt/', 'schoolwires/', 'academixdirect/', 'recommind/', 'ntrglobal/', 'viant/', 'telemedicine-clinic-tmc/', 'sts/', 'intelepeer/', 'resilience/', 'frsglobal/', 'sequans-communications/', 'adviva/', 'daptiv/', 'chipidea/', 'kapow-technologies/', 'netpros/', 'fluency-voice-technology/', 'netpros/', 'ubizen/', 'exonys/', 'clearswift/', 'aarohi/', 'volantis-systems/', 'aspective/', 'no-wires-needed/', 'altitun/', 'cramer-systems/', 'orchestream/', 'paragon-software/', 'monis/', 'consul-risk-management/', 'oxygen-solutions/']

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
    results = soup.find_all('div', class_='ct-div-block info-portfolio')

    for result in results:
        name_element = result.find('span', id='span-12-180')
        name = name_element.text if name_element else ''
        
        locat_element = result.find('span', id='span-29-180')
        locat = locat_element.text if locat_element else ''

        stat_element = result.find('span', id='span-34-180')
        stat = stat_element.text if stat_element else ''

        data.append([name, locat, stat])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {name}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/kennetpartn.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time

