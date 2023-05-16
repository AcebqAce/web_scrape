from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

base_url = "https://elevationcapital.com/portfolio/"
page_paths = ['able-jobs', 'acko', 'airblack', 'anar', 'anthem', 'appsforbharat', 'autoninja', 'aye-finance', 'bliss-club', 'bookmyshow', 'brite', 'css-corp', 'capital-float', 'care-24', 'cashflo', 'chaayos', 'citymall', 'cleartax', 'country-delight', 'crowdanalytix', 'detect-technologies', 'dezerv', 'drivetrain', 'everstage', 'factors-ai', 'fampay', 'fareye', 'fashinza', 'firstcry', 'flobiz', 'frnd', 'frontrow', 'goodera', 'haber-water', 'headfone', 'high-street-essentials', 'hyype', 'indiamart', 'industrybuying', 'ixigo', 'jodo', 'journeyfront', 'justdial', 'lifecare', 'loop-health', 'makemytrip', 'medtrail', 'meesho', 'Mintifi', 'mosaic-wellness', 'murf-ai', 'nse', 'nanonets', 'nobroker', 'paytm', 'paytm-mall', 'pillow', 'ping', 'playsimple', 'plena-data', 'plobal-apps', 'polygon', 'polymerize', 'proptiger', 'qikwell', 'rigi', 'rivigo', 'sugar-cosmetics', 'sarvagram', 'senco-gold', 'sensehawk', 'sharechat', 'SolarSquare', 'spinny', 'Sprinto', 'strata', 'superops-ai', 'swiggy', 'souledstore', 'toppr', 'tracxn', 'treebo', 'turnip', 'unacademy', 'uni', 'urban-company', 'urban-ladder', 'vegrow', 'wmall', 'xpressbess', 'yellow-class', 'yoga-bar', 'yourdost', 'zeni', 'ziploan', 'zomentum']

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
    results = soup.find_all('section')

    for result in results:
        name_element = result.find('h1')
        name = name_element.text if name_element else ''

        web_element = result.find('a', class_='c0225')
        web = web_element['href'] if web_element else ''

        data.append([name, web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {name}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('/home/ace/web_scrape/web_scrape/scraped-csv/elevation.csv', index=False)

end_time = time.time()

elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
