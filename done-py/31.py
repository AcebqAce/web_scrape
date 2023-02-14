from bs4 import BeautifulSoup

with open('downloaded-html/31.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a')

for result in results:
    web_element = result.get('href')
    print(web_element)