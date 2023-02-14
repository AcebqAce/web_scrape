from bs4 import BeautifulSoup

with open('downloaded-html/22.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='elementor-widget-container')

for result in results:
    website_elements = result.find('a', href=True)
    website = website_elements['href'] if website_elements else ''

    print(website)