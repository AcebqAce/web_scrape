from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://newfundcap.com/company/"
page_paths = ['aircall', 'fairmarkit', 'umiami', 'eqinov', 'inarix', 'shareid', 'purenat', 'pono', 'locuta', 'livejourney', 'hireguide-0', 'rwazi', 'rendition', 'ramify', 'keenat', 'reecall-0', 'dolly', 'hoopcare-0', 'vendict-0', 'upkid-0', 'savvy', 'homeroom-0', 'olino-ex-riskee', 'in2bones', 'medtech', 'tageos', 'oplit', 'nfinite', 'kumo', 'adaxis', 'rabot', 'keypup', 'mustard', 'bolero', 'astran', 'zing', 'sonetio', 'fleeti', 'volara', 'limonetik', 'wfhomie', 'omnidoc', 'v-motech', 'oko', 'beyond-ratings', 'storey', 'umiami', 'arkhn', 'lead', 'relevize', 'qra-corp', 'brightflow-ai', 'touch-sensity', 'urbanease', 'civ-robotics', 'hd-rain', 'optimcare', 'aware-healthcare', 'dexter', 'cents', 'bornio', 'cuure', 'comeen', 'brazeco', 'eano', 'coverd', 'volum', 'atelier-braam', 'datagalaxy', 'les-nouveaux-affineurs', 'ogust', 'moodwork', 'gpio', 'cofi', 'impala', 'jobypepper', 'presence-ai', 'cocoon-space', 'avanseo', 'liveminutes', 'curv-health', 'shapemeasure', 'camping-and-co', 'pliant', 'xotelia', 'aveine', 'homeland', 'pom-monitoring', 'jinka', 'tagbio', 'young-alfred', 'agathos', 'shelterluv', 'arenametrix', 'wizville', '909c', 'optionizr', 'fairmoney', 'fairmarkit', 'advitam', 'mobpartner', 'jobijoba', 'visiblee', 'monbento', 'billtrim', 'infirmierscom', 'dipli', 'relimetrics', 'luckey-homes', 'customermatrix', 'teachfx', 'cettefamille', 'dejamobile', 'apptopia', 'otto', 'zinier', 'visage', 'yummypets', 'shotgun', 'learnissimo', 'climb', 'kiute', 'blue-industryscience', 'ibillionaire', 'ocr', 'jooxter', 'braineet', 'siga', 'le-grand-dressing', 'meta-api', 'alchemy', 'watchdog-system', 'akoustic-arts', 'pharmasimple', 'avanoo', 'apitic', 'riva', 'paymium', 'roomkey', 'hull', 'joovence', 'aircall', 'kara', 'loginchinese', 'greenkub', 'camping-car-park', 'couriier', 'frequentiel', 'tradeit', 'quasar', 'redluxury', 'elues-locales', 'finaho', 'tiwal', 'edicia', 'stormize', 'happy-meal', 'suntrade-travel', 'simcom-europe', 'invoxia', 'joxko', 'bretzel-love', 'yoopala', 'groupe-pratique']

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
    results = soup.find_all('div', class_='field field--name-field-link field--type-link field--label-hidden field__item')

    for result in results:
        web_element = result.find('a')
        web = web_element['href'] if web_element else ''

        data.append([web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/newfundcap.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time
