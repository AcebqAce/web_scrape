from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://ftvcapital.com/portfolio-item/"
page_paths = ['6-degrees-health/', 'actimize/', 'agiloft/', 'apex-fund-services/', 'aspire-financial-services/', 'aveksa/', 'bluegill-technologies/', 'cardconnect/', 'cashstar/', 'castle-pines-capital/', 'catalyst-repository-systems/', 'centaur/', 'cloudfactory/', 'cloudmark/', 'company-com/', 'connexpay/', 'coremetrics/', 'covario/', 'dataart/', 'daylight-forensic/', 'derivative-path/', 'ebaotech/', 'edgewater-markets/', 'egress/', 'e-loan/', 'embroker/', 'empyrean-benefit-solutions/', 'etf-securities/', 'exlservice/', 'financial-engines/', 'finaro/', 'fleet-one/', 'gale-healthcare-solutions/', 'globant/', 'gmi/', 'health-credit-services/', 'id-me/', 'indexiq/', 'intrepid-learning-solutions/', 'investcloud/', 'kvs/', 'lean-solutions-group/', 'liberis/', 'liveintent/', 'loanpro/', 'logicsource/', 'luma-health/', 'many-pets/', 'marketsandmarkets/', 'marketshare/', 'masttro/', 'medsynergies/', 'mu-sigma/', 'neon-one/', 'opensesame/', 'openspan/', 'paddle/', 'patra/', 'peoplecert/', 'perfecto-mobile/', 'plate-iq/', 'powershares/', 'presidio-reinsurance-group/', 'rapidratings/', 'riskalyze/', 'security-compass/', 'singleops/', 'solid/', 'sourcecode/', 'spredfast/', 'strata-fund-solutions/', 'swan-global-investments/', 'symbio/', 'tango-card/', 'tidal/', 'true-potential/', 'trustwave/', 'vagaro/', 'varicent/', 'velocity-shares/', 'verus-financial-management/', 'vindicia/', 'vortx/', 'vpay/', 'welcome/', 'wepay/', 'worldfirst/', 'xign/', 'xplor/', 'zoovu/']

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
    results = soup.find_all('div', class_='aside wow fadeInUp')

    for result in results:
        web_element = result.find('a')
        if web_element:
            web = web_element['href']
            if 'ftvcapital.com' in web:
                continue
        else:
            web = ''

        locat_element = result.find_all('p')
        locat = locat_element[4].text if len(locat_element) >= 5 else ''

        data.append([web, locat])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/ftvcap.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
