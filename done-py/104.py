from bs4 import BeautifulSoup

with open('downloaded-html/104.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('a', class_='ww-link')
for result in results:
    web = result['href']
    
    print(web)