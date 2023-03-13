from bs4 import BeautifulSoup

soup = BeautifulSoup(open('downloaded-html/118.html'), 'html.parser')

results = soup.find_all('a', {'data-testid': 'linkElement'})

for result in results:
    if 'href' in result.attrs:
        link = result['href']
        print(link)
