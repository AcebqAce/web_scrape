from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://main.nl/companies/"
page_paths = ['19415-2/', 'genodata/', 'syska/', 'timegrip/', 'certwell/', 'wefact/', 'van-den-berg/', 'pdv-financial-software-gmbh/', 'vendre/', 'selfpoint/', '2bra-system/', 'timeplan/', 'casix/', 'uhb-consulting-ag/', 'medisoft/', 'tasper/', 'fleetgo/', 'wanko/', 'avancit/', 'timeff/', 'plato/', 'iqs/', 'avinty/', 'janusid/', 'lost-lemon/', 'apployed/', 'eazyproject/', 'synetics/', 'bizzdesign/', 'akyla/', 'skarp/', 'funatic/', 'smartaim/', 'bcs/', 'pro4all/', '2ndc/', 'videovisit/', 'concludis/', 'aruba-informatik-gmbh/', 'litreca-ag/', 'texdata-software-gmbh/', 'nissen-velten-software-gmbh/', 'enventa-group/', 'cryptshare/', 'audimex/', 'blika/', 'sowiso/', 'swedish-care/', 'readid/', 'qlogic/', 'biomedion/', 'form-solutions-gmbh/', 'oribi-id-solutions/', 'qics/', 'people-test-systems/', '8308-2/', 'sovren/', 'timekeeper/', 'spendency/', 'daisy-2/', 'zig-websoftware/', 'eelloo/', 'emagixx/', 'zaurus/', 'way2connect/', 'kindplanner/', 'infent/', 'cpm4care/', 'tog-nederland/', 'bjorn-lunden/', 'cdds/', 'secmaker/', 'clinicbuddy/', 'sivis/', 'expansion/', 'berkeley-bridge/', 'scienta/', 'paragin/', 'innospot/', 'viima/', 'safeharbour/', 'sep-isms/', 'foconis/', 'pronexus/', 'data-plan/', 'boomerweb/', 'relyon/', '4865-2/', '4value/', 'netivity/', 'hlp/', 'perbility/', 'pointsharp/', 'business-forensics/', 'textkernel/', 'mach-ag/', 'multisignaal/', 'tt-compett/', 'geodan/', 'eezeebee/', 'joliv/', 'frontin/', 'zaaksysteem-nl/', 'css-breda/', 'workflowwise/', 'avedos/', 'howaboutyou/', 'alfa/', '3795-2/', 'exxellence-groep/', 'the-competence-group/', 'king-software/', 'hfmtalentindex/', '3267-2/', 'optimizers/', 'gbtec-software-consulting-ag/', 'assessio/', 'onventis-gmbh/', 'reports/', 'hype-innovation/', 'ctrl/', '1292-2/', 'cleversoft/', 'meddex/', 'geodan-van-den-berg/', 'cormel-it/', 'plandatis/', 'enovation/', 'sdb-ayton/', 'lias-software/', 'allgeier-medical-it/', 'jobrouter/', 'brein/', 'goconnectit/', 'avenida/', 'engram/', 'verklizan/', 'inergy/', 'muis-software/', 'dutch-cloud/', 'buzzcapture/', 'artegic/', 'credit-tools/', 'obi4wan/', 'axxerion/', 'denit/', 'psms/', 'cebes/', 'crotec/', 'bm-informatik/', 'green-valley/', 'ymor/', 'daarwin/', 'roxit/', 'onguard/', 'the-patient-safety-company/', 'rvc-medical-it/', 'chainpoint/', 'regas/', 'connexys/', 'cwize/', 'sofon/', '287-2/', 'secondfloor/', 'visionwaves/', 'iaso/', 'zetacom/', 'sharewire/', 'actuera/', 'tedopres-international/']

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
    results = soup.find_all('div', class_='header-content')

    for result in results:
        name_element = result.find('h1')
        name = name_element.text if name_element else ''

        data.append([name])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {name}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/maincapital_name.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time

