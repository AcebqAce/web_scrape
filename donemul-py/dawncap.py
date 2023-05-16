from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import stem.process
from stem.util import term

base_url = "https://dawncapital.com/our-companies/"
page_paths = ['ably/', 'accessfintech/', 'billie/']

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def scrape_website(url, headers, proxies):
    page = requests.get(url, headers=headers, proxies=proxies)
    if not page.ok:
        print(f'Error: {page.status_code} - {page.reason}')
        return None

    try:
        encoding = page.encoding if 'charset' in page.headers.get('Content-Type', '') else 'utf-8'
        soup = BeautifulSoup(page.content.decode(encoding, 'ignore'), 'html.parser')
    except Exception as e:
        print(f'Error decoding page content: {e}')
        return None

    results = soup.find_all('div', class_='col-12 social_box text-center')

    web_links = []
    for result in results:
        web_element = result.find('a')
        web_link = web_element['href'] if web_element else ''
        web_links.append(web_link)

    print(f'Scraped {len(web_links)} web links from {url}')
    time.sleep(random.uniform(1, 3))

    return web_links

def rotate_ip():
    print(term.format('Starting Tor...\n', term.Attr.BOLD))
    tor_process = stem.process.launch_tor_with_config(
        tor_cmd='tor',
        config={
            'SocksPort': '9052',
            'ControlPort': '9053',
            'ExitNodes': '{us}',
        },
        init_msg_handler=print,
    )
    return tor_process

data = []
tor_process = rotate_ip()
headers = {'User-Agent': get_random_user_agent()}
proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
for page_path in page_paths:
    url = base_url + page_path
    web_links = scrape_website(url, headers, proxies)
    if web_links:
        data.extend(web_links)
    else:
        print(f'Error: Unable to scrape {url}')
    time.sleep(5)

tor_process.kill()
if data:
    df = pd.DataFrame(data, columns=['Web Link'])
    df.to_csv('scraped-csv/dawncap.csv', index=False)
    print(f'Successfully scraped the website and saved data to scraped-csv/dawncap.csv file.')
