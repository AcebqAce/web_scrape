from bs4 import BeautifulSoup

with open('downloaded-html/96.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='pc-card')

for result in results:
    link = result['href']

    print(link)