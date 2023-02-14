from bs4 import BeautifulSoup

with open('downloaded-html/26.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

results = soup.find_all('div', class_='small-clients__overlay--container')

for result in results:
    website_elements = result.find('span', class_='small-clients__link link-hover--underline')
    website = website_elements.text if website_elements else ''

    location_elements = result.find('span', class_='small-clients__location bold"')
    location = location_elements.text if location_elements else ''

    print(website)
