from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

base_url = "https://www.indexventures.com/companies/"
page_paths = ['1stdibs/', 'abacusai/', 'adallom/', 'adyen/', 'adzuna/', 'alan/', 'algolia/', 'alkemics/', 'anine-bing/', 'ankorstore/', 'anrok/', 'applyboard-inc/', 'argent/', 'arista-networks/', 'armada-interactive/', 'arthurai/', 'ascend/', 'asos/', 'atlantic-money/', 'atlar/', 'attackiq/', 'aurora/', 'auxmoney/', 'backbone/', 'ballertv/', 'beam/', 'beamery/', 'beauty-pie/', 'because/', 'behavox/', 'betfair/', 'bigger-games/', 'big-health/', 'bird/', 'birdie/', 'bit-odd/', 'bitpay/', 'blablacar/', 'bloom-wild/', 'blue-bottle-coffee/', 'boku/', 'boulevard/', 'brightback/', 'brighthire/', 'brinc/', 'built/', 'capitolis/', 'captain-train/', 'cargoone/', 'castle/', 'catch/', 'causaly/', 'centrify/', 'checkhq/', 'ciphercloud/', 'citymapper/', 'clickhouse/', 'climate/', 'clumio/', 'coalition/', 'cockroach-labs/', 'cocoon/', 'codat/', 'codecademy/', 'codesignal-inc/', 'cohere-inc/', 'collibra/', 'common-room/', 'complyadvantage/', 'confluent/', 'cord/', 'covariantai/', 'coverwallet/', 'cowboy/', 'cradlebio/', 'creative-juice/', 'credit-benchmark/', 'criteo/', 'crossing-minds/', 'culture-amp/', 'curbside/', 'curtsy/', 'cutover/', 'datadog/', 'deepnote/', 'deepscribe-inc/', 'deliveroo/', 'discord/', 'double/', 'dream-games/', 'drivy/', 'dropbox/', 'duffel/', 'duo/', 'edited/', 'elastic/', 'elementl/', 'etsy/', 'evervault/', 'expel/', 'facebook/', 'faceit/', 'factual/', 'farfetch/', 'feathery/', 'figma/', 'fireblocks/', 'flagship/', 'flatfair/', 'flipboard/', 'fonoa/', 'footprint/', 'funding-circle/', 'gather/', 'gatsby/', 'geophy/', 'glossier/', 'goat/', 'gong/', 'good-eggs/', 'goody/', 'grailed/', 'greg/', 'gremlin/', 'gruppo-mutuionline/', 'hebbiaai/', 'hortonworks/', 'humanloop/', 'humu/', 'hutch-games/', 'immersive-gamebox/', 'incident/', 'instabase/', 'intercom/', 'iterable/', 'izettle/', 'jumbo-privacy/', 'jump/', 'just-eat/', 'justpark/', 'justworks/', 'kano/', 'kayrros/', 'king/', 'kong/', 'kry-livi/', 'lacoon/', 'lastfm/', 'layer/', 'lever/', 'gridai/', 'linear/', 'linktree/', 'liquido/', 'privacycom/', 'loctax/', 'lookout/', 'lovefilm/', 'matera/', 'mercantile/', 'metromile/', 'milestone/', 'mimecast/', 'moleskine/', 'monad/', 'monograph/', 'montonio/', 'moo/', 'keeptruckin/', 'motorway/', 'whitehat/', 'myheritage/', 'mysql/', 'nacelle/', 'navabi/', 'net-a-porter/', 'netlog/', 'newfront-insurance/', 'nexthink/', 'noths/', 'notion/', 'nova-credit/', 'novus/', 'oanda/', 'okendo/', 'onefinestay/', 'openx/', 'otrium/', 'otterize/', 'outbrain/', 'ozonru/', 'patreon/', 'pave/', 'peanut/', 'pentaho/', 'peoplevox/', 'pepper/', 'persona/', 'personio/', 'photobox/', 'pilot/', 'pinata-farms/', 'pitch/', 'plaid/', 'plaincom/', 'playfish/', 'pomelola/', 'printify/', 'privalia/', 'prodigy-finance/', 'productboard/', 'pure-storage/', 'qapa/', 'gtmhub/', 'quill/', 'fanbase/', 'raisin/', 'readyset/', 'rebtel/', 'rec-room/', 'remotecom/', 'resistant-ai/', 'revenuecat-inc/', 'revolut/', 'rightscale/', 'robinhood/', 'roblox/', 'rohlikcz/', 'roli/', 'rooser/', 'rpx-corporation/', 'safetyculture/', 'sanlo/', 'savvy/', 'scale/', 'science-exchange/', 'scoop/', 'second-home/', 'secret-escapes/', 'seedcamp/', 'seedlegals/', 'servicetitan/', 'seso/', 'shapeways/', 'shopmonkey/', 'signal-sciences/', 'silverfin/', 'skype/', 'slack/', 'socialbakers/', 'sofia/', 'solvo/', 'sourceful/', 'spendesk/', 'squarespace/', 'stack-exchange/', 'starburst/', 'strapi/', 'stytch/', 'supercell/', 'super-conductive/', 'super-evil-megacorp/', 'supersolid/', 'swiftkey/', 'swile/', 'sylvera/', 'tactic/', 'tactile-games/', 'taktile/', 'taxfix/', 'teatime-games/', 'teemo/', 'tekion/', 'temporal/', 'the-business-of-fashion/', 'the-garden/', 'tiney/', 'toolbx/', 'topi/', 'transcend/', 'transform/', 'trello/', 'trialpay/', 'trolltech/', 'trouva/', 'trustpilot/', 'twelve-labs/', 'typeform/', 'ubiquity6/', 'upollo/', 'lustre/', 'vouch/', 'wealthfront/', 'weaviate/', 'wetravel/', 'transferwise/', 'wizio/', 'workbounce/', 'xata/', 'zendesk/', 'zuora/']

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
    results = soup.find_all('a', class_='company-description__link company-description__link--external')

    for result in results:
        web = result['href']

        data.append([web])
        time.sleep(random.uniform(1, 3))

        print(f'Scraped {web}')

    print(f'Finished scraping {url}')
    df = pd.DataFrame(data)
    df.to_csv('scraped-csv/indexvent.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time

