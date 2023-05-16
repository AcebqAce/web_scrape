from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://mindmaps.dka.global/firms/"
page_paths = ['20487', '26618', '11915', '146418', '146277', '145830', '72160', '19419', '147352', '145369', '145227', '144982', '39193', '55205', '35037', '81154', '12188', '143296', '143191', '143115', '5560', '98204', '142954', '142731', '142446', '27211', '2542', '141732', '141588', '141390', '42926', '141220', '19423', '141068', '140905', '12056', '140453', '140100', '139813', '139484', '40540', '62821', '138841', '9035', '138632', '138580', '138227', '51650', '40661', '138034', '52196', '137801', '18057', '137665', '137564', '4461', '123645', '136083', '14997', '5877', '11485', '2611', '134882', '117554', '5915', '59578', '134688', '26219', '134380', '19160', '134260', '22414', '134116', '22415', '5947', '133955', '27171', '133644', '5964', '133564', '19233', '132969', '132832', '26596', '132503', '123128', '132453', '6020', '132193', '118336', '112429', '6068', '123530', '51826', '26973', '130757', '55979', '130586', '6123', '130160', '130013', '129993', '129987', '2827', '6132', '129835', '2950', '129700', '123953', '41661', '123860', '24341', '2687', '129061', '123549', '123543', '123539', '123531', '41724', '123517', '123319', '123293', '41782', '123082', '2007', '122801', '21523', '122714', '15197', '6274', '26812', '122106', '122073', '127923', '26452', '121946', '121939', '121907', '6309', '121815', '22824', '87729', '127648', '127610', '127546', '21329', '126879', '27212', '97111', '26460', '114635', '126234', '126120', '86526', '70396', '125912', '125787', '14806', '26625', '72414', '111509', '125238', '125080', '26203', '124898', '124844', '124810', '71004', '124429', '124277', '7558', '6489']

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
    results = soup.find_all('div', class_='border border-light rounded p-4 border-right-0')

    for result in results:
        row = {}
        web_element = result.find('a')
        row['web'] = web_element['href'] if web_element else ''
        
        elements = result.find_all('div')
        for i in range(10):
            try:
                row[f'{i+1}'] = elements[i].text.replace('\t', '').strip()
            except IndexError:
                row[f'{i+1}'] = ''
        
        data.append(row)
        time.sleep(random.uniform(1, 3))

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/mindmap.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time
print('\n' f'Scaping complete in {elapsed_time:.2f} seconds')
