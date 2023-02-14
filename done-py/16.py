from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/16.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h3')
data = []

for result in results:
    name = result.text.strip().split(") ")[-1]

    website_element = result.find_next('a', href=True)
    website = website_element['href'] if website_element else ''

    country_element = result.find_next('li')
    if country_element:
        country = country_element.text.split("Country: ")[-1].strip()
    else:
        country = ''

    city_element = country_element.find_next('li') if country_element else None
    if city_element:
        city = city_element.text.split("City: ")[-1].strip()
    else:
        city = ''

    founded_element = city_element.find_next('li') if city_element else None
    if founded_element:
        founded = founded_element.text.split("Started in: ")[-1].strip()
    else:
        founded = ''
    
    founder_element = founded_element.find_next('li') if founded_element else None
    if founder_element:
        founder = founder_element.text.split("Founders: ")[-1].strip()
    else:
        founder = ''
    
    industry_element = founder_element.find_next('li') if founder_element else None
    if industry_element:
        industry = industry_element.text.split("Industries: ")[-1].strip()
    else:
        industry = ''

    stage_element = industry_element.find_next('li') if industry_element else None
    if stage_element:
        stage = stage_element.text.split("Stages: ")[-1].strip()
    else:
        stage = ''

    minCheck_element = stage_element.find_next('li') if stage_element else None
    if minCheck_element:
        minCheck = minCheck_element.text.split("Minimum check size: ")[-1].strip()
    else:
        minCheck = ''

    maxCheck_element = minCheck_element.find_next('li') if minCheck_element else None
    if maxCheck_element:
        maxCheck = maxCheck_element.text.split("Maximum check size: ")[-1].strip()
    else:
        maxCheck = ''

    numInv_element = maxCheck_element.find_next('li') if maxCheck_element else None
    if numInv_element:
        numInv = numInv_element.text.split("Number of investments: ")[-1].strip()
    else:
        numInv = ''

    numExit_element = numInv_element.find_next('li') if numInv_element else None
    if numExit_element:
        numExit = numExit_element.text.split("Number of exits: ")[-1].strip()
    else:
        numExit = ''

    raised_element = numExit_element.find_next('li') if numExit_element else None
    if raised_element:
        raised = raised_element.text.split("Funds raised: ")[-1].strip()
    else:
        raised_element = ''

    investment_element = raised_element.find_next('li') if raised_element else None
    if investment_element:
        investment = investment_element.text.split("3 remarkable investments: ")[-1].strip()
    else:
        investment = ''

    data.append([name, website, country, city, founded, founder, industry, stage, minCheck, maxCheck, numInv, numExit, raised, investment])

df  = pd.DataFrame(data)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/16.csv', index=False)