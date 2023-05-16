from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd

base_url = "https://www.ciscoinvestments.com/portfolio/"
page_paths = ['21', '3ts-capital-partners', '4paradigm', '6wind', 'aavishkaar', 'acqueon', 'acrew', 'actility', 'actioniq', 'adbrain', 'aimotive', 'alchemist-accelerator', 'algebra-ventures', 'almaz-capital', 'altiostar-networks', 'ambiq-micro', 'andapt', 'appomni', 'apptio', 'aquantia', 'aravo', 'archetype-ventures-fund', 'ascendify', 'aspect-ventures', 'atlantis', 'avi-networks', 'ayla-networks', 'behaviosec', 'belly', 'bit-stew', 'blackbird-ventures', 'blind', 'bni-video', 'bolt-io', 'bull-city-venture-partners', 'capnamic-ventures', 'celeno', 'chiratae-ventures', 'cinarra', 'cliqr', 'cloudcherry', 'cloudfx', 'cloudvelox', 'cnex-labs', 'cogniac', 'cohda-wireless', 'cohesity', 'control4', 'corellium', 'covacsis', 'crcm-ventures', 'cross-mediaworks', 'ctera', 'datarobot', 'datos-io', 'desktone', 'digitalsmiths', 'dremio', 'duo', 'dynamic-signal', 'edge-delta', 'elastica', 'elastifile', 'elevate', 'embrane', 'enverv', 'esentire', 'esilicon', 'evolution-equity', 'evrythng', 'exabeam', 'exent', 'expel', 'flashpoint', 'futureplay', 'gainsight', 'georgian-partners', 'glasswing', 'global-talent-track', 'gobi-partners', 'gong', 'grid-net', 'guardicore', 'habana-labs', 'hashicorp', 'helpshift', 'hunters', 'hycu', 'hytrust', 'icontrol-networks', 'idinvest-partners', 'illusive', 'ineda-systems', 'innovid', 'inspur-cisco-networking-technology', 'intersec', 'invitalia-ventures', 'involvio', 'ip-access', 'island', 'isovalent', 'jupiterone', 'kaszek-ventures', 'kespry', 'kii', 'komodor', 'kumu-networks', 'kustomer', 'kyligence', 'l-attitude', 'lightbits', 'lightwire', 'liveaction', 'luma-health', 'luxtera', 'mapr', 'mashery', 'mavenir', 'mcrock-capital-fund-i-and-ii', 'memverge', 'mio', 'mist-systems', 'monashees', 'moogsoft', 'moxtra', 'mozaiq-operations', 'n3n', 'nantero', 'near-pte-ltd', 'netronome', 'nexpa', 'nobl9', 'notion-capital', 'ns1', 'oak9', 'omers-ventures-fund-ii', 'one-mobikwik-systems-private-limited', 'opendns', 'openwave-mobility', 'ozon', 'packetvideo', 'panaseer', 'parallels', 'paris-saclay-fund', 'parsable', 'partech', 'paxata', 'phunware', 'piston-cloud-computing', 'pixvana', 'platfora', 'plexo-capital', 'portworx', 'prospera', 'pubnub', 'puppet', 'quantcast', 'qwilt', 'qyuki', 'rangeforce', 'real-image', 'redpoint-eventures', 'relayr', 'rivermeadow', 'rookout', 'rstor', 'safeguard-cyber', 'sealights', 'secure-code-warrior', 'securiti', 'securview', 'seeq', 'sensity-systems', 'servion', 'sibeam', 'silicon-badia', 'sky-tech-holdings-ltd', 'skyport-systems', 'smart-foa', 'springpath', 'startupbootcamp', 'stellaris-venture-partners', 'stratoscale', 'styra', 'tagnos', 'team8-ventures', 'teradici', 'terracis-tech', 'theatro', 'theta-lake', 'threatquotient', 'tidelift', 'tilera', 'triggermesh', 'turbonomic', 'u-life-solutions', 'uniphore', 'upskill', 'urbanise', 'valtix', 'vce', 'velocloud', 'veniam', 'verodin', 'videonetics', 'voicea', 'voiceitt', 'voodle', 'wabbi', 'walden-catalyst', 'walden-international', 'walden-riverwood-ventures-ii-wrv', 'whatfix', 'wilocity', 'work-bench', 'worldsensing', 'wso2', 'zensys', 'zillionsource']

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

robots_txt = requests.get(base_url + '/robots.txt', headers=HEADERS)
if robots_txt.status_code == 200 and 'Disallow'in robots_txt.text:
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
    results = soup.find_all('li',class_='ml-8')

    for result in results:
        web_element = result.find('a', class_='hover:text-primary-400')
        if web_element:
            web = web_element['href']
            # check if website is LinkedIn, Twitter, Facebook, or YouTube and skip it
            if 'linkedin.com' in web or 'twitter.com' in web or 'facebook.com' in web or 'youtube.com' in web or '/portfolio/' in web:
                continue
        else:
            web = ''

        data.append([web])
        time.sleep(random.uniform(1,3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('/home/ace/web_scrape/web_scrape/scraped-csv/ciscoinvest.csv', index=False)

end_time = time.time()

elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
