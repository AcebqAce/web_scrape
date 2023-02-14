from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded-html/15.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='investor')
data = []
columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

for result in results:
    investor_element = result.find('span', class_='investor__name')
    investor = investor_element.text if investor_element else ''

    desc_element = result.find('div', class_='desc')
    desc = desc_element.text if desc_element else ''
    desc = desc.replace("\n", '')
    desc = desc.replace("   ", '')

    linkOne_element = result.find_all('a', href=True)
    if linkOne_element:
        linkOne = linkOne_element[0].get('href')
    else:
        linkOne = ''
    
    linkTwo_element = result.find_all('a', href=True)
    if linkTwo_element:
        linkTwo = linkTwo_element[1].get('href') if len(linkTwo_element) > 1 else ''
    else:
        linkTwo = ''

    linkThree_element = result.find_all('a', href=True)
    if linkThree_element:
        linkThree = linkThree_element[2].get('href') if len(linkThree_element) > 2 else ''
    else:
        linkThree = ''

    focusOne_element = result.find_all('li')
    focusOne = focusOne_element[0].text if focusOne_element else ''

    focusTwo_element = result.find_all('li')
    focusTwo = focusTwo_element[1].text if focusTwo_element else ''

    focusThree_element = result.find_all('li')
    focusThree = focusThree_element[2].text if focusThree_element else ''

    portOne_element = result.find_all('li')
    portOne = portOne_element[3].text if portOne_element else ''
    portOne = portOne.replace("\n", '')
    portOneW = result.find_all('li')[3].a['href'] if portOne_element and len(portOne_element[3].find_all('a')) else ''

    portTwo_element = result.find_all('li')
    if len(portTwo_element) >= 5:
        portTwo = portTwo_element[4].text
        portTwo = portTwo.replace("\n", '')
        portTwoW = result.find_all('li')[4].a['href'] if len(portTwo_element[4].find_all('a')) else ''
    else:
        portTwo = ''
        portTwoW = ''

    portThree_element = result.find_all('li')
    if len(portThree_element) >= 6:
        portThree = portThree_element[5].text
        portThree = portThree.replace("\n", '')
        portThreeW = result.find_all('li')[5].a['href'] if len(portThree_element[5].find_all('a')) else ''
    else:
        portThree = ''
        portThreeW = ''

    data.append([investor, desc, linkOne, linkTwo, linkThree, focusOne, focusTwo, focusThree, portOne, portOneW, portTwo, portTwoW, portThree, portThreeW])

df = pd.DataFrame(data, columns=columns)
df = df.replace(r'^\s*$', '', regex=True)
df.to_csv('scraped-csv/15.csv', index=False)