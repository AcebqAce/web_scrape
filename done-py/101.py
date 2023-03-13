from bs4 import BeautifulSoup

with open('downloaded-html/101.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='company-card_item')

for result in results:
    web_element = result.find('a')
    web = web_element['href'] if web_element else ''

    print(web)