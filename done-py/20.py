from bs4 import BeautifulSoup

with open('downloaded-html/20.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h4')

for result in results:
    # web_element = result.find('a', href=True)
    # web = web_element['href'] if web_element else ''

    name = result.text 

    print(name)