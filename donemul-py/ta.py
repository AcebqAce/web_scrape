from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://www.ta.com/portfolio/investments/"
page_paths = ['10bis/', '2nd-story-software-inc/', '511-inc/', 'abovenet-inc/', 'the-access-group/', 'accion-labs/', 'accruent-llc/', 'adcubum/', 'advantice-health/', 'advantive/', 'advisory-research-inc/', 'affinipay-holdings-llc/', 'aicent-inc/', 'aldevron/', 'alere-medical-inc/', 'alma-lasers-ltd/', 'altocom-inc/', 'amann-girrbach-ag/', 'american-access-care-llc/', 'american-specialty-health-inc/', 'ameritrade-holding-corporation/', 'amplify-snack-brands-inc/', 'and-1/', 'andovernet/', 'answers/', 'apex-group/', 'appfire/', 'aptean-inc/', 'arcserve/', 'arxan-technologies-inc/', 'asurion/', 'atria-convergence-technologies-act/', 'auction-technology-group-atg/', 'aurora-networks-inc/', 'avg-technologies/', 'babcock-jenkins-inc/', 'babilou/', 'backstage/', 'bats-global-markets-inc/', 'behavioral-health-works/', 'benecon/', 'betashares/', 'bigpoint-gmbH/', 'billdesk/', 'biocomposites/', 'bluepay/', 'bomgar/', 'bsquare-corporation/', 'byggfakta-group/', 'caprock/', 'car-toys-inc/', 'cardtronics-inc/', 'cast-crew/', 'cath-kidston/', 'ccrm/', 'cfra-holdings-llc/', 'chaos/', 'chartered-marketing-services/', 'cipres/', 'circle-graphics/', 'clayton-holdings-inc/', 'cmosis/', 'confluence/', 'conservice/', 'cosentry-llc/', 'creditex-inc/', 'cyncly/', 'cyoptics-inc/', 'cypress-pharmaceutical-inc/', 'dealer-tire-llc/', 'death-wish-coffee/', 'digicert-inc/', 'direct-hit-technologies-inc/', 'dl-software/', 'dnca-finance-sa/', 'dr-lal-pathlabs/', 'drive-assist-uk-ltd/', 'dymatize-enterprises-llc/', 'e-emphasys-technologies/', 'eagle-test-systems-inc/', 'ecircle/', 'edifecs-inc/', 'edreams/', 'elos-medtech-ab/', 'emeria/', 'escher-group-ltd/', 'espublico/', 'evanston-capital-management-llc/', 'evicore-healthcare/', 'exeter-property-group/', 'eyp-mission-critical-facilities-inc/', 'fairstone-group/', 'fargo-electronics-inc/', 'faria-education-group/', 'financial-information-technologies-llc/', 'fincare/', 'finisar-corporation/', 'first-american-corelogic-inc/', 'first-eagle-investment-management-llc/', 'fisher-funds-management-limited/', 'flashtalking/', 'flexera/', 'forgame-holdings-limited/', 'fortra/', 'fotolia-holdings-inc/', 'fractal-analytics-private-limited/', 'freewave-technologies-inc/', 'gamma-technologies/', 'global-360-inc/', 'globeop-financial-services/', 'gong-cha/', 'green-street/', 'hana-group/', 'healix/', 'healthlink-inc/', 'honan-insurance-group/', 'hornetsecurity/', 'icims/', 'idea-cellular-ltd/', 'ideal-cures-pvt-ltd/', 'idera-inc/', 'ifs/', 'igel/', 'image-process-design-inc/', 'incorp-global/', 'indira-ivf/', 'inhealth-md-alliance/', 'insightsoftware/', 'inspired/', 'installshield-software-corporation/', 'instinet-group-incorporated/', 'insurity-inc/', 'intelerad/', 'intercontinental-exchange-inc/', 'internationella-engelska-skolan-ab/', 'interswitch-limited/', 'intralinks-inc/', 'ion-investment-group-ltd/', 'ipg-photonics-corporation-usa/', 'itrs/', 'ivanti-inc/', 'jb-software-inc/', 'jupiter-fund-management/', 'k2-advisors/', 'keeley-asset-management-corp/', 'kinetic-social/', 'kintana-inc/', 'kiwoko/', 'kofax/', 'lava-trading-inc/', 'lawson-software/', 'leadsonline/', 'leadventure/', 'legalzoomcom-inc/', 'list/', 'logistics-health-inc/', 'lumber-liquidators-inc/', 'lumivero/', 'm-and-m-direct-ltd/', 'maintenance-connection/', 'martin-group-inc/', 'mav-beauty-brands/', 'mediaocean/', 'medrisk-inc/', 'merian-global-investors/', 'metropcs-communications-inc/', 'microban-international/', 'micromax-informatics-limited/', 'microseismic-inc/', 'mid-america-pet-food/', 'millennium-health-llc/', 'mis-implants-technologies-ltd/', 'misa/', 'mitratech/', 'monotype-imaging/', 'mq-associates-inc/', 'mri-software/', 'mythic-entertainment-inc/', 'nactarome/', 'national-imaging-associates-inc/', 'national-stock-exchange-of-india-ltd-nse/', 'navia-benefit-solutions-inc/', 'navisys-inc/', 'netnumina-inc/', 'netrisk-group/', 'netscout-systems-inc/', 'netsmart/', 'netwrix/', 'nintex-global-ltd/', 'nugenesis-technologies-corporation/', 'numara-software-inc/', 'numeric-investors-llc/', 'odealim-group/', 'omnia-partners/', 'omniactive-health-technologies/', 'one-call-medical-inc/', 'onlineprinters-holding-gmbh/', 'openlink-financial-inc/', 'orion-advisor-solutions/', 'paulas-choice-llc/', 'pdi/', 'pdqcom/', 'pepperjax-grill/', 'petcurean/', 'petpeople/', 'physiol/', 'planview/', 'plural-inc/', 'plusgrade/', 'power-line-systems/', 'precisely/', 'preferred-freezer-services-inc/', 'prime-rx/', 'priority-software/', 'private-business-inc/', 'procare-solutions/', 'professional-warranty-service-corporation/', 'prometheus-group-holdings-llc/', 'pros-holdings-inc/', 'prudent-corporate-advisory-services/', 'purposebuilt-brands/', 'q-up-systems-inc/', 'quantitative-analytics-inc/', 'quotient-bioresearch-holdings-limited/', 'radiant-logic-inc/', 'radixx-international-inc/', 'rategain/', 'rectangle-health/', 'research-now-group-inc/', 'revalize/', 'rgm-advisors-llc/', 'riskonnect/', 'rldatix/', 'russell-investments/', 'senior-whole-health/', 'shilpa-medicare-limited/', 'smartstream-technologies/', 'soderberg-partners/', 'softmed-systems-inc/', 'softwriters-inc/', 'solabia-group/', 'sophos/', 'sovos/', 'speedcast-international-limited/', 'stackline/', 'stadion-money-management-llc/', 'stonewall-kitchen/', 'surfaces-group/', 'synokem-pharmaceuticals-ltd/', 'targusinfo/', 'tcns-clothing-co-limited/', 'technosylva/', 'tega-industries-ltd/', 'tempur-pedic-international-inc/', 'teoco-corporation/', 'the-collected-group/', 'the-murrayhill-company/', 'thermacell/', 'thinkproject/', 'tierpoint/', 'togethersoft-corporation/', 'touchtunes/', 'towne-park/', 'triumph-healthcare/', 'truck-hero-inc/', 'twin-med-llc/', 'unit4/', 'veracode/', 'viewpoint-inc/', 'vivacy/', 'voyant-technologies-inc/', 'wag-payment-solutions-as-eurowag/', 'wealth-enhancement-group/', 'websidestory-inc/', 'wind-telecom-spa/', 'workwave/', 'yarra-capital-management/', 'yeepay/', 'youth-and-family-centered-services-inc/', 'zadig-voltaire/', 'zifo-rnD-solutions/', 'zoominfo/']

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
    results = soup.find_all('div', class_='relative col-span-25 -ml-outer-gutter min-h-screen bg-white py-xl pr-outer-gutter pl-outer-gutter lg:col-span-21 lg:pr-[15vw] -lg:-mr-outer-gutter')

    for result in results:
        name_element = result.find('h1')
        name = name_element.text.split(' is')[0].split(' was')[0] if name_element else ''

        country_element = result.find_all('p')
        country = country_element[-1].text.split(', ')[-1] if country_element else ''

        web_element = result.find('a', class_='base-link text-red !text-dark')
        web = web_element['href'] if web_element else ''

        data.append([name, country, web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {name}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/ta.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time
print('\n' f'Scraping complete in {elapsed_time:.2f} seconds')

