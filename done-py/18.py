from bs4 import BeautifulSoup

with open('downloaded-html/18.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('h2')

for result in results:
    name = result.text

    print(name)