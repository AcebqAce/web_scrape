from bs4 import BeautifulSoup

soup = BeautifulSoup(open('downloaded-html/93.html'), 'html.parser')

results = soup.find_all('p')
for result in results:
    name = result.text

    print(name)