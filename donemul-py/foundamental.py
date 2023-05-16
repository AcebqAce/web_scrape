from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://foundamental.com/portfolio/"
page_paths = ['infra-market/', 'tul/', 'loconav/', 'wizfreight/', '011h/', 'powerus/', 'speckle/', 'mighty-buildings/', 'welcome-homes/', 'safeai/', 'ofload/', 'juno/', 'forge/', 'vahak/', '1build/', 'stealth-company-4/', 'lun/', 'adaptive/', 'cutr/', 'snaptrude/', 'ivyhomes/', 'terraform/', 'cottage/', 'graneet/', 'metalbook/', 'rayon/', 'onsite/', 'tazapay/', 'werk/', 'homebase/', 'gocement/', 'zaraye/', 'alice-technologies/', 'earlytrade/', 'novade/', 'baupal/', 'carbonbuilt/', 'bricknbolt/', 'infraprime-logistics/', 'yojak/', 'prolance/', 'ackcio/', 'permitflow/', 'stealth-26/', 'reframe-systems/', 'stealth-42/', 'jumba/', 'mattoboard/', 'latii/', 'dekoruma/', 'kagenova/', 'indus-ai/', 'q-bot/', 'reinvent/', 'trelar/', 'holobuilder/']

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/5378.36'}

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
    results = soup.find_all('li')

    for result in results:
        web_element = result.find('a')
        if web_element:
            web = web_element['href']
            if 'linkedin.com' in web or 'twitter.com' in web or 'facebook.com' in web or 'foundamental.com' in web:
                continue
        else:
            web = ''

        data.append([web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/foundamental.csv', index=False)
    
end_time = time.time()

elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')
