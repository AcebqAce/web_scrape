from bs4 import BeautifulSoup

with open('downloaded-html/98.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='c-portfolio_item-link')

for result in results:
    link_element = result.find('a')
    link = link_element['href'] if link_element else ''

    print(link)