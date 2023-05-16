from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://costanoa.vc/company/"
page_paths = ['3scale/', '6sense/', 'acme/', 'alpha-health/', 'alation/', 'amplify-ai/', 'aperture/', 'appomni/', 'apptimize/', 'aquabyte/', 'aserto/', 'auterion/', 'bigeye/', 'billgo/', 'bolster/', 'bugcrowd/', 'comun/', 'flexio/', 'coiled/', 'cyberhaven/', 'cyral/', 'datalogix/', 'demandbase/', 'earthmover/', 'elevate-security/', 'faunadb/', 'focal-systems/', 'fossa/', 'gamechanger/', 'grovo/', 'guardian-analytics/', 'highline/', 'highnote/', 'inflection/', 'intacct/', 'isocket/', 'jitsu/', 'kenna-security/', 'kepler/', 'kevala/', 'krypton/', 'landit/', 'leap/', 'lex-machina/', 'liferaft/', 'lively/', 'luabase/', 'malga/', 'muon-space/', 'novoed/', 'noteable/', 'novel/', 'noyo/', 'numberai/', 'outerbounds/', 'parallel-domain/', 'passbase/', 'paynearme/', 'pepperdata/', 'propeller/', 'quizlet/', 'rafay-systems/', 'regrow/', 'rerun/', 'replicant/', 'return-path/', 'roadster/', 'sgnl/', 'skedulo/', 'smile-identity/', 'springboard/', 'stackhawk/', 'stitch-labs/', 'textualize/', 'umba/', 'sync-computing/', 'vannevar-labs/', 'victorops/', 'vic-ai/', 'vividly/', 'zentist/', 'zerowall/']

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
    results = soup.find_all('li', class_='')

    for result in results:
        web_element = result.find('a')
        if web_element:
            web = web_element['href'] 
            if 'linkedin.com' in web or 'twitter.com' in web or 'costanoa.vc' in web:
                continue
        else:
            web = ''

        data.append([web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/costanoa.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time

